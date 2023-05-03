import mysql.connector

#connexion de base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Etoile19*",
  database="LaPlateforme"
)

# Récupération des données de la table "salles"
mycursor = db.cursor()
mycursor.execute("SELECT nom, capacite FROM salles")
result = mycursor.fetchall()

# Affichage des données récupérées
for x in result:
  print(x)