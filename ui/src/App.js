import React from 'react';
import './App.css';
import Header from './Header'; // make sure to import your Header component
import { WalletProvider } from './components/WalletContext'; // Import the provider
import ExampleGameComponent from './games/ExampleGameComponent'; // Import the game component
import RockPaperScissors from './games/RockPaperScissors';
import AceArcade from './games/AceArcade';

// Update the contract address here
const exampleContractAddress = "0x51C72848c68a965f66FA7a88855F9f7784502a7F";
const testingRPCAdress = "0x65DfcD089DC1135F687dA33a05C66Ec6B78C802F"

function App() {
  return (
    <WalletProvider> {/* Wrap the entire application with WalletProvider */}
      <div className="App">
        <Header />
        <div className="content">
          <div className="side-panel" style={{ flex: '15%' }}></div>
          <div className="main-panel" style={{ flex: '70%' }}>
            {/* Main content goes here */}
            {/* <ExampleGameComponent contractAddress={exampleContractAddress} /> */}
            <RockPaperScissors contractAddress={testingRPCAdress}/>
            <AceArcade contractAddress={testingRPCAdress} />
          </div>
          <div className="side-panel" style={{ flex: '15%' }}></div>
        </div>
      </div>
    </WalletProvider>
  );
}

export default App;
