from flask import Flask, request, render_template_string, g
import sqlite3

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('database.db')
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        db = get_db()
        db.execute('INSERT INTO user_input (input) VALUES (?)', (user_input,))
        db.commit()
        return render_template_string("""
            <p>Hello, welcome to this app</p>
            <form method="post">
                <input type="text" name="user_input" />
                <input type="submit" value="OK" />
            </form>
            <h2>You entered: {{ user_input }}</h2>
        """, user_input=user_input)
    
    return render_template_string("""
        <p>Hello, welcome to this app</p>
        <form method="post">
            <input type="text" name="user_input" />
            <input type="submit" value="OK" />
        </form>
    """)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(host='0.0.0.0', port=80)
