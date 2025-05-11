// restaurant-app/server.js

const express = require('express');
const dotenv = require('dotenv');
const restaurantRoutes = require('./routes/restaurantRoutes');
const db = require('./config/db');

dotenv.config();
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use('/restaurants', restaurantRoutes);

// Serve static frontend files
app.use(express.static('public'));


app.listen(port, '0.0.0.0', () => {
    console.log(`✅ Server running on http://localhost:${port}`);
  });
  


