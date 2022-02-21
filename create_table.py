import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_users_table_query ="CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
create_cakes_table_query ="CREATE TABLE IF NOT EXISTS cakes (id INTEGER PRIMARY KEY, name text, comment text, price real, imgUrl text, yum_factor real)"

cursor.execute(create_users_table_query)
cursor.execute(create_cakes_table_query)

connection.commit()

connection.close()
