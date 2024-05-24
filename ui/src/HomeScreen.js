import React from "react";

// import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom"; // Ensure Link is imported

import "./App.css";
import Header from "./Header"; // make sure to import your Header component
import { WalletProvider } from "./components/WalletContext"; // Import the provider
import ExampleGameComponent from "./games/ExampleGameComponent"; // Import the game component
import LinkToGame from "./LinkToGame.js";

import {
  BrowserRouter as Router,
  Routes,
  Route,
  useParams,
} from "react-router-dom";

import BattleshipGameComponent from "./games/Battleship.js";

// Update the contract address here
const exampleContractAddress = "0x51C72848c68a965f66FA7a88855F9f7784502a7F";

const GameName = "GameName";

function HomeScreen() {
  return (
    <WalletProvider>
      {" "}
      {/* Wrap the entire application with WalletProvider */}
      <div className="App">
        <Header />
        <div className="content">
          <div className="side-panel" style={{ flex: "15%" }}></div>

          <div className="side-panel" style={{ flex: "15%" }}>
            <p>side bar</p>
          </div>
          {/* button to go to new page */}
          <div className="main-panel" style={{ flex: "70%" }}>
            {/* Main content goes here */}
            <LinkToGame gameName={GameName} />
          </div>
        </div>
      </div>
    </WalletProvider>
  );
}

export default HomeScreen;
