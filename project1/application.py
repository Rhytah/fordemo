import os


from flask import Flask, render_template, url_for, redirect
from form import RegistrationForm, LoginForm 



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



@app.route('/search', methods=['POST', 'GET'])
def search():
	form = SearchForm()
	if form.validate_on_submit():
		results = db.execute("SELECT * FROM books WHERE author LIKE  '%a%' ORDER BY id OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY ")
		print(results)
		return render_template('results.html', results=results)
		# return redirect(url_for('home'))
	return render_template('search.html', form=form)


@app.route('/query', methods=['POST', 'GET'])
def query():
	form = SearchForm()
	if form.validate_on_submit():
		params = {
			'api_key':'{API_KEY}',}
		r = requests.get('https://www.goodreads.com/book/review_counts.json',{'params':params, 'isbns':form.isbns.data})
		return render_template('results.html', results=json.loads(r.text)['books'])
	return render_template('search.html', form=form)