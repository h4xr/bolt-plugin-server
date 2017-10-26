'''
File: app.py
Description: The main entrypoint file for the application server
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 26/10/2017
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
