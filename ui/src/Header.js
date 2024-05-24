import React, { useState } from "react";
import WalletConnect from "./components/WalletConnect";

const Header = () => {
  const [balance, setBalance] = useState("0.00");

  return (
    <header className="header">
      <head>
        <link
          href="https://fonts.cdnfonts.com/css/arcade-classic"
          rel="stylesheet"
        />
      </head>
      <div className="header-left"> BLOCADE</div>
      <div className="header-logo">
        <img src="logo512.png" width="100" alt="Blocade Logo" />
      </div>
      <div className="header-right">
        <div id="wallet-button">
          <WalletConnect setBalance={setBalance} />
        </div>

        <div className="balance">Balance: {balance} ETH</div>
      </div>
    </header>
  );
};

export default Header;
