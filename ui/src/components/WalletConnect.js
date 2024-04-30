import React from 'react';
import { useWallet } from './WalletContext'; // Import the useWallet hook from your context

const WalletConnect = () => {
  const { walletAddress, balance, connectWallet } = useWallet(); // Use the context values

  // Function to format the wallet address
  const formatAddress = (address) => {
    return address ? `0x${address.slice(2, 6)}...${address.slice(-4)}` : '';
  };

  return (
    <div className="wallet-connect">
      {walletAddress ? (
        <div>
          <h4 className="wallet-address">{formatAddress(walletAddress)}</h4>
          <p>Balance: {balance} ETH</p> {/* Assuming balance is in ETH */}
        </div>
      ) : (
        <button className="btn" onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletConnect;
