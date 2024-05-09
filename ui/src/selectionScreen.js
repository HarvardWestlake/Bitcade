/***
 * create a dark (black) background
 * text will be neon maybe yellow or multicolored
 * should have big title "WYRM" on the top 
 * below, there will be all the games (with photo and name) and their description underneath
 */

import React from 'react';
import './App.css';

// Neon text styling
const neonTextStyles = {
  color: '#fff',
  fontSize: '3rem',
  textShadow: '0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #0ff, 0 0 70px #0ff, 0 0 80px #0ff, 0 0 100px #0ff, 0 0 150px #0ff',
  animation: 'flicker 1.5s infinite alternate'
};

// CSS keyframes for flicker animation
const flickerKeyframes = `
  @keyframes flicker {
    0% {
        opacity: 0.2;
    }
    100% {
        opacity: 1;
    }
  }
`;

// Inline CSS for the black background
const blackBackgroundStyles = {
  backgroundColor: 'black',
  height: '100vh',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center'
};

// App component
function selectionScreen() {
  /*return (
    <div style={blackBackgroundStyles}>
      <style>{flickerKeyframes}</style>
      <h1 style={neonTextStyles}>WYRM</h1>
    </div>
  );*/
  return (
    <WalletProvider> {/* Wrap the entire application with WalletProvider */}
      <div className="selectionScreen">
        <Header />
        <div className="content">
        <head>
          <title>WYRM</title>
        </head>
          <div className="side-panel" style={{ flex: '15%' }}></div>
          <div className="main-panel" style={{ flex: '70%' }}>
            {
              <div style={blackBackgroundStyles}>
                <style>{flickerKeyframes}</style>
                <h1 style={neonTextStyles}>WYRM</h1>
              </div>
            }
            <ExampleGameComponent contractAddress={exampleContractAddress} />
          </div>
          <div className="side-panel" style={{ flex: '15%' }}></div>
        </div>
      </div>
    </WalletProvider>
  );
}

export default SelectionScreen;
