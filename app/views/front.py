from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


frontend = Blueprint('frontend', __name__, url_prefix='/')



@frontend.route('/')
def home():
    return render_template('landing/index.html')


@frontend.route('/base')
def base():
    return render_template('landing/base.html')