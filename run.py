"""
Date: 08-03-19
This is the Main Python file that will run.
In this Python file we will:

    - Import the instance of the app from flask_paycheck_tracker/__init__.py
    - Call the run function from the instance
    - While in development, the debug wil be set to true.
"""

from flask_master_template import app

app.run(debug=True)
