import React from 'react';
import './App.css';
import Header from './Header'; // make sure to import your Header component

function App() {
  return (
    <div className="App">
      <Header />
      <div className="content">
        <div className="side-panel" style={{ flex: '15%' }}></div>
        <div className="main-panel" style={{ flex: '70%' }}>
          {/* Main content goes here */}
        </div>
        <div className="side-panel" style={{ flex: '15%' }}></div>
      </div>
    </div>
  );
}

export default App;
