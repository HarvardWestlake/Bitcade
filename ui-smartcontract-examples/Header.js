import React, { useState } from 'react';
import WalletConnect from './components/WalletConnect';

const Header = () => {
  const [balance, setBalance] = useState('0.00');

  return (
    <header className="header">
      <div className="header-left">Blocade</div>
      <div className="header-middle">Balance: {balance} ETH</div>
      <div className="header-right">
        <WalletConnect setBalance={setBalance} />
      </div>
    </header>
  );
};

export default Header;
