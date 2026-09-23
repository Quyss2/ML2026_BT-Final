from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

try:
    mysql = MySQL()

    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '@Obama123'
    app.config['MYSQL_DATABASE_DB'] = 'studentmanagment'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'

    mysql.init_app(app)

    conn = mysql.connect()
    print("connection is successful!")

    cursor = conn.cursor()

    cursor.execute("select * from student")
    data = cursor.fetchall()

    print("ID\tCode\tName")
    for item in data:
        print(item[0], "\t", item[1], "\t", item[2])

except Exception as e:
    print("Error = ", e)

finally:
    conn.close()
    cursor.close()
    print("Mysql is closed")