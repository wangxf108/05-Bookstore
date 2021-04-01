# Create a backend database by sqlite3. You should remember it.

import sqlite3

def connect():
    conn=sqlite3.connect("books.db")       #build a connect to the database
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")        
     #execute a SQL statement. 
     #And if there's no such data then build a new table to install the data
     #Also need some parameter to check the new data. (id, title, year, isbn )
    conn.commit()
    conn.close() 

def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")       #build a connect to the database
    cur=conn.cursor()
    # when click the insert button in the frontend, the system should execute thte new commit and connect with database.
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn)) 
    # (trick)'NULL'==python will create a ID directly.
    conn.commit()
    conn.close() 

def view():
    conn=sqlite3.connect("books.db")       #build a connect to the database
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")       # select all the things from the book
    rows=cur.fetchall()       #a rows function to return the tuple
    conn.close() 
    return rows
 
def search(title="", author="", year="", isbn=""):       # To pass some empty strings as default values. 
    # (="") Even thougt you input only one value of one parameter, the system will not be error.
    conn=sqlite3.connect("books.db")       #build a connect to the database
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))       
    # select all the books where title equals to something and others are the same.
    # (title, author, year, isbn) is the second parameter of the argument.
    rows=cur.fetchall()       #a row function to return the tuple
    conn.close() 
    return rows

def delete(id):  # delete the tuple of data by it's ID
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))            # Don't forget the comma
    conn.commit()
    conn.close() 

def update(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))  # 'id' is at the end of the tuple
    conn.commit()
    conn.close() 

connect()
#insert("The Sun","Andy Wang",1918,9131231132) 
#delete(7)
update(5, "The moon","John Smooth",1917,99999)
print(view())
print(search(author="John Smith"))