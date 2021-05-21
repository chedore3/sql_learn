import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '33start3',
    database='testdb123'
)

mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE users (login VARCHAR(255), password INTEGER(10))')