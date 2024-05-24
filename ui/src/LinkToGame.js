import React, { useState, useEffect } from "react";

import {
  BrowserRouter as Router,
  Routes,
  Route,
  useParams,
} from "react-router-dom";

import { useNavigate } from "react-router-dom";

const LinkToGame = ({ gameName }) => {
  const navigate = useNavigate();

  const goToGame = async () => {
    navigate("/GamePage");
  };

  return (
    <div
      className="example-game-component"
      style={{ width: "300px", border: "1px solid white", padding: "10px" }}
    >
      <h3>Game Link</h3>
      <>
        <button onClick={goToGame}>
          {gameName}
          {/* direct to game page */}
        </button>
        <p>filler</p>
        <p>fillerfiller</p>
      </>
    </div>
  );
};

export default LinkToGame;
