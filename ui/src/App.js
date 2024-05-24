import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "./App.css";
import Header from "./Header";
import { WalletProvider } from "./components/WalletContext";
import ExampleGameComponent from "./games/ExampleGameComponent";
import CreatorsPage from "./creators";

// Update the contract address here
const exampleContractAddress = "0x51C72848c68a965f66FA7a88855F9f7784502a7F";

function App() {
  return (
    <WalletProvider>
      <Router>
        <div className="App">
          <Header />
          <div className="content">
            <div className="side-panel" style={{ flex: "15%" }}></div>
            <div className="main-panel" style={{ flex: "70%" }}>
              <Routes>
                <Route
                  path="/"
                  element={
                    <div className="game-grids">
                      <ExampleGameComponent
                        contractAddress={exampleContractAddress}
                      />
                      <ExampleGameComponent
                        contractAddress={exampleContractAddress}
                      />
                      <ExampleGameComponent
                        contractAddress={exampleContractAddress}
                      />
                    </div>
                  }
                />
                <Route path="/creators" element={<CreatorsPage />} />
              </Routes>
            </div>
            <div className="side-panel" style={{ flex: "15%" }}></div>
          </div>
          <footer className="footer">
            <li>
              <a href="/creators">
                Blocade is a HW Topics Project. See our developers
              </a>
            </li>
          </footer>
        </div>
      </Router>
    </WalletProvider>
  );
}

export default App;
