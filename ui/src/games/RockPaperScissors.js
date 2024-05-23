import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { useWallet } from '../components/WalletContext';
import '../App.css';
import { useCookies } from 'react-cookie';


const RockPaperScissors = ({ contractAddress }) => {
  const { walletAddress, contracts, signer } = useWallet();
  const [userChoice, setUserChoice] = useState(null);
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [inGame, setInGame] = useState(false);
  const [testBalance, setTestBalance] = useState(0);
  const [gameContract, setGameContract] = useState(null);
  const [betAmount, setBetAmount] = useState(0);
  const [gameStatus, setGameStatus] = useState('');
  const [p1, setP1] = useState({
    id: 0,
    choice: 'uncommitted',
  })
  const [p2, setP2] = useState({
    id: 0,
    choice: 'uncommitted',
  })
  const [id, setId] = useState(0);
  const [cookies, setCookie] = useCookies([]);
  const [revealReady, setRevealReady] = useState(false);

  


  useEffect(() => {
    if (walletAddress && contracts && contracts.RockPaperScissors) {
      setGameContract(new ethers.Contract(contractAddress, contracts.RockPaperScissors, signer))
      console.log('Game Contract Initialized:');
    } else {
      console.log('Provider, walletAddress, or contracts not available');
     
    }
  },  [walletAddress, contracts, contractAddress]);


  const choices = ['Rock', 'Paper', 'Scissors'];


  useEffect(() => {
    getBalance();
  }, [gameContract]);

  const getCookieValue = (type, id) => {
    const cookieName = `${type}${id}`;
    return cookies[cookieName];
  };


  const handleGameOptionClick = async (option) => {
    if (option === 'create') {
      const bet = prompt('Enter the bet amount');
      const opponent = prompt('Enter the address of the player you want to play with');
      await createGame(bet, opponent);
    } else if (option === 'join') {
      const gameId = prompt('Enter the game ID');
      await viewGame(gameId);
      setInGame(true);
    } else if (option === 'addBalance') {
      let amount = prompt('Enter the amount to add');
      await addBalance(amount);
    } else if (option === 'Rock' || option === 'Paper' || option === 'Scissors') {
      if(option == 'Rock') {
        await playGame(1);
      } else if(option == 'Paper') {
        await playGame(2);
      } else {
        await playGame(3);
      }
    } else if (option === 'Reveal') {
      await revealGame();
    }
  };

  const addBalance = async (amount) => {
    if (!gameContract) return;
    setLoading(true);
    try {
      const addBalanceTx = await gameContract.initBalance(parseInt(amount));
      const receipt = await addBalanceTx.wait();
      console.log(receipt);
    } catch (error) {
      console.error('Error adding balance:', error);
      alert('Failed to add balance');
    }
    setLoading(false);
  };

  const getBalance = async () => {
    if (!gameContract) return;
    setLoading(true);
    try {
      const getAccountBalanceTx = await gameContract.getAccountBalance();
      const balance = await getAccountBalanceTx.toString();

      setLoading(false);
      console.log('Balance:', balance);
      setTestBalance(balance);
    } catch (error) {
      console.error('Error getting balance:', error);
      alert('Failed to get balance');
    }
    setLoading(false);
  };

  const viewGame = async (gameId) => {
    if (!gameContract) return;
    setLoading(true);
    try {
      const game = await gameContract.getGame(gameId);
      const bet = game[2].toString();
      setId(gameId);
      console.log('Game:', game);
      const winner = game[3].toString();
      const draw = game[4].toString();
      const player1 = game[0];
      const player2 = game[1];
      setP1({
        id: player1[0] == walletAddress ? "You" : player1[0],
        choice: player1[2] ? ( player1[1].toString() == "1" ? "Rock" : (player1[1].toString() == "2" ? "Paper" : "Scissors")  ) : (player1[3] == "0x0000000000000000000000000000000000000000000000000000000000000000"
         ? 'uncommitted' : "Committed"),
      });
      setP2({
        id: player2[0] == walletAddress ? "You" : player2[0],
        choice: player2[2] ? player2[1].toString() : (player2[3] == "0x0000000000000000000000000000000000000000000000000000000000000000"
        ? 'uncommitted' : "Committed"),
      });

      if(player1[0] == walletAddress && !player1[2] && player1[3] != "0x0000000000000000000000000000000000000000000000000000000000000000") {
        setRevealReady(true);
      } else if(player2[0] == walletAddress && !player2[2] && player2[3] != "0x0000000000000000000000000000000000000000000000000000000000000000") {
        setRevealReady(true);
      }
      

      if (winner !== '0x0000000000000000000000000000000000000000') {
        setGameStatus('Winner: ' + winner);
      } else if (draw === 'true') {
        setGameStatus('Game Draw');
      }
      else {
        setGameStatus('Game in progress');
      }
      setBetAmount(bet)
    } catch (error) {
      console.error('Error getting game:', error);
      alert('Failed to get game');
    }
    setLoading(false);
  }

  const createGame = async (bet, opponent) => {
    if (!gameContract) return;
    setLoading(true);
    try {
      let _bet = parseInt(bet); // Ensure bet is in correct format
      const createTx = await gameContract.createGame(_bet, opponent);
      const receipt = await createTx.wait();
      console.log(receipt.logs[0].args[0]);
      alert('Game created successfully with ID: ' + receipt.logs[0].args[0].toString())
    } catch (error) {
      console.error('Error creating game:', error);
      alert('Failed to create game');
    }
    setLoading(false);
  }

  const playGame = async (choice) => {
    if (!gameContract) return;
    setLoading(true);
    try {
      const rand = Math.floor(Math.random() * 10000000000000);
      setCookie(`rand${id}`, rand, { path: '/' });
      setCookie(`choice${id}`, choice, { path: '/' });
      const playTx = await gameContract.joinGame(parseInt(id), parseInt(choice), parseInt(rand));
      const receipt = await playTx.wait();
      console.log(receipt);
      const result = receipt?.logs[0]?.args[0]?.toString();
      console.log('Result:', result);
    } catch (error) {
      console.error('Error playing game:', error);
      alert('Failed to play game');
    }
    setLoading(false);
  }

  const revealGame = async () => {
    if (!gameContract) return;
    setLoading(true);
    try {
      const rand = getCookieValue(`rand`, id);
      const choice = getCookieValue(`choice`, id);
      console.log('Rand:', rand);
      console.log('Choice:', choice);
      const revealTx = await gameContract.revealChoice(parseInt(id), parseInt(choice), parseInt(rand));
      const receipt = await revealTx.wait();
      console.log(receipt);
    } catch (error) {
      console.error('Error revealing game:', error);
      alert('Failed to reveal game');
    }
    setLoading(false);
  }

  return (
    <div className="flex flex-col items-center justify-center w-1/2 bg-gray-100">
      <div className="flex space-x-4">
        <div className="bg-gray-200 p-4 rounded-lg">
          <h2 className="text-xl font-semibold">Test Balance</h2>
          <p className="text-2xl font-bold">${testBalance}</p>
        </div>
        <button
          onClick={() => handleGameOptionClick('addBalance')}
          className="px-6 py-2 bg-yellow-500 text-white rounded-lg hover:bg-yellow-700"
        >
          Add Test Balance
        </button>
      </div>

      <h1 className="text-4xl font-bold mb-8">Rock Paper Scissors</h1>
      {inGame ? (
        <>
    <div className="flex flex-col items-center">
      <div className="flex justify-between space-x-4">
        <div>
          <h2>Player 1</h2>
          <p>Choice: {p1.choice}</p>
          <p>ID: {p1.id}</p>
          <button
            onClick={() => handleGameOptionClick('Rock')}
            className={`px-6 py-2 rounded-lg ${
              "You" === p1.id && p1.choice == 'uncommitted' ? 'bg-gray-500 text-white hover:bg-gray-700' : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
            disabled={"You" !== p1.id || p1.choice !== 'uncommitted'}
          >
            Rock
          </button>
          <button
            onClick={() => handleGameOptionClick('Paper')}
            className={`px-6 py-2 rounded-lg ${
              "You" === p1.id && p1.choice == 'uncommitted' ? 'bg-gray-500 text-white hover:bg-gray-700' : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
            disabled={"You" !== p1.id || p1.choice !== 'uncommitted'}
          >
            Paper
          </button>
          <button
            onClick={() => handleGameOptionClick('Scissors')}
            className={`px-6 py-2 rounded-lg ${
              "You" === p1.id && p1.choice == 'uncommitted' ? 'bg-gray-500 text-white hover:bg-gray-700' : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
            disabled={"You" !== p1.id || p1.choice !== 'uncommitted'}
          >
            Scissors
          </button>
        </div>
        <div>
          <h2>Player 2</h2>
          <p>Choice: {p2.choice}</p>
          <p>ID: {p2.id}</p>
          <button
            onClick={() => handleGameOptionClick('Rock')}
            className={`px-6 py-2 rounded-lg ${
              "You" === p2.id && p2.choice == 'uncommitted' ? 'bg-gray-500 text-white hover:bg-gray-700' : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
            disabled={"You" !== p2.id || p2.choice !== 'uncommitted'}
          >
            Rock
          </button>
          <button
            onClick={() => handleGameOptionClick( 'Paper')}
            className={`px-6 py-2 rounded-lg ${
              "You" === p2.id && p2.choice == 'uncommitted' ? 'bg-gray-500 text-white hover:bg-gray-700' : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
            disabled={"You" !== p2.id || p2.choice !== 'uncommitted'}
          >
            Paper
          </button>
          <button
            onClick={() => handleGameOptionClick( 'Scissors')}
            className={`px-6 py-2 rounded-lg ${
              "You" === p2.id && p2.choice == 'uncommitted' ? 'bg-gray-500 text-white hover:bg-gray-700' : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
            disabled={"You" !== p2.id || p2.choice !== 'uncommitted'}
          >
            Scissors
          </button>
        </div>
      </div>
      {revealReady ? (
      <div className="mt-4">
        <button
          onClick={() => handleGameOptionClick('Reveal')}
          className="px-6 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-700"
        >
          Reveal Choices
        </button>
      </div>
      ) : ( <></>)}
      <div className="mt-4">
        <h3>Bet amount: ${betAmount}</h3>
      </div>
      <div className="mt-4">
        <h3>Game Result: {gameStatus}</h3>
      </div>
    </div>
          
        </>
      ) : (
        <div className="flex space-x-4">
          <button
            onClick={() => handleGameOptionClick('create')}
            className="px-6 py-2 bg-green-500 text-white rounded-lg hover:bg-green-700"
          >
            Create Game
          </button>
          <button
            onClick={() => handleGameOptionClick('join')}
            className="px-6 py-2 bg-purple-500 text-white rounded-lg hover:bg-purple-700"
          >
            View/Join Game
          </button>
        </div>
      )}
    </div>
  );
}

export default RockPaperScissors;
