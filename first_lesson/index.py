import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '33start3'
)

mycursor = mydb.cursor()
mycursor.execute('SHOW DATABASES')
for db in mycursor:
    print(db)