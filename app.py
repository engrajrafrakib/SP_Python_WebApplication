from flask import Flask, render_template, request, flash, url_for

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/hello')
def index():
    flash("What's your name?")
    return render_template('index.html')

@app.route('/greet', methods=['GET', 'POST'])

def greet():
    flash("Hello " + str(request.form['name_input']) + ", great to see you!")
    return render_template('index.html')

app.run()