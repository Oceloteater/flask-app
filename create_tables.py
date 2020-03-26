import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS dogs (id INTEGER PRIMARY KEY, name text, breed text, age numeric)'
cursor.execute(create_table)

connection.commit()
connection.close()
