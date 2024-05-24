import React from 'react';
import './App.css';
import Header from './Header'; // make sure to import your Header component
import { WalletProvider } from './components/WalletContext'; // Import the provider
import ExampleGameComponent from './games/ExampleGameComponent'; // Import the game component

// Update the contract address here
const exampleContractAddress = "0x51C72848c68a965f66FA7a88855F9f7784502a7F";
// Update the IPFS CID here
const exampleIpfsHash = "QmaXsAPN3xfjbism2UGRetGMnphF6d8dQcQy3m51f36NBL";
const ExampleGameComponentName = "Example Game";

const wyrmsContractAddress = "0x51C72848c68a965f66FA7a88855F9f7784502a7F";
const wyrmsIpfsHash = "QmWRnVAMTeAUq7dmtFTL6zS8nnnbT5gNd8FsHc2Aqxybxc";
const wyrmsGameComponentName = "Wyrms";

function App() {
  return (
    <WalletProvider> {/* Wrap the entire application with WalletProvider */}
      <div className="App">
        <Header />
        <div className="content">
          <div className="side-panel" style={{ flex: '15%' }}></div>
          <div className="main-panel" style={{ flex: '70%' }}>
            {/* Main content goes here */}
            <ExampleGameComponent contractAddress={exampleContractAddress} ipfsHash={exampleIpfsHash} componentName={ExampleGameComponentName} />
            <ExampleGameComponent contractAddress={wyrmsContractAddress} ipfsHash={wyrmsIpfsHash} componentName={wyrmsGameComponentName}/>
          </div>
          <div className="side-panel" style={{ flex: '15%' }}></div>
        </div>
      </div>

   
      
    </WalletProvider>
  );
}

export default App;
