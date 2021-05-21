import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '33start3',
    database='testdb123'
)

mycursor = mydb.cursor()

sqlformula = 'INSERT INTO users (login, password) VALUES (%s, %s)'
user1 = ('user1', '123')

mycursor.execute(sqlformula, user1)
mydb.commit()