from flask import Blueprint, render_template, url_for, flash, redirect
from flask_master_template.forms.forms import LoginForms
from flask_master_template.models.models import Users, createall, commit, addit

login = Blueprint('login', __name__)


@login.route('/login', methods=['GET', 'POST'])
def loginpage():
    form = LoginForms()
    if form.validate_on_submit():
        try:
            flash(f'User {form.username.data} added successfully!!!', 'success-message')
            print(form.username.data)
            createall()
            users = Users(username=form.username.data, password=form.password.data)
            addit(users)
            commit()
            print(users.__repr__())
            return redirect(url_for('home.homepage'))
        except:
            flash(f'User {form.username.data} not found', 'error-message')

    print(form.username.data)
    return render_template('login/login.html', title='Login', form=form)
