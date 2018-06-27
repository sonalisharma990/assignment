#Q1 and #Q2   '''tables are created as well as values are inserted'''
import sqlite3
conn=sqlite3.connect('book.db')
print("opened data base successfully")
conn.execute('''CREATE TABLE BOOK4(BOOK_ID INT PRIMARY KEY NOT NULL,TITLE_ID INT  NOT NULL,LOCATION CHAR(50),GENRE TEXT NOT NULL);''')
print("table created successfully")
conn.execute("INSERT INTO BOOK4(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(15,1,'Dragonwings bookstore','Action')")
conn.execute("INSERT INTO BOOK4(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(23,2,'Jaberwocky bookshop','Horror')")
conn.execute("INSERT INTO BOOK4(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(36,3,'Paragraphs bookstore','Romance')")
conn.commit()
print("table created successfully")

conn.execute('''CREATE TABLE TITLES(TITLE_ID INT PRIMARY KEY NOT NULL,TITLE CHAR(50) NOT NULL,ISBN INT NOT NULL,PUBLISHER_ID CHAR(50) NOT NULL,PUBLISHER_YEAR INT NOT NULL);''')
print("table created successfully")
conn.execute('''CREATE TABLE PUBLISHERS(PUBLISHER_ID INT PRIMARY KEY NOT NULL,NAME CHAR(50) NOT NULL,STREET_ADDRESS CHAR(50),SUITE_NUMBER INT NOT NULL,ZIP_CODE_ID INT NOT NULL);''')
print("table created successfully")
conn.execute('''CREATE TABLE ZIP_CODES(ZIP_CODE_ID INT PRIMARY KEY NOT NULL,CITY CHAR(50) NOT NULL,STATE CHAR(50),ZIP_CODE INT NOT NULL);''')
print("table created successfully")
conn.execute('''CREATE TABLE AUTHOR'S_TITLES(AUTHOR_TITLE_ID INT PRIMARY KEY NOT NULL,AUTHOR_ID INT NOT NULL,TITLE_ID INT NOT NULL);''')
print("table created successfully")
conn.execute('''CREATE TABLE AUTHORS(AUTHOR_ID INT PRIMARY KEY NOT NULL,FIRST_NAME CHAR(50) NOT NULL,MIDDLE_NAME CHAR(50),LAST_NAME NOT NULL);''')
print("table created successfully")


#Q3
import sqlite3
conn=sqlite3.connect('book.db')
print("before updation")
cursor = conn.execute("SELECT book_id,title_id,location,genre from book4")
for row in cursor:
    print("BOOK_ID=",row[0])
    print("TITLE_ID=",row[1])
    print("LOCATION=",row[2])
    print("GENRE=",row[3],"\n")
print("records created successfully")
print("after updation")
cursor=conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE from BOOK4")
conn.execute("UPDATE BOOK4 set TITLE_ID=TITLE_ID+2 where BOOK_ID=23")
conn.commit()
for row in cursor:
    print("BOOK_ID=",row[0])
    print("TITLE_ID=",row[1])
    print("LOCATION=",row[2])
    print("GENRE=",row[3],"\n")
print("updated successfully")


