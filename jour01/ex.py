import mysql.connector

#connexion de base de données
db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="LaPlateforme"
)

mycursor = db.cursor ()

sql = "INSERT INTO customers (name, adress) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.executed(sql, val)

db.commit()

print(mycursor.rowcount, "record inserted.")