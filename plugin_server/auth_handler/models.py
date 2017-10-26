'''
File: models.py
Description: Models for the authentication handler
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 26/10/2017
'''
from plugin_server.app import db

class User(db.Model):
    """User definition model

    The model provides definitions for the User table such as the fields and
    their type definition.
    """

    id = db.Column(db.Interger, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255))
    reg_date = db.Column(db.DateTime(), default=datetime.datetime())
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        """Return the representative version of the Model"""

        return '<User %r'> % self.id

class Permissions(db.Model):
    """Permission definition model

    The model provides definition for the management of user priviledges
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    permissions = db.Column(db.Integer, default=1)
    last_updated = db.Column(db.Integer, default=datetime.datetime())

    def __repr__(self):
        """Return the representative version of the permission model"""

        return '<Permissions %r>' % self.id
