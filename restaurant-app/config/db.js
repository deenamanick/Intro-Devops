// restaurant-app/config/db.js
const mysql = require('mysql2'); // Ensure you use 'mysql2'
const dotenv = require('dotenv');

dotenv.config();

const db = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  port: process.env.DB_PORT || 3306
});

// Connect to MySQL
db.connect(err => {
  if (err) {
    console.error("❌ Database connection failed:", err);
    process.exit(1);
  }
  console.log("✅ MySQL Connected...");
});

module.exports = db; // Ensure the module exports the connection

