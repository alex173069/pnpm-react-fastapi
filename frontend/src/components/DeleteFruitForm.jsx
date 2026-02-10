import React, { useState } from 'react';

const DeleteFruitForm = ({ removeFruit }) => {
  const [fruitName, setFruitName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (fruitName) {
      removeFruit(fruitName);
      setFruitName('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={fruitName}
        onChange={(e) => setFruitName(e.target.value)}
        placeholder="Enter fruit name to delete"
      />
      <button type="submit">Delete Fruit</button>
    </form>
  );
};

export default DeleteFruitForm;