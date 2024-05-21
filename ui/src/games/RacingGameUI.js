import React, { useState, useEffect } from 'react';
import { useWallet } from '../components/WalletContext'; // Import the useWallet hook from your context if needed

const HorseRacingGameComponent = ({ contractAddress }) => {
  const { walletAddress, contracts } = useWallet();
  const [raceStarted, setRaceStarted] = useState(false);
  const [racers, setRacers] = useState([]);
  const [raceDistance, setRaceDistance] = useState(1000); // Example race distance
  const [positions, setPositions] = useState([]);
  const [loading, setLoading] = useState(false);

  const mockRacers = [
    { address: '0xRacer1', speed: 10, level: 5, isBoosted: false, position: 0 },
    { address: '0xRacer2', speed: 12, level: 4, isBoosted: false, position: 0 },
    { address: '0xRacer3', speed: 8, level: 6, isBoosted: false, position: 0 },
  ];

  const startRace = async () => {
    setLoading(true);
    setRaceStarted(true);
    setRacers(mockRacers);
    setPositions(
      mockRacers.map((racer) => ({ address: racer.address, position: 0 }))
    );
    setLoading(false);
  };

  const boostSpeed = async (racerAddress) => {
    setLoading(true);
    const updatedRacers = racers.map((racer) =>
      racer.address === racerAddress ? { ...racer, isBoosted: true } : racer
    );
    setRacers(updatedRacers);
    setLoading(false);
  };

  const simulateRace = () => {
    if (!raceStarted) return;

    const interval = setInterval(() => {
      setPositions((prevPositions) => {
        const newPositions = prevPositions.map((racer) => {
          const racerStats = racers.find((r) => r.address === racer.address);
          const movement =
            racerStats.speed *
            racerStats.level *
            (racerStats.isBoosted ? 1.1 : 1);
          const newPosition = racer.position + movement;

          return {
            ...racer,
            position: newPosition >= raceDistance ? raceDistance : newPosition,
          };
        });

        if (newPositions.some((racer) => racer.position >= raceDistance)) {
          clearInterval(interval);
        }

        return newPositions;
      });
    }, 1000);
  };

  useEffect(() => {
    if (raceStarted) {
      simulateRace();
    }
  }, [raceStarted]);

  return (
    <div
      className='horse-racing-game-component'
      style={{ width: '300px', border: '1px solid white', padding: '10px' }}
    >
      <h3>Horse Racing Game</h3>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <>
          {!raceStarted ? (
            <button onClick={startRace} disabled={loading}>
              Start Race
            </button>
          ) : (
            <>
              {racers.map((racer) => (
                <button
                  key={racer.address}
                  onClick={() => boostSpeed(racer.address)}
                  disabled={loading}
                >
                  Boost Speed for {racer.address}
                </button>
              ))}
            </>
          )}
          <div>
            <h4>Race Status</h4>
            <p>Race Distance: {raceDistance}</p>
            <ul>
              {positions.map((racer) => (
                <li key={racer.address}>
                  Racer {racer.address}: {racer.position}
                </li>
              ))}
            </ul>
          </div>
        </>
      )}
    </div>
  );
};

export default HorseRacingGameComponent;
