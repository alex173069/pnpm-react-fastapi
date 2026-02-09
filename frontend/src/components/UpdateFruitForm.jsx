import React, { useState } from 'react';

const UpdateFruitForm = ({ updateFruit }) => {
  const [oldName, setOldName] = useState('');
  const [newName, setNewName] = useState('');
  const handleSubmit = (event) => {
    event.preventDefault();
    if (oldName && newName) {
      updateFruit(oldName, newName);
      setOldName('');
      setNewName('');
    }
  };
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={oldName}
        onChange={(e) => setOldName(e.target.value)}
        placeholder="Current fruit name"
      />
      <input
        type="text"
        value={newName}
        onChange={(e) => setNewName(e.target.value)}
        placeholder="New fruit name"
      />
      <button type="submit">Update Fruit</button>
    </form>
  );
}

export default UpdateFruitForm;