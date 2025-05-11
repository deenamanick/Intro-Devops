from flask import Flask, request, jsonify
import psycopg2
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/api/items', methods=['GET', 'POST'])
def handle_items():
    if request.method == 'GET':
        # Retrieve all items
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM items;')
        items = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([{'id': item[0], 'name': item[1]} for item in items])
    
    elif request.method == 'POST':
        # Add new item
        data = request.get_json()
        name = data['name']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO items (name) VALUES (%s) RETURNING id;', (name,))
        item_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'id': item_id, 'name': name}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
