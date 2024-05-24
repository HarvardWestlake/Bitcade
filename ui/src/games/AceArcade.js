import React, { useState, useEffect } from "react";
import "./AceArcade.css";

const App = () => {
  let dhand = "K, 3, 4";
  let phand = "Q, 5, 8";
  return (
    <div className="container">
      <h1>Ace Arcade - Blackjack</h1>
      <div id="game">
        <h3>Dealer:</h3>
        <p>{dhand}</p>
        <h3>Player:</h3>
        <p>{phand}</p>
        <div id="actions">
          <div id="deal">
            <button id="bdeal">Deal</button>
          </div>
          <div id="hit">
            <button id="bhit">Hit</button>
          </div>
          <div id="stand">
            <button id="bstand">Stand</button>
          </div>
          {/* <button onClick={deal}>Deal</button>
          <button onClick={hit}>Hit</button>
          <button onClick={stand}>Stand</button> */}
        </div>
      </div>
    </div>
  );
};

export default App;
