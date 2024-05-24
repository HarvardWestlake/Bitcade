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
      <div className="header-left">
        <div id="blocade-title">BLOCADE</div>
        <form action="" class="search-bar">
          <input type="search" name="search" pattern=".*\S.*" required />
          <button class="search-btn" type="submit">
            <span>Search</span>
          </button>
        </form>
      </div>
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
