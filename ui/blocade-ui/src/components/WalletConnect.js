import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

const WalletConnect = ({ setBalance }) => {
  const [walletAddress, setWalletAddress] = useState("");

  const connectWallet = async () => {
    try {
      const provider = new ethers.BrowserProvider(window.ethereum);
      await provider.send('eth_requestAccounts', []);
      const signer = await provider.getSigner();
      const address = await signer.getAddress();
      setWalletAddress(address);
      await fetchBalance(address); // Fetch initial balance upon wallet connection
    } catch (error) {
      console.error("Error connecting wallet:", error);
      alert("Failed to connect wallet. Please try again.");
    }
  };

  // Function to format the wallet address
  const formatAddress = (address) => {
    return address ? `0x${address.slice(2, 6)}...${address.slice(-4)}` : '';
  };

  // Function to fetch the initial balance from Firebase
  const fetchBalance = async (address) => {
    try {
      const response = await fetch(`http://localhost:3001/balance/${address}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setBalance(data.balance);
    } catch (error) {
      console.error("Error fetching balance:", error);
    }
  };

  // Call fetchBalance when walletAddress changes
  useEffect(() => {
      if (walletAddress) {
        fetchBalance(walletAddress);
      }
  }, [walletAddress]);

  return (
    <div className="wallet-connect">
      {walletAddress ? (
        <div>
          <h4 className="wallet-address">{formatAddress(walletAddress)}</h4>
        </div>
      ) : (
        <button className="btn" onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletConnect;
