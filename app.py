from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def index():
    flash("What's your name?")
    return render_template('index.html')

@app.route('/greet', methods=['GET', 'POST'])

def greet():
    flash("Hello " + str(request.form['name_input']) + ", great to see you!")
    return render_template('index.html')

# app.run(host='0.0.0.0', port=8000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)