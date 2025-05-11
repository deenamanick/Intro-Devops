// restaurant-app/routes/restaurantRoutes.js
const express = require('express');
const router = express.Router();
const db = require('../config/db');

// Get all restaurants
router.get('/', (req, res) => {
  db.query('SELECT * FROM restaurants', (err, results) => {
    if (err) {
      console.error("❌ Error fetching restaurants:", err);
      return res.status(500).json({ error: "Database query failed" });
    }
    res.json(results);
  });
});

// Add a new restaurant
router.post('/', (req, res) => {
  const { name, location, cuisine } = req.body;
  
  if (!name || !location || !cuisine) {
    return res.status(400).json({ error: "All fields are required" });
  }

  db.query('INSERT INTO restaurants (name, location, cuisine) VALUES (?, ?, ?)',
    [name, location, cuisine],
    (err, result) => {
      if (err) {
        console.error("❌ Error inserting restaurant:", err);
        return res.status(500).json({ error: "Database insert failed" });
      }
      res.status(201).json({ id: result.insertId, name, location, cuisine });
    }
  );
});

module.exports = router;
