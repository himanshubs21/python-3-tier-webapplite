from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template_string("""
            <p>Hello, welcome to this app</p>
            <form method="post">
                <input type="text" name="user_input" />
                <input type="submit" value="OK" />
            </form>
            <h2>Thank you, we received your response: {{ user_input }}</h2>
        """, user_input=user_input)
    
    return render_template_string("""
        <p>Hello, welcome to this app</p>
        <form method="post">
            <input type="text" name="user_input" />
            <input type="submit" value="OK" />
        </form>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
