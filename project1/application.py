import os


from flask import Flask, render_template, url_for, redirect,session,jsonify,json
from form import RegistrationForm, LoginForm 
from bcrypt import Bcrypt
import requests
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from db_connect.server import DatabaseConnect


app = Flask(__name__)



# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"]=('066459a30b9c2d387ba0')
app.config["API_KEY"] = os.environ.get('API_KEY')

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		db.execute("INSERT INTO users(username, email, password) VALUES(:username, :email, :password)",{"username":form.username.data, "email":form.email.data, "password":hashed_password})
		db.commit()
		return redirect(url_for('login.html'))
	return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = db.execute("SELECT * FROM users WHERE (email=:email)",{'email': form.email.data}).fetchone()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			
			return redirect(url_for('home'))
		else:
			flash("Invalid email or password. Try again", 'danger')			
	return render_template('login.html', form=form)


app.config["SECRET_KEY"]= os.environ.get('SECRET_KEY')
app.config["API_KEY"] = os.environ.get('API_KEY')
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template('index.html')

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
    
@app.route("/books/search/<search>")
def search_books(search):
    query= f"SELECT * FROM books WHERE isbn LIKE ('%{search}%') OR title LIKE ('%{search}%')  OR author LIKE ('%{search}%')"
    result=db.execute(query)
    return render_template('books.html', books=result)

if __name__ == '__main__':
    app.run(debug=True, port =5000)
    # db = DatabaseConnect()
