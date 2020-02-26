import sqlite3
try:
	db = sqlite3.connect(':memory:')

	cursor = db.cursor()

	fh = open('db.sql', 'r')
	script = fh.read()
	cursor.executescript(script)
	cursor.executescript("INSERT INTO article VALUES(1, 'test', 'pu', 'Jean', '2020-02-20', 'ceci est un test')")
	cursor.execute("SELECT * from article;")
	print(cursor.fetchall())
	print("Executed")

except Exception as e:
	db.rollback()
	raise e

finally:
	db.close()