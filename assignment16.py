#Q1 and #Q2   '''tables are created as well as values are inserted'''
import sqlite3
conn=sqlite3.connect('book.db')
print("opened data base successfully")
conn.execute('''CREATE TABLE BOOK3(BOOK_ID INT PRIMARY KEY NOT NULL,TITLE_ID INT  NOT NULL,LOCATION CHAR(50),GENRE TEXT NOT NULL);''')
print("table created successfully")
conn.execute("INSERT INTO BOOK3(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(15,1,'Dragonwings bookstore','Action')")
conn.execute("INSERT INTO BOOK3(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(23,2,'Jaberwocky bookshop','Horror')")
conn.execute("INSERT INTO BOOK3(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(36,3,'Paragraphs bookstore','Romance')")
conn.commit()
print("insert successfully")
cursor=conn.execute("SELECT book_id,title_id,location,genre from BOOK3")

for row in cursor:
    print("BOOK_ID=",row[0])
    print("TITLE_ID=",row[1])
    print("LOCATION=",row[2])
    print("GENRE=",row[3],"\n")
print("records created successfully")


conn.execute('''CREATE TABLE TITLES(TITLE_ID INT PRIMARY KEY NOT NULL,TITLE CHAR(50) NOT NULL,ISBN INT NOT NULL,PUBLISHER_ID CHAR(50) NOT NULL,PUBLISHER_YEAR INT NOT NULL);''')#print("table created successfully")
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
print("opened data base successfully")
conn.execute('''CREATE TABLE TITLES(TITLE_ID INT PRIMARY KEY NOT NULL,TITLE CHAR(50) NOT NULL,ISBN INT NOT NULL,PUBLISHER_ID CHAR(50) NOT NULL,PUBLISHER_YEAR INT NOT NULL);''')
print("table created successfully")
conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLISHER_YEAR)VALUES(1,'Ram',246378,'sona@gmail.com',2004)")
conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLISHER_YEAR)VALUES(2,'Seeta',678393,'gouri@gmail.com',2005)")
conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLISHER_YEAR)VALUES(3,'Shyam',579029,'anu@gmail.com',2006)")
conn.commit()
print("insert successfully")
cursor = conn.execute("SELECT title_id,title,isbn,publisher_id,publisher_year from TITLES")

for row in cursor:
    print("TITLE_ID=",row[0])
    print("TITLE=",row[1])
    print("ISBN=",row[2])
    print("PUBLISHER_ID=",row[3])
    print("PUBLISHER_YEAR=",row[4],"\n")
print("records created successfully")
conn.execute("UPDATE TITLES set PUBLISHER_YEAR=2007 where TITLE_ID=3")
conn.commit()
