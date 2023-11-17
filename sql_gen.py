import sqlite3
from faker import Faker

# Create a Faker object
fake = Faker()

# Create a connection to the database
conn = sqlite3.connect('./db/your_database.db')
cursor = conn.cursor()

# Create table users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
''')

# Create table products
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT
    )
''')

# Create table sales
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product_id INTEGER,
        date DATE
    )
''')

# Generate users
for _ in range(100):
    name = fake.name()
    email = fake.email()

    cursor.execute('''
        INSERT INTO users (name, email)
        VALUES (?, ?)
    ''', (name, email))

# Generate products
for _ in range(20):
    product_name = fake.word()

    cursor.execute('''
        INSERT INTO products (product_name)
        VALUES (?)
    ''', (product_name,))

# Generate sales
for _ in range(1000):
    user_id = fake.random_int(min=1, max=100)
    product_id = fake.random_int(min=1, max=20)
    sale_date = fake.date_between(start_date='-1y', end_date='today')  # Generate a date within the past year

    cursor.execute('''
        INSERT INTO sales (user_id, product_id, date)
        VALUES (?, ?, ?)
    ''', (user_id, product_id, sale_date))

# Save changes and close the connection
conn.commit()
conn.close()