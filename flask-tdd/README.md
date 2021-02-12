# Flask TDD

### Setup

- mkdir my_app
- mkdir tests
- python -m venv env
- source env/bin/activate
- pip install flask
- pip install pytest
- pip freeze > requierment.txt

### First test

lets start with the test file tests/app_test.py (with env active, ie. source env/bin/activate)

- python -m pytest

It should return an error.
Now, add the my_app/app.py file, and rerun the test.

- python -m pytest

Now it should pass ...

you can run the app with :

FLASK_APP=my_app/app.py python -m flask run

and go to the web link:

http://127.0.0.1:5000/
