import React from "react";
import { WalletProvider } from "./components/WalletContext"; // Import the provider
import Header from "./Header";
import BattleShip from "./games/Battleship";

function GamePage() {
  return (
    <WalletProvider>
      <div className="App">
        {/* Wrap the entire application with WalletProvider */}
        <Header />
        <div
          style={{
            flex: 1,
            border: "1px solid white",
            padding: "10px",
          }}
        >
          <BattleShip bs></BattleShip>
        </div>
      </div>
    </WalletProvider>
  );
}

export default GamePage;
