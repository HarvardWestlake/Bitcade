import React, { useState, useEffect } from "react";
import "./LeaderBoard.css";

const LeaderBoard = () => {
  const [users, setUsers] = useState([
    { username: "Alice", score: 85, photo: "https://via.placeholder.com/50" },
    { username: "Bob", score: 92, photo: "https://via.placeholder.com/50" },
    { username: "Charlie", score: 88, photo: "https://via.placeholder.com/50" },
    { username: "Dave", score: 75, photo: "https://via.placeholder.com/50" },
    { username: "Eve", score: 95, photo: "https://via.placeholder.com/50" },
  ]);

  useEffect(() => {
    // Sort users by score in descending order
    const sortedUsers = [...users].sort((a, b) => b.score - a.score);
    setUsers(sortedUsers);
  }, [users]);

  const topThree = users.slice(0, 3);
  const allUsers = users;

  return (
    <div className="leaderboard">
      <div className="top-three">
        <h2>Top 3 Users</h2>
        <ul id="top-three-list">
          {topThree.map((user, index) => (
            <li key={index}>
              <img
                src={user.photo}
                alt={`${user.username}'s avatar`}
                className="avatar"
              />
              {user.username}: {user.score}
            </li>
          ))}
        </ul>
      </div>
      <div className="extended-list">
        <h3>All Users</h3>
        <ul id="all-users-list">
          {allUsers.map((user, index) => (
            <li key={index}>
              {user.username}: {user.score}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default LeaderBoard;

// Coded by Chris Weng, Aidan Michaelson, and Ronan Valle
