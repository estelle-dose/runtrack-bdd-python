import mysql.connector

#connexion de base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="LaPlateforme"
)

# Récupération des données de la table "salles"
mycursor = db.cursor()
mycursor.execute("SELECT SUM(capacite) FROM salles")
result = mycursor.fetchone()[0]

# Affichage des données récupérées
print("La capacité de toutes les salles est de :", result)