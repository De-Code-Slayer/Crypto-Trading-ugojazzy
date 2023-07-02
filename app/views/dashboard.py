from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')



@dashboard.route('/')
def dashboard_home():
    return render_template('dashboard/index.html')


@dashboard.route('/transfers')
def transfers():
    return render_template('dashboard/exchange.html')

@dashboard.route('/wallets')
def wallet():
    return render_template('dashboard/wallet.html')

@dashboard.route('/profile')
def profile():
    return render_template('dashboard/profile-settings.html')

@dashboard.route('/sign-in')
def sign_in():
    return render_template('dashboard/signin.html')

@dashboard.route('/reset-password')
def reset_password():
    return render_template('dashboard/reset.html')

@dashboard.route('/log-out')
def sign_out():
    return render_template('dashboard/profile-settings.html')


@dashboard.route('/base')
def base():
    return render_template('dashboard/base.html')