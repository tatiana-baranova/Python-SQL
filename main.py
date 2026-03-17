import sqlite3 as sql

# Створення файла з базою даних
conn = sql.connect('database.sqlite')
cur = conn.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS users(
    id int auto_increment primary key,
    name varchar(25),
    password varchar(50)
) ''')
conn.commit()

user_name = input('Enter your name: ')
user_password = input('Enter your password: ')

cur.execute('INSERT INTO users (name, password) VALUES (?, ?)', (user_name, user_password))
conn.commit()

print('List users:\n')
cur.execute('SELECT * FROM users')
users = cur.fetchall()
for user in users:
    print(f'Name: {user[1]} | Password: {user[2]}')

cur.close()
conn.close()