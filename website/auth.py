from flask import Blueprint,render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # '''retrive data from the form'''
    # data = request.form
    # print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('email is invalid', category='error')
        elif len(firstName) < 3:
            flash('Name must be more than 3 character', category='error')
        elif password1 != password2:
            flash('Password did not match', category='error') 
        elif len(password1) < 7:
            flash('Password must be more than 7 character', category='error')
        else:
            flash('Signup Succesful', category='successful')

    return  render_template('signup.html')