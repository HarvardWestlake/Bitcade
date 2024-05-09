import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { useWallet } from '../components/WalletContext';

const HorseRacingGameComponent = ({ contractAddress }) => {
  const { walletAddress, contracts } = useWallet();
  const [racers, setRacers] = useState([]);
  const [raceStarted, setRaceStarted] = useState(false);
  const [raceDistance, setRaceDistance] = useState(0);
  const [loading, setLoading] = useState(false);
  const [joinedGame, setJoinedGame] = useState(false);

  const MIN_RACERS_REQUIRED = 2; // Define the minimum number of racers required to start the race

  const gameContract =
    contracts && contracts.HorseRacing
      ? new ethers.Contract(
          contractAddress,
          contracts.HorseRacing,
          walletAddress
        )
      : null;

  const joinGame = async () => {
    if (!gameContract) {
      console.log('Join game button is pressed');
    }
    setLoading(true);
    try {
      // Call the joinGame method in the smart contract
      await gameContract.joinGame();
      // Update racers state
      const updatedRacers = await gameContract.getRacers();
      setRacers(updatedRacers);
      // Check if enough racers have joined to start the race
      const enoughRacers = updatedRacers.length >= MIN_RACERS_REQUIRED;
      if (enoughRacers && !raceStarted) {
        startRace();
      }
      // Set joinedGame to true
      setJoinedGame(true);
    } catch (error) {
      console.error('Error joining game:', error);
      alert('Failed to join game');
    }
    setLoading(false);
  };

  const startRace = async () => {
    if (!gameContract) return;
    setLoading(true);
    try {
      // Call the startRace method in the smart contract
      await gameContract.startRace();
      // Set raceStarted to true
      setRaceStarted(true);
    } catch (error) {
      console.error('Error starting race:', error);
      alert('Failed to start race');
    }
    setLoading(false);
  };

  useEffect(() => {
    if (walletAddress && gameContract) {
      // Fetch initial game state on component mount
      // Example: fetchRaceDetails();
    }
  }, [walletAddress, gameContract]);

  return (
    <div
      className='horse-racing-game-component'
      style={{ width: '100%', padding: '10px' }}
    >
      {!joinedGame ? (
        <div>
          <h3>Welcome to Horse Racing Game!</h3>
          <button onClick={joinGame} disabled={!gameContract}>
            Join Game
          </button>
        </div>
      ) : (
        <div className='race-track'>
          <h3>Race Track</h3>
          <div className='racers'>
            {racers.map((racer, index) => (
              <div
                key={index}
                className='racer'
                style={{
                  position: 'absolute',
                  top: `${index * 20}px`,
                  left: `${racer.position}px`,
                  width: '20px',
                  height: '20px',
                  backgroundColor: 'blue',
                }}
              />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default HorseRacingGameComponent;
