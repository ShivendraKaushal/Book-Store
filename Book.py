import sqlite3

class database :
    def connect(self):
        global conn 
        conn = sqlite3.connect("books.db")
        global cur 
        cur = conn.cursor()

    def com(self):
        conn.commit()

    def cl(self):
        conn.close()

    def __init__(self):
        self.connect()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.com()
        self.cl()

    def insert(self,title, author, year, isbn):
        self.connect()
        cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",(title, author, year, isbn))
        self.com()
        self.cl()

    def view(self):
        self.connect()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        self.cl()
        return rows

    def search(self, title = "", author = "", year = "", isbn = ""):
        self.connect()
        cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
        rows = cur.fetchall()
        self.cl()
        return rows

    def delete(self, id):
        self.connect()
        cur.execute("DELETE FROM book WHERE id = ?",(id,))
        self.com()
        self.cl()

    def upadte(self, id, title, author, year, isbn):
        self.connect()
        cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title, author, year, isbn, id))
        self.com()
        self.cl()


