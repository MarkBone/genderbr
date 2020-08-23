PYTHONCMD=python

deps:
	pip install -r requirements.txt

freeze:
    pip freeze > requirements.txt