import React from "react";

// import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom"; // Ensure Link is imported

import "./App.css";
import Header from "./Header"; // make sure to import your Header component
import { WalletProvider } from "./components/WalletContext"; // Import the provider
import ExampleGameComponent from "./games/ExampleGameComponent"; // Import the game component
import LinkToGame from "./LinkToGame.js";
import HomeScreen from "./HomeScreen.js";
import GamePage from "./GamePage.js";

import {
  BrowserRouter as Router,
  Routes,
  Route,
  useParams,
} from "react-router-dom";

import BattleshipGameComponent from "./games/Battleship.js";

const Battleship = "Battleship";

function App() {
  return (
    <WalletProvider>
      <Router>
        <Routes>
          <Route path="/" element={<HomeScreen />} />
          <Route path="/GamePage" element={<GamePage />} />
        </Routes>
      </Router>
    </WalletProvider>
  );
}

export default App;
