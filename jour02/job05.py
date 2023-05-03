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
mycursor.execute("SELECT SUM(superficie) AS superficie_totale FROM etage")
result = mycursor.fetchone()[0]

# Affichage des données récupérées
print("La superficie de La Plateforme est de", result, "m2")