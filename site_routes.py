from flask import Blueprint, render_template


site = Blueprint('site', __name__)


@site.route('/')
def index():
    '''
    load homepage
    '''
    return render_template('index.html')
