from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

title = 'User Signup'


@app.route("/")
def index():
    return render_template(
        'index.html',
        title=title
    )


@app.route("/welcome")
def welcome():
    return render_template(
        'welcome.html',
        title=title,
        username="Bob"
    )


if __name__ == '__main__':
    app.run()
