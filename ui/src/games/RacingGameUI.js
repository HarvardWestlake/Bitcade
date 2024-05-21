import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { useWallet } from '../components/WalletContext'; // Import the useWallet hook from your context if needed

const HorseRacingGameComponent = ({ contractAddress }) => {
  const { walletAddress, contracts } = useWallet();
  const [raceStarted, setRaceStarted] = useState(false);
  const [racers, setRacers] = useState([]);
  const [raceDistance, setRaceDistance] = useState(1000); // Example race distance for mock data
  const [positions, setPositions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [winner, setWinner] = useState(null); // State to track the winner

  const mockRace = true; // Set this to true for mock race, false to use smart contract

  const mockRacers = [
    {
      address: 'Buttercup',
      speed: 10,
      level: 5,
      isBoosted: false,
      position: 0,
    },
    {
      address: 'Seabiscuit',
      speed: 12,
      level: 4,
      isBoosted: false,
      position: 0,
    },
    { address: 'Bob', speed: 8, level: 6, isBoosted: false, position: 0 },
  ];

  const raceContract =
    contracts && contracts.Racing
      ? new ethers.Contract(contractAddress, contracts.Racing, walletAddress)
      : null;

  const startRace = async () => {
    setLoading(true);
    setWinner(null); // Reset winner state
    if (mockRace) {
      setRaceStarted(true);
      setRacers(mockRacers);
      setPositions(
        mockRacers.map((racer) => ({ address: racer.address, position: 0 }))
      );
    } else {
      try {
        const startTx = await raceContract.startRace();
        await startTx.wait();
        setRaceStarted(true);
      } catch (error) {
        console.error('Error starting race:', error);
        alert('Failed to start race');
      }
    }
    setLoading(false);
  };

  const boostSpeed = async (racerAddress) => {
    setLoading(true);
    if (mockRace) {
      const updatedRacers = racers.map((racer) =>
        racer.address === racerAddress ? { ...racer, isBoosted: true } : racer
      );
      setRacers(updatedRacers);
    } else {
      try {
        const boostTx = await raceContract.boostSpeed();
        await boostTx.wait();
      } catch (error) {
        console.error('Error boosting speed:', error);
        alert('Failed to boost speed');
      }
    }
    setLoading(false);
  };

  const fetchRaceStatus = async () => {
    setLoading(true);
    if (mockRace) {
      // Mock fetching race status
      const positionsArray = mockRacers.map((racer) => ({
        address: racer.address,
        position: racer.position,
      }));
      setPositions(positionsArray);
    } else {
      try {
        const racersArray = await raceContract.Racers();
        const raceDistanceValue = await raceContract.raceDistance();
        const positionsArray = await Promise.all(
          racersArray.map(async (racer) => {
            const stats = await raceContract.RacerStats(racer);
            return { address: racer, position: stats.position };
          })
        );

        setRacers(racersArray);
        setRaceDistance(raceDistanceValue);
        setPositions(positionsArray);
      } catch (error) {
        console.error('Error fetching race status:', error);
      }
    }
    setLoading(false);
  };

  const simulateRace = () => {
    if (!raceStarted) return;

    const interval = setInterval(() => {
      setPositions((prevPositions) => {
        let raceFinished = false; // Flag to track if any horse finished the race
        const newPositions = prevPositions.map((racer) => {
          const racerStats = racers.find((r) => r.address === racer.address);
          const randomFactor = Math.random() * 0.5 + 0.75; // Random factor between 0.75 and 1.25
          const movement =
            racerStats.speed *
            racerStats.level *
            (racerStats.isBoosted ? 1.1 : 1) *
            randomFactor;
          const newPosition = racer.position + movement;

          if (newPosition >= raceDistance && !winner) {
            setWinner(racer.address); // Set winner if race is finished
            raceFinished = true; // Set flag to true if any horse finishes the race
          }

          return {
            ...racer,
            position: newPosition,
          };
        });

        if (raceFinished) {
          clearInterval(interval); // Stop the race if any horse finishes
        }

        return newPositions;
      });
    }, 1000);
  };

  useEffect(() => {
    if (raceStarted) {
      if (mockRace) {
        simulateRace();
      } else {
        fetchRaceStatus();
      }
    }
  }, [raceStarted]);

  const getHorseStyle = (position) => {
    const percentage = (position / raceDistance) * 90; // Adjusted to 90% to leave room for finish line
    return { left: `${percentage}%` }; // Removed transform for the horse emoji
  };

  return (
    <div
      className='horse-racing-game-component'
      style={{ width: '700px', border: '1px solid white', padding: '10px' }}
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
            {winner && <h4>Winner: {winner}</h4>} {/* Display the winner */}
            <div className='race-track'>
              <div className='finish-line' style={{ left: '90%' }}>
                Finish Line
              </div>
              {positions.map((racer, index) => (
                <div
                  key={racer.address}
                  className='horse'
                  style={{
                    ...getHorseStyle(racer.position),
                    top: `${index * 40}px`,
                  }}
                >
                  <span className='horse-emoji' role='img' aria-label='horse'>
                    🐎
                  </span>
                  <span className='horse-name'>{racer.address}</span>
                  <span className='horse-distance'>
                    {Math.round(racer.position)}m
                  </span>
                </div>
              ))}
            </div>
          </div>
        </>
      )}
      <style jsx>{`
        .race-track {
          position: relative;
          width: calc(100% + 100px); /* Extend width for horse details */
          height: ${racers.length *
          40}px; /* Adjust height based on number of racers */
          border: 1px solid black;
          background: #4caf50; /* Green background for the track */
          margin-top: 20px;
          overflow: hidden; /* Ensure horses are visible after finishing */
        }

        .horse {
          position: absolute;
          transition: left 1s;
          display: flex;
          align-items: center;
        }

        .horse-emoji {
          margin-right: 10px; /* Adjust spacing */
          transform: scaleX(-1); /* Mirror only the horse emoji */
        }

        .horse-name,
        .horse-distance {
          font-weight: bold;
          color: white;
        }

        .horse-name {
          margin-right: 10px; /* Adjust spacing */
        }

        .horse-distance {
          margin-right: 20px; /* Adjust spacing */
        }

        .finish-line {
          position: absolute;
          width: 10px;
          height: 100%;
          background: red;
          text-align: center;
          color: white;
          transform: translateX(-50%);
        }
      `}</style>
    </div>
  );
};

export default HorseRacingGameComponent;
