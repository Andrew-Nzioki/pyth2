import sqlite3 #import sqlite3
conn = sqlite3.connect("customer.db") #create a connection || in this sqlite3 creates the databse customer in this directore

# con=sqlite3.connect(":memory:")#in this the database created is destroyed when the program stops or is terminated
cur = conn.cursor()

#create a table

cur.execute()