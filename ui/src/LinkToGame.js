import React, { useState, useEffect } from "react";

import { Link } from "react-router-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import GamePage from "./GamePage.js";
import { ethers } from "ethers";
import { useWallet } from "./components/WalletContext"; // Import the useWallet hook from your context if needed

const LinkToGame = ({ gameName }) => {
  const goToGame = async () => {
    try {
    } catch (error) {
      console.error("Error playing game:", error);
      alert("Failed to play game" + error);
    }
  };

  return (
    <div
      className="example-game-component"
      style={{ width: "300px", border: "1px solid white", padding: "10px" }}
    >
      <h3>Game Link</h3>
      <>
        <Link to={"./games/${gameName}"}>
          <button onClick={goToGame}>
            {gameName}
            {/* direct to game page */}
          </button>
          <p>filler</p>
          <p>fillerfiller</p>
        </Link>
      </>
    </div>
  );
};

export default LinkToGame;
