import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { useWallet } from '../components/WalletContext'; // Import the useWallet hook from your context if needed

const AceArcade = ({ contractAddress }) => {
    const { walletAddress, contracts } = useWallet();
    const [gameResult, setGameResult] = useState('');
    const [randomNumber, setRandomNumber] = useState(null);
    const [accountBalance, setAccountBalance] = useState(0);
    const [loading, setLoading] = useState(false);
    const [bettingAmount, setBettingAmount] = useState("");
    const [userCards, setUserCards] = useState("1,2");
    const [cpuCards, setCpuCards] = useState("10,x");
    const [cardSum, setCardSum] = useState("3");

    let userCardArr = [1, 2]; //These integers could be replaced by random number variables
    let cpuCardArr = [10, "x"] //These integers could be replaced by random number variables

    // Instance of the contract
    const gameContract = contracts && contracts.ExampleGame
        ? new ethers.Contract(contractAddress, contracts.ExampleGame, walletAddress)
        : null;

    const handleOnChangeBettingAmount = e => {
        setBettingAmount(e.target.value);
    }
    
    const handleStart = e => {
       const newBalance = accountBalance - bettingAmount;
       setAccountBalance(newBalance);

       setUserCards(userCardArr.toString());
       setCpuCards(cpuCardArr.toString());
       setCardSum(3);
    }

    const handleHit = e => {
        let newArray = userCardArr.concat(3);
        userCardArr = newArray;
        setUserCards(userCardArr.toString());
        setCardSum(6);
    }

    const playGame = async () => {
        if (!gameContract) return;
        setLoading(true);
        try {
            const playTx = await gameContract.play();
            const receipt = await playTx.wait();
            const playResult = receipt.events?.filter((x) => x.event === 'Play')[0].args.result;
            setGameResult(playResult);
        } catch (error) {
            console.error('Error playing game:', error);
            alert('Failed to play game');
        }
        setLoading(false);
    };

    const fetchRandomNumber = async () => {
        if (!gameContract) return;
        setLoading(true);
        try {
            const randNumber = await gameContract.rand();
            setRandomNumber(randNumber.toString());
        } catch (error) {
            console.error('Error fetching random number:', error);
        }
        setLoading(false);
    };

    const fetchAccountBalance = async () => {
        if (!gameContract || !walletAddress) return;
        setLoading(true);
        try {
            const balance = await gameContract.accountBalance(walletAddress);
            //setAccountBalance(ethers.utils.formatEther(balance));
        } catch (error) {
            console.error('Error fetching account balance:', error);
        }
        setLoading(false);
    };

    // UseEffect to fetch balance on load
    useEffect(() => {
        if (walletAddress && gameContract) {
            fetchAccountBalance();
            fetchRandomNumber();
        }
    }, [walletAddress, gameContract]);

    return (
      <div>
        <h3>Ace Arcade</h3>
        Enter Betting Amount<input type="text" value={bettingAmount} onChange={handleOnChangeBettingAmount} />
        <button onClick={handleStart}>Bet</button>
        <p>Your Hand: {userCards}      Sum: {cardSum}</p>
        <p>CPU Hand: {cpuCards}</p>
        <button onClick={handleHit}>Hit</button>
        <button>Stay</button>
      </div>
    );
};

export default AceArcade;
