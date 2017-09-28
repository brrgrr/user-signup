from flask import Flask, request, redirect, render_template
import string

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


def is_valid_length(text):
    return (len(text) >= 3 and len(text) <= 20)


def contains_space(text):
    try:
        text.index(' ')
        return True
    except ValueError:
        return False


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
    if not (is_valid_length(username) and username.isalnum()):
        username_err = 'Invalid username. Must be 3-20 alphanumeric characters, with no spaces.'

    # Password validation
    if not is_valid_length(password):
        password_err = 'Invalid password. Must be 3-20 characters.'

    # Password verification
    if not (password == verify):
        verify_err = 'Passwords do not match.'

    # Email validation
    if email:
        if not (email.count('@') == 1 and email.count('.') == 1 and not contains_space(email) and is_valid_length(email)):
            email_err = 'Invalid email address.'

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
