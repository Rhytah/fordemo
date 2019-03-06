
import os, psycopg2, csv


DATABASE_URL = os.environ['DATABASE_URL']
']
conn = psycopg2.connect(host="ec2-54-204-2-25.compute-1.amazonaws.com",database="de4ddh75282quq", user="qveeiishhqryyg"
, password="609b9db3f2b326518943a8ce73b4fa0cc1ee1091bd6d47c4e18c1758853e4f7a")




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