from flask import  url_for
from string import ascii_letters, digits
from random import choice

def set_code(n):
    return ''.join(choice(ascii_letters + digits) for i in range(n))

def get_image_file(user):
    image_uri = user.image_file if user.is_authenticated else 'profileimg.jpg'
    return url_for('static', filename='resources/images/profile_pics/' + image_uri)
    