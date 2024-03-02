from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import book_model, user_model

# route to display my library with all the books the user has added.

@app.route('/mylibrary')
def display_my_library():
    if 'id' not in session:
        flash("You need to log in to access that page.", "login")
        return redirect("/")

    all_books = book_model.Book.get_all_books_from_one_user()
    user_in_session = user_model.User.get_user_by_id({'id': session['id']})

    return render_template('dashboard.html', all_books = all_books, user_in_session = user_in_session)
