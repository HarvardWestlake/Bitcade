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
<<<<<<< Updated upstream
        <div className="App">
          <Header />
          <div className="content">
            <div className="side-panel" style={{ flex: "15%" }}></div>
            <div className="main-panel" style={{ flex: "70%" }}>
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
            </div>
            <div className="side-panel" style={{ flex: "15%" }}></div>
=======
      {" "}
      {/* Wrap the entire application with WalletProvider */}
      <head>
        
      </head>
      <div className="App">
        <Header />
        <div className="content">
          <div className="side-panel" style={{ flex: "15%" }}></div>
          <div className="main-panel" style={{ flex: "70%" }}>
            {/* Main content goes here */}
            <div className="game-grid">
              <ExampleGameComponent contractAddress={exampleContractAddress} />
              <ExampleGameComponent contractAddress={exampleContractAddress} />
              <ExampleGameComponent contractAddress={exampleContractAddress} />
              {/* Add more ExampleGameComponent as needed */}
            </div>
>>>>>>> Stashed changes
          </div>
          <footer className="footer">
            <li>
              <a href="/creators">
                Blocade is a HW Topics Project. See our developers
              </a>
            </li>
          </footer>
        </div>
    </WalletProvider>
  );
}

export default App;
