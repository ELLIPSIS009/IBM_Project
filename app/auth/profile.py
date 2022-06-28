from app import db
from app.models import User
from app.base import set_code
from datetime import datetime

def register(form, role):
    '''Registers a User given form data'''
    user = User(firstName=form.firstName.data, lastName=form.lastName.data, email=form.email.data, urole=role, confirmed=False)
    user.set_password(form.password.data)
    if role == 'student':
        set_knewbie_id(user)
    db.session.add(user)
    db.session.commit()
    return user
        
def confirm_user(user):
    user.confirmed = True
    user.confirmed_on = datetime.now()
    db.session.commit()

def set_knewbie_id(user):
    code = set_code(8)
    while User.query.filter_by(knewbie_id=code).first():
        code = set_code(8)
    user.knewbie_id = code
    return user