from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'your_super_secret_key_here' 



@app.route('/')
def home():
    # If already logged in, send them straight to the dashboard
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

@app.route('/dashboard')
def dashboard():
  
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])
@app.route('/logout')
def logout():
    session.pop('username', None) 
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)
