from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/Main/main.do')
def home():
    return render_template('index.html')


@app.route('/')
def index():
    return redirect(url_for('home')+'?site=main01')


if __name__ == '__main__':
    app.run(debug=True)
