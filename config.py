'''
File: config.py
Description: Application level configuration.
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 26/10/2017
'''

#WARNING: DO NOT MODIFY UNLESS NECESSARY.

DEBUG = True
SECRET_KEY = 'my_secret_key'

#SQLAlchemy related configuration
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://test:test123@localhost/bolt_plugins'
SQLALCHEMY_TRACK_MODIFICATIONS = True   #Enable it for development purpose
