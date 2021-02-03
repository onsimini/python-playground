import os
import sqlite3

# storage definition
DATABASE = r'./database.db'

if os.path.isfile(DATABASE):
    # connect to db
    conn = sqlite3.connect(DATABASE)
else:
    # create & connect to db
    conn = sqlite3.connect(DATABASE)
    # Empty table creation
    conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')

list = [
    ('gontran sion',    '123 rue nationale',    'montreal',      100),
    ('kelly gonzalez',  '456 rue secondaire',   'quebec',        200),
    ('Marlon bucher',   '789 rue tertiaire',    'troisriviaire', 300),
    ('truc much',       '10 rue du bout',       'paris',         400)
]

conn.execute("INSERT INTO students VALUES ('bill oute', '22 vla les', 'flics', 999)")
conn.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", list)
conn.commit()

for row in conn.execute('SELECT * FROM students'):
    print(row)

for row in conn.execute('SELECT * FROM students WHERE name = "kelly gonzalez"'):
    print(row)

# close db connection
conn.close()

#delete the database
os.remove(DATABASE)
