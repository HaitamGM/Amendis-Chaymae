import psycopg2
from flask_bcrypt import Bcrypt

# Connexion à PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1975"
)
cursor = conn.cursor()
bcrypt = Bcrypt()

# 1. استرجاع كل المستخدمين وكلمات السر العادية
cursor.execute("SELECT id_utilisateur, mot_de_passe FROM utilisateurs")
utilisateurs = cursor.fetchall()

# 2. تشفير وتحديث كل password
for user_id, plain_pwd in utilisateurs:
    hashed_pwd = bcrypt.generate_password_hash(plain_pwd).decode('utf-8')
    cursor.execute(
        "UPDATE utilisateurs SET mot_de_passe = %s WHERE id_utilisateur = %s",
        (hashed_pwd, user_id)
    )

# 3. حفظ التغييرات
conn.commit()
cursor.close()
conn.close()

print("✅ تم تشفير جميع كلمات السر بنجاح.")
