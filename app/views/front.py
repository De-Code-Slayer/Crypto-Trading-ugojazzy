from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)


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

@frontend.route('/signup')
def register():
    return render_template('landing/signup.html')


@frontend.route('/base')
def base():
    return render_template('landing/base.html')