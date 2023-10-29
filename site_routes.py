from flask import Blueprint, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create Form Class
class LoginForm(FlaskForm):
    '''
    Login Form fields
    '''
    username = StringField("Input your username.", validators=[DataRequired()])
    password = StringField("Input your password.", validators=[DataRequired()])
    submit = SubmitField('Submit')


# views to not include
login_form_views = []


def include_login_form(fn):
    login_form_views.append(fn.__name__)
    return fn


site = Blueprint('site', __name__)


@site.context_processor
def additional_parameters():
    if request.endpoint in login_form_views:
        return {}

    name = None
    form = LoginForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    
    return {
        'name': name,
        'form': form
    }

@site.route('/')
@include_login_form
def index():
    return render_template('index.html')


