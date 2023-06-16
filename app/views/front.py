from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


frontend = Blueprint('frontend', __name__, url_prefix='/')



@frontend.route('/hello')
def hello():
    return 'Hello, World!'