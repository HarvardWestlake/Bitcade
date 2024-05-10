import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { useWallet } from '../components/WalletContext'; // Import the useWallet hook from your context if needed

const ListGames = ({ contractAddress }) => {
    const { walletAddress, contracts } = useWallet();
    const [gameResult, setGameResult] = useState('');
    const [accountBalance, setAccountBalance] = useState(0);
    const [loading, setLoading] = useState(false);
    const [showDescriptions, setShowDescriptions] = useState(false); // Define showDescriptions state

    // Instance of the contract
    const gameContract = contracts && contracts.ExampleGame
        ? new ethers.Contract(contractAddress, contracts.ExampleGame, walletAddress)
        : null;

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
        }
    }, [walletAddress, gameContract]);

    // Function to toggle showDescriptions state
    const toggleDescription = () => {
        setShowDescriptions(!showDescriptions);
    };

    return (
        <>
            <div className="list-games" style={{ width: "300px", border: "1px solid white", padding: "10px", float: "left", marginRight: "20px", marginBottom: "20px" }}>
                <h3>Example Game</h3>
                {loading ? (
                    <p>Loading...</p>
                ) : (
                    <>
                        <button onClick={playGame} disabled={!gameContract}>Play Game</button>
                        <p>Game Result: {gameResult}</p>
                        <p>Random Number: {randomNumber}</p>
                        <p>Account Balance: {accountBalance} ETH</p>
                        <button onClick={toggleDescription}>Show Description</button>
                        {showDescriptions && (
                            <div>
                                <p>This is a brief description of the game...</p>
                            </div>
                        )}
                    </>
                )}
            </div></>
    );
};

export default ListGames;
