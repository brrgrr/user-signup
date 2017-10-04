from flask import Flask, request, redirect, render_template
import string
import re

app = Flask(__name__)

app.config['DEBUG'] = True

title = 'User Signup'


@app.route('/')
def index():
    return render_template(
        'signup_form.html',
        title=title,
        username='', username_err='',
        password='', password_err='',
        verify='', verify_err='',
        email='', email_err=''
    )


def is_valid(text):
    return re.search(r'(^[^\s]{3,20}$)', text)


def is_valid_email(text):
    return (is_valid(text) and re.search(r'^[^\s@\.]+@[^\s@\.]+\.[^\s@\.]+$', text))


@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username'].strip()
    password = request.form['password'].strip()
    verify = request.form['verify'].strip()
    email = request.form['email'].strip()

    username_err = ''
    password_err = ''
    verify_err = ''
    email_err = ''

    # Username validation
    if not is_valid(username):
        username_err = 'Username is not valid. Must be 3-20 characters, no white space.'

    # Password validation
    if not is_valid(password):
        password_err = 'Password is not valid. Must be 3-20 characters, no white space.'

    # Password verification
    if not password == verify:
        verify_err = 'Passwords do not match.'

    # Email validation
    if not is_valid_email(email):
        email_err = 'Email address is not valid. Must be 3-20 characters, no white space, and include "@" and "."'

    if not username_err and not password_err and not verify_err and not email_err:
        # Success
        return redirect('welcome?username={0}'.format(username))
    else:
        if username_err:
            uvs = 'is-invalid'
        else:
            uvs = 'is-valid'
        if password_err:
            pvs = 'is-invalid'
        else:
            pvs = 'is-valid'
        if verify_err:
            vvs = 'is-invalid'
        else:
            vvs = 'is-valid'
        if email_err:
            evs = 'is-invalid'
        else:
            evs = 'is-valid'

        return render_template(
            'signup_form.html',
            title=title,
            username=username, email=email,
            username_vstate=uvs, username_err=username_err,
            password_vstate=pvs, password_err=password_err,
            verify_vstate=vvs, verify_err=verify_err,
            email_vstate=evs, email_err=email_err
        )


@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template(
        'welcome.html',
        title=title,
        username=username
    )


if __name__ == '__main__':
    app.run()
