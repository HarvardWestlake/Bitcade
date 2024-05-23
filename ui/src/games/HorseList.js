import React, { useState } from 'react';

const HorseList = ({ racers, onAddHorse }) => {
  const [newHorseName, setNewHorseName] = useState('');

  const handleNewHorseNameChange = (event) => {
    setNewHorseName(event.target.value);
  };

  const handleAddHorse = () => {
    if (newHorseName.trim() !== '') {
      onAddHorse(newHorseName.trim());
      setNewHorseName('');
    }
  };

  return (
    <div>
      <h4>Horses:</h4>
      <ul>
        {racers.map((racer, index) => (
          <li key={index}>{racer}</li>
        ))}
      </ul>
      <input
        type='text'
        value={newHorseName}
        onChange={handleNewHorseNameChange}
        placeholder='Enter new horse name'
      />
      <button onClick={handleAddHorse}>Add Horse</button>
    </div>
  );
};

export default HorseList;
