from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sreyaammu123'
app.config['MYSQL_DB'] = 'databasesreya'
mysql = MySQL(app)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret'  

jwt = JWTManager(app)

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({"msg": "User registered successfully!"}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    
    if user:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

# CRUD operations for items

# GET all items
@app.route('/items', methods=['GET'])
@jwt_required()
def get_items():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    cursor.close()
    
    return jsonify(items), 200

# GET a specific item
@app.route('/items/<int:item_id>', methods=['GET'])
@jwt_required()
def get_item(item_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    cursor.close()
    
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    return jsonify(item), 200

# POST a new item
@app.route('/items', methods=['POST'])
@jwt_required()
def create_item():
    new_item = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (new_item['name'], new_item['description']))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({"msg": "Item created"}), 201

# PUT to update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    updated_data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE items SET name = %s, description = %s WHERE id = %s", 
                   (updated_data['name'], updated_data['description'], item_id))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({"msg": "Item updated"}), 200

# DELETE an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({"msg": "Item deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
