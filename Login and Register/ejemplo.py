#!/usr/bin/python3
import pymysql

# Parameters and connect
miConexion = pymysql.connect(host='localhost', user='AdminLS',
                             passwd='Admin', db='LiveScore')
cur = miConexion.cursor()

# Select
cur.execute("SELECT mail, passwd FROM users")
print("Resultados de tabla users:")
# After execute we can see the results using fetchall()
for mail, passwd in cur.fetchall():
    print("{} : {}".format(mail, passwd))

# Insert
cur.execute("insert into users values(113, 'Angely Ballesteros',\
     '2022-02-27', '113@mail.com', '113', 'Female');")
cur.execute("SELECT mail, passwd FROM users")
print("\nLuego de agregar\n")
for mail, passwd in cur.fetchall():
    print("{} : {}".format(mail, passwd))

# Update
cur.execute("update users set mail='ñaña@ñaña.com' where id=113;")
cur.execute("SELECT mail, passwd FROM users")
print("\nLuego de modificar\n")
for mail, passwd in cur.fetchall():
    print("{} : {}".format(mail, passwd))

# Delete
cur.execute("delete from users where id=113;")
print("\nLuego de eliminar\n")
cur.execute("SELECT mail, passwd FROM users")
for mail, passwd in cur.fetchall():
    print("{} : {}".format(mail, passwd))

# Apply and close
miConexion.commit()
miConexion.close()
