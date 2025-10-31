from flask import Flask, render_template, request, redirect, url_for, session, jsonify # type: ignore
import random

app = Flask(__name__)
app.secret_key = "super_secret_key"

USERS = {"admin": "password123"}  # demo login

# Puzzle words
WORD_LIST = ["PYTHON", "FLASK", "CODE", "DEBUG", "ARRAY"]

def generate_grid(size=8):
    grid = [[chr(random.randint(65, 90)) for _ in range(size)] for _ in range(size)]
    # Hide words horizontally
    for word in WORD_LIST:
        if len(word) > size: continue
        row = random.randint(0, size-1)
        col = random.randint(0, size-len(word))
        for i, ch in enumerate(word):
            grid[row][col+i] = ch
    return grid

@app.route('/')
def home():
    if 'user' in session:
        grid = generate_grid()
        return render_template('puzzle.html', grid=grid, words=WORD_LIST, user=session['user'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            session['user'] = username
            return redirect(url_for('home'))
        return render_template('login.html', error="Invalid credentials.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/check_word', methods=['POST'])
def check_word():
    data = request.get_json()
    word = data.get('word', '').upper()
    return jsonify({"found": word in WORD_LIST})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
