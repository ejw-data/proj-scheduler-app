from flask import Blueprint, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from query import login_request


# Create Form Class
class LoginForm(FlaskForm):
    '''
    Login Form fields
    '''
    username = StringField("Input your Username.", validators=[DataRequired()])
    password = StringField("Input your Password.", validators=[DataRequired()])
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
        name = Authentication.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Authentication()
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash("User Added Successfully")

    return {
        'name': name,
        'form': form
    }

@site.route('/')
@include_login_form
def index():
    return render_template('index.html')


