import sqlite3

def ensureConnection(func):
	def inner(*args, **kwargs):
		with sqlite3.connect("database.db") as conn:
			kwargs["conn"] = conn
			res = func(*args, **kwargs)
		return res
	return inner

@ensureConnection
def initDB(conn, force: bool = False):
	c = conn.cursor()
	if force:
		c.execute("DROP TABLE IF EXISTS linkList")
	c.execute("""
		CREATE TABLE IF NOT EXISTS linkList (
            link                TEXT NOT NULL,
            length              TEXT NOT NULL,
            condition           TEXT NOT NULL
		)
	""")
	conn.commit()

@ensureConnection
def addLink(conn, link: str, length: int, condition: int):
	c = conn.cursor()
	c.execute("INSERT INTO linkList (link, length, condition) VALUES (?, ?, ?)", (link, length, condition))
	conn.commit()
@ensureConnection
def checkLink(conn, link: str):
	c = conn.cursor()
	c.execute("SELECT link FROM linkList WHERE link = ?", (link, ))
	result = c.fetchone()
	if result:
		return result[0]