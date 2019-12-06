import sqlite3


dbConnection = sqlite3.connect('BookLists.db')

def Mamad() :
    print('hello')

db = dbConnection.cursor()
#db.execute("CREATE TABLE members (id integer, name text, age integer)")

db.execute("SELECT * from members where name = 'ashkan'")

#db.execute("INSERT INTO members(id, name, age) VALUES(1, 'ashkan', 14)")




a = db.fetchall()
print(a)
dbConnection.commit()
#print(db)

