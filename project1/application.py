import os

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('/register.html')

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
