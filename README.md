# Flask API with MySQL and Authentication

This project aims to create a RESTful API using Flask that can handle various types of requests (GET, POST, PUT, DELETE) for managing resources in a MySQL database. The API will also implement user authentication using JWT (JSON Web Tokens).

# Key Features
User Registration and Authentication: Here users can register by providing a username and password and user can log in to receive a JWT for authenticated requests.

# Operation:
Create: Add new items to the database.
Read: Retrieve existing items.
Update: Modify details of an existing item.
Delete: Remove an item from the database.

# Database Integration:
A MySQL database will be used to store user and item information.

# Technology
Flask: A micro web framework for Python.
Flask-MySQLdb: A Flask extension to interact with MySQL.
Flask-JWT-Extended: A Flask extension for managing JSON Web Tokens.
MySQL: The database system for data storage.

# Requirements:
Flask
MySQLdb
Flask-JWT_Extended
pip install flask
pip install flask-mysqldb
pip install flask-jwt-extended

# Users Table:

id: INT, primary key, auto-increment.
username: VARCHAR(50),not null.
password: VARCHAR(50), not null.

# Items Table:

id: INT, primary key, auto-increment.
name: VARCHAR(50), not null.
description: TEXT.

