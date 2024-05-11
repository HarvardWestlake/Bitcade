import React, { useState } from 'react';

function PlayButton() {
  const [isActive, setIsActive] = useState(false);

  const handleClick = () => {
    setIsActive(true);
    alert('Play button activated!');
  };

  return (
    <button onClick={handleClick} style={{ fontSize: '20px', padding: '10px 20px' }}>
      {isActive ? 'Playing' : 'Play'}
    </button>
  );
}

export default PlayButton;
