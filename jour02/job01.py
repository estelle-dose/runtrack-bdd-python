import mysql.connector

#connexion de base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="LaPlateforme"
)

mycursor = db.cursor()
mycursor.execute("SELECT * FROM etudiants")
etudiants = mycursor.fetchall()

for etudiant in etudiants:
  print(etudiant)