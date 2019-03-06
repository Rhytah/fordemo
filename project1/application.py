import os

from flask import Flask, session,jsonify,render_template,json
import requests 
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from db_connect.server import DatabaseConnect

db=DatabaseConnect()


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.config["SECRET_KEY"]= os.environ.get('SECRET_KEY')
app.config["API_KEY"] = os.environ.get('API_KEY')
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/books")
def show_books():
    cmd="SELECT * FROM books ORDER BY isbn OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY"
    
    result=db.execute(cmd)
    if result:
        return render_template('books.html', books= result)
    return jsonify({"message":"Resource not found"})

@app.route("/books/<isbn>")
def show_specific_books(isbn):
    cmd=f"SELECT * FROM books WHERE isbn ='{isbn}' "
    
    result=db.execute(cmd)
    if result:
        return render_template('books.html', books= result)
    return jsonify({"message":"Resource not found"})
    # res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key":"vF7Z3t3lTDbuqMCOAuI0ZQ", "isbns": f"{isbn}"})
    # return jsonify({"book": res.json()})
    
    

if __name__ == '__main__':
    app.run(debug=True, port =5000)
    # db = DatabaseConnect()