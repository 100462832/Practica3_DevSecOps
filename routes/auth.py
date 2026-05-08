from db import get_users_connection, hash_password
from flask import request, redirect, render_template, session, flash, url_for
from server import app
from urllib.parse import urlparse

def is_safe_redirect_url(url):
    parsed = urlparse(url)
    return not parsed.netloc and not parsed.scheme

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))

    next_url = request.args.get('next', '')
    if is_safe_redirect_url(next_url):
        session['next_url'] = urlparse(next_url).path  # solo guardamos el path
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_users_connection()
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        user = conn.execute(query, (username, hash_password(password))).fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            session['company_id'] = user['company_id']
            session.permanent = True
            destination = session.pop('next_url', None) or url_for('dashboard')
            return redirect(destination)
        else:
            flash("Invalid username or password", "danger")
            return render_template('auth/login.html', next_url=next_url)
    return render_template('auth/login.html', next_url=next_url)


@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))
