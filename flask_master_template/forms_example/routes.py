import base64
from flask import Blueprint, render_template, url_for, flash, redirect
from flask_master_template.forms.forms import ExampleForm
from flask_master_template.models.models import FExample, createall, commit, addit

forms_example = Blueprint('forms_example', __name__)


@forms_example.route('/forms_example', methods=['GET', 'POST'])
def formsexamplepage():
    print('Loaded')
    form = ExampleForm()
    if form.validate_on_submit():
        if form.files.data:
            foo = base64.encodebytes(form.files.data.encode())
        print('Executed')
        flash(f'Form {form.string.data} added successfully!!!', 'success-message')
        createall()
        forms_example_db = FExample(string=form.string.data, password=form.password.data,
                                    floats=form.floats.data, booleans=form.booleans.data,
                                    selects=form.selects.data,
                                    files=foo, dates=form.dates.data)
        print('inserted')
        addit(forms_example_db)
        print('added')
        commit()
        return redirect(url_for('home.homepage'))
    else:
        print('error')
    return render_template('forms_example/forms_example.html', title='Forms Example', form=form)
