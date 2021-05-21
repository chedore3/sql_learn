import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '33start3',
    database='testdb123'
)

mycursor = mydb.cursor()
mycursor.execute('SHOW TABLES')
for tb in mycursor:
    print(tb)