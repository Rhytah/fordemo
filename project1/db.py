
import os, psycopg2, csv


DATABASE_URL = os.environ.get('DATABASE_URL')

conn = psycopg2.connect(host="ec2-54-204-41-109.compute-1.amazonaws.com",database="dchga802mgmbih", user="ksuitsnkksjdlx"
, password="468f5659deec7f5393c221f188c39f56d022aede152f990ad34c27a1bce99585")




csvfile = open("books.csv") 
reader = csv.reader(csvfile,delimiter=',')
print("Creating books table!")

cur = conn.cursor()

cur.execute("CREATE TABLE books ( id SERIAL PRIMARY KEY, \
								   isbn VARCHAR NOT NULL, \
								   title VARCHAR NOT NULL, \
								   author VARCHAR NOT NULL, \
								   year VARCHAR NOT NULL );")

print("Created!")

print("Adding values to table.")

for isbn, title, author, year in reader:
	cur.execute("INSERT INTO books (isbn, title, author, year) VALUES (%s, %s, %s, %s)",(isbn,title,author,year))

conn.commit()
print("Insert Completed!")


cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, password VARCHAR NOT NULL, create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
conn.commit()
print("user table created successfully")


cur.execute("CREATE TABLE reviews (id SERIAL PRIMARY KEY, review VARCHAR NOT NULL,book_id INTEGER NOT NULL,user_id INTEGER REFERENCES users);")
conn.commit()
print("Reviews table created successfully!")