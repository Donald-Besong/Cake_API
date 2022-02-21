import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

select_items_table_query ="SELECT * FROM cakes"
select_users_table_query ="SELECT * FROM users"

data = cursor.execute(select_items_table_query)
user_data = cursor.execute(select_users_table_query)
print(list(data))
#print(list(user_data))
connection.commit()

connection.close()
