from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from .view_utils.authentication import handle_registration


frontend = Blueprint('frontend', __name__, url_prefix='/')



@frontend.route('/')
def home():
    return render_template('landing/index.html')

@frontend.route('/trade')
def buy_and_sell():
    return render_template('landing/buy-sell.html')

@frontend.route('/wallet')
def wallet():
    return render_template('landing/wallet-features.html')

@frontend.route('/market')
def market_data():
    return render_template('landing/market-data.html')

@frontend.route('/contact')
def contact():
    return render_template('landing/contact.html')

@frontend.route('/support')
def support():
    return render_template('landing/faqs.html')

@frontend.route('/signup', methods=['GET','POST'])
def register():
    if request.method == 'POST':

        form_data = request.form
        registered = handle_registration(form_data)

        if registered:
            # login user
            return redirect(url_for('dashboard.dashboard_home'))
        
        elif registered == {'error': 'User already exists'}:
            flash('Email already in used, login instead', 'warning')

        else:
            flash('Could not register user', 'warning')

    return render_template('landing/signup.html')


@frontend.route('/base')
def base():
    return render_template('landing/base.html')