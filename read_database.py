import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

select_items_table_query ="SELECT * FROM cakes"


data = cursor.execute(select_items_table_query)

print(list(data))

connection.commit()

connection.close()
