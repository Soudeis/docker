import mysql.connector

# Connexion directe à la base MySQL
conn = mysql.connector.connect(
    host="mysql-image-latest.onrender.com",
    port=3306,
    user="mia",
    password="1234",
    database="ma_base"
)

# Tester la connexion
cursor = conn.cursor()
cursor.execute("SELECT NOW()")  # récupère la date et l'heure actuelle
result = cursor.fetchall()
print("Connexion OK, date actuelle :", result)

# Fermer la connexion
cursor.close()
conn.close()
