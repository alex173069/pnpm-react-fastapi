import React, { useEffect, useState } from 'react';
import AddFruitForm from './AddFruitForm';
import UpdateFruitForm from './UpdateFruitForm';
import DeleteFruitForm from './DeleteFruitForm';
import api from '../api';

const FruitList = () => {
  const [fruits, setFruits] = useState([]);

  const fetchFruits = async () => {
    try {
      const response = await api.get('/fruits');
      setFruits(response.data.fruits);
    } catch (error) {
      console.error("Error fetching fruits", error);
    }
  };

  const addFruit = async (fruitName) => {
    try {
      await api.post('/fruits', { name: fruitName });
      fetchFruits();  // Refresh the list after adding a fruit
    } catch (error) {
      console.error("Error adding fruit", error);
    }
  };

  const updateFruit = async (oldName, newName) => {
  try {
    // 1st arg: URL
    // 2nd arg: Data/Body (null because we are using query params)
    // 3rd arg: Config object (where 'params' goes)
    await api.put('/fruits', null, {
      params: {
        old_name: oldName,
        new_name: newName
      }
    });
    fetchFruits(); 
  } catch (error) {
    console.error("Error updating fruit", error.response?.data || error.message);
  }
};

  const removeFruit = async (fruitName) => {
  try {
    // We use the 'params' key so Axios attaches this to the URL: /fruits?fruit_name=Apple
    await api.delete('/fruits', { 
      params: { fruit_name: fruitName } 
    });
    fetchFruits(); 
  } catch (error) {
    console.error("Error removing fruit", error);
  }
};

  useEffect(() => {
    fetchFruits();
  }, []);

  return (
    <div>
      <h2>Fruits List</h2>
      <ul>
        <UpdateFruitForm updateFruit={updateFruit} />
        {fruits.map((fruit, index) => (
          <li key={index}>{fruit.name}</li>
        ))}
      </ul>
      <DeleteFruitForm removeFruit={removeFruit} />
      <AddFruitForm addFruit={addFruit} />
    </div>
  );
};

export default FruitList;