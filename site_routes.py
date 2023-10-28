from flask import Blueprint, render_template, jsonify


site = Blueprint('site', __name__)


@site.route('/')
def index():
    return render_template('index.html')