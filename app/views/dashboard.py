from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask_login import login_user, logout_user, login_required 
from .view_utils.authentication import login_user_from_db
from .view_utils.data_objects import update_profile_info



dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard.route('/')
@login_required
def dashboard_home():
    return render_template('dashboard/index.html')

@dashboard.route('/trade-live')
@login_required
def live_trading():
    return render_template('dashboard/trade.html')

@dashboard.route('/transfers')
@login_required
def transfers():
    return render_template('dashboard/exchange.html')

@dashboard.route('/wallets')
@login_required
def wallet():
    return render_template('dashboard/wallet.html')

@dashboard.route('/profile', methods=['GET','POST','PUT'])
@login_required
def profile():
    # user info update
    if request.method == 'POST':
        updated = update_profile_info(request.form, file=request.files)
        if updated:
            flash('User info updated', 'success')
    return render_template('dashboard/profile-settings.html')

@dashboard.route('/sign-in', methods=['GET','POST'])
def sign_in():
    if request.method == 'POST':
        
        user = login_user_from_db(request.form)
        if user:
            # logg in
            login_user(user, remember=True)
            return redirect(url_for('dashboard.dashboard_home'))
        else:
            flash('Username or password Invalid','warning')


    return render_template('dashboard/signin.html')

@dashboard.route('/reset-password')
def reset_password():
    return render_template('dashboard/reset.html')

@dashboard.route('/log-out')
@login_required
def sign_out():
    logout_user()
    return redirect(url_for('dashboard.sign_in'))


@dashboard.route('/base')
def base():
    return render_template('dashboard/base.html')