from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import user_model

# Homepage and login & registration:

# route to display registration and login form
@app.route('/')
def display_home_page():
    return render_template('home.html')


@app.route('/register')
def display_register_page():
    return render_template('register.html')

# route for registration form
@app.route('/register', methods=['POST'])
def register_new_user_form():
    if not user_model.User.validate_registration(request.form):
        return redirect("/register")

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }

    id = user_model.User.create_new_user(data)
    session['id'] = id
    return redirect ('/mylibrary')

@app.route('/login')
def display_login_page():
    return render_template('login.html')

# route for login form
@app.route('/login', methods=['POST'])
def user_login_form():
    user_in_db = user_model.User.get_user_by_email(request.form['email'])

    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect('/login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", 'login')
        return redirect('/login')

    session['id'] = user_in_db.id
    return redirect('/mylibrary')


# route to clear session for logging out
@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect("/")

