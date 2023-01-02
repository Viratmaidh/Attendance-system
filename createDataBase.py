import sqlite3
# import playsound

conn = sqlite3.connect('database.db')
c = conn.cursor()

sql = """
DROP TABLE IF EXISTS users1;
CREATE TABLE users1 (
           id integer unique primary key autoincrement,
           name text
);
"""
c.executescript(sql)

print("User Table created successfully in database")

# playsound.playsound('sound.mp3')

conn.commit()
conn.close()