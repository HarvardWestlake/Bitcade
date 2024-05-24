import React, { useState, useEffect } from "react";

import {
  BrowserRouter as Router,
  Routes,
  Route,
  useParams,
} from "react-router-dom";

import { useNavigate } from "react-router-dom";

const BattleShip = () => {
  return (
    <div
      className="example-game-component"
      style={{ border: "1px solid white", padding: "10px" }}
    >
      <h3>Battleship</h3>
      <>{"game goes here"}</>
    </div>
  );
};

export default BattleShip;
