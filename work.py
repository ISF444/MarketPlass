import sqlite3

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()

sql = '''
CREATE TABLE customers (
Id SERIAL PRIMARY KEY,
FirstName CHARACTER VARYING(30),
LastName CHARACTER VARYING(30),
Email CHARACTER VARYING(30),
Age INTEGER);
'''

sql1 = '''
DROP table customers
'''

sql3 = '''
INSERT INTO customers (Id, FirstName, LastName, Email, Age)
VALUES (1, 'Alex', 'pypkun', 'name@py', 12);'''
data = cursor.execute(sql3)
connect.commit()
print(data.fetchall())
