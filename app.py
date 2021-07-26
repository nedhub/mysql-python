
import mysql.connector



db = mysql.connector.connect(

    host = "localhost",
    user = "root",
    passwd = "password1234",
    database = "pythonsql"
)


# print(db)

cursor = db.cursor()

#cursor.execute("CREATE DATABASE IF NOT EXISTS pythonsql")


     # ^
     # | run this first
      #|
     # |
      #|

cursor.execute("CREATE TABLE IF NOT EXISTS student (id INT PRIMARY KEY, name VARCHAR(64))")
cursor.execute("CREATE TABLE IF NOT EXISTS course (id INT PRIMARY KEY, name VARCHAR(64))")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS owns (
#     person INT,
#     thing INT,
#     FOREIGN KEY (student) REFERENCES person(id),
#     FOREIGN KEY (course) REFERENCES thing(id)
# );


# """
# )


cursor.execute("SHOW TABLES")


for table in cursor:
    print(table)