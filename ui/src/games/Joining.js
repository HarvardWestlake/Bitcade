import { ethers } from 'ethers';
import React, { useState } from 'react';
import { useWallet } from '../components/WalletContext';

const Joining = ({ contractAddress }) => {
    const { walletAddress, contracts } = useWallet();
    const [gameResult, setGameResult] = useState('');
    const [loading, setLoading] = useState(false);
    const gameContract = contracts && contracts.ExampleGame
    ? new ethers.Contract(contractAddress, contracts.ExampleGame, walletAddress)
    : null;

    const joinGame = async () => {
        if (!gameContract) return;
        setLoading(true);
        try {
            const joinTx = await gameContract.play();
            const receipt = await joinTx.wait();
            const playResult = receipt.events?.filter((x) => x.event === 'Play')[0].args.result;
            setGameResult(playResult);
        } catch (error) {
            console.error('Error joining game:', error);
            alert('Failed to join game');
        }
        setLoading(false);
    };
    return (
        <div className="example-game-component" style={{ width: "300px", border: "1px solid white", padding: "10px" }}>
            <h3>AAAAAA</h3>
            {loading ? (
                <p>Loading...</p>
            ) : (
                <>
                    <button onClick={joinGame} disabled={!gameContract}>Play Game</button>
                    <p>Game Result: {gameResult}</p>
                </>
            )}
        </div>
    );
}
export default Joining;