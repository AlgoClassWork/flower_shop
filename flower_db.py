import sqlite3

def create_database():
    connection = sqlite3.connect('flowers.db')
    cursor = connection.cursor()
    cursor.execute(     '''
    CREATE TABLE IF NOT EXISTS flowers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL,
    quantity INTEGER,
    image_path TEXT)    ''')
    connection.commit()
    connection.close()

def add_flower(name, description, price, quantity , image_path):
    connection = sqlite3.connect('flowers.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO flowers (name, description, price, quantity, image_path)
    VALUES (?, ?, ?, ?, ?)''', (name, description, price, quantity, image_path))
    connection.commit()
    connection.close()

def update_flower(name, description, price, quantity , image_path, id):
    connection = sqlite3.connect('flowers.db')
    cursor = connection.cursor()
    cursor.execute('''
    UPDATE flowers SET name=?, description=?, price=?, quantity=?, image_path=?
    WHERE id=?''', (name, description, price, quantity, image_path, id))
    connection.commit()
    connection.close()

def delete_flower(id):
    connection = sqlite3.connect('flowers.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM flowers WHERE id=?', (id))
    connection.commit()
    connection.close()

def get_all_flowers():
    connection = sqlite3.connect('flowers.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM flowers')
    flowers = cursor.fetchall()
    connection.close()
    return flowers

def get_flower(id):
    connection = sqlite3.connect('flowers.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM flowers WHERE id=?', (id))
    flower = cursor.fetchall()
    connection.close()
    return flower

create_database()

