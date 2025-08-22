import mysql.connector

try:
    conn = mysql.connector.connect(
        host="mysql-image-latest.onrender.com",
        port=3306,
        user="mia",
        password="1234",
        database="ma_base"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT NOW()")
    result = cursor.fetchall()
    print("Connexion réussie ! Date actuelle :", result)

except mysql.connector.Error as err:
    print("Erreur lors de la connexion :", err)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
