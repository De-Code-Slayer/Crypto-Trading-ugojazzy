from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from flask_login import login_user, logout_user, login_required, current_user
from .view_utils.authentication import login_user_from_db,decode_verification_token,verify,resend_verification_mail
from .view_utils.data_objects import update_profile_info, get_trader, follow_trader, proccess_withdrawal,get_trx
from .view_utils.currency_price import get_usd_to_



dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard.route('/')
@login_required
def dashboard_home():
    trx=get_trx()
    

    return render_template('dashboard/index.html', trx=trx)

@dashboard.route('/trade-live')
@login_required
def live_trading():
    return render_template('dashboard/trade.html')

@dashboard.route('/tradeplans')
@login_required
def trade_plans():
    return render_template('dashboard/tradeplans.html')

# copy trading
@dashboard.route('/transfers', methods=('POST','PUT','GET'))
@login_required
def transfers():
    exchange_rates = {
    'usd_btc_rate'  : get_usd_to_().get('BTC'),
    'usd_usdt_rate' : get_usd_to_().get('USDT'),
    'usd_eth_rate'  : get_usd_to_().get('ETH'),
    }
    # get followed trader info
    trader_list = get_trader() # - populate the trader list when page is opened at any time
    trader = get_trader(user_trader = current_user.trader_profile_id) # returns the followed trader by the user
    # used to view the info of selected trader by clicking view profile
    if request.method == 'PUT':
        # get info of selected trader
        trader = get_trader(request.get_json())
    if request.method=="POST":
        trader_id = request.get_json()['trader_id']
        traded_plan = request.get_json()['selected_plan']
        traded_amount = request.get_json()['amount']

        # follow trader
        followed = follow_trader(traded_plan, traded_amount, trader_id)
        if not followed:
            flash('Could not Follow','warning')
        else:
            flash('Followed','success')
    
    return render_template('dashboard/exchange.html', **exchange_rates, trader=trader, trader_list=trader_list)

@dashboard.route('/wallets', methods=['GET','POST'])
@login_required
def wallet():

    transactions = {
        'usdt_trx': current_user.tether_account.transactions,
        'eth_trx' : current_user.ethereum_account.transactions,
        'btc_trx' : current_user.bitcoin_account.transactions,
    }

    exchange_rates = {
    'usd_btc_rate'  : get_usd_to_().get('BTC'),
    'usd_usdt_rate' : get_usd_to_().get('USDT'),
    'usd_eth_rate'  : get_usd_to_().get('ETH'),
    }

    if request.method == 'POST':
        withdrawn = proccess_withdrawal(request.form)
        if withdrawn:
            flash('Withdrawal in progress', 'success')
        else:
            flash('Withdrawal request was not sent, contact account manager','warning')

    return render_template('dashboard/wallet.html', **exchange_rates, **transactions)

@dashboard.route('/profile', methods=['GET','POST','PUT'])
@login_required
def profile():
    # user info update
    if request.method == 'POST':
        updated = update_profile_info(request.form, file=request.files)
        if updated:
            flash('User info updated', 'success')
    return render_template('dashboard/profile-settings.html')

@dashboard.route('/security', methods=['GET','POST'])
@login_required
def security():
    # user info update
    
    return render_template('dashboard/security-settings.html')

@dashboard.route('/payment-method', methods=['GET','POST'])
@login_required
def payment_method():
    # user info update
    
    return render_template('dashboard/payment-method.html')

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
    # if request.method == 'POST':
        
    return render_template('dashboard/reset.html')

@dashboard.route('/log-out')
@login_required
def sign_out():
    logout_user()
    return redirect(url_for('dashboard.sign_in'))

@dashboard.route('/base')
def base():
    return render_template('dashboard/base.html')


@dashboard.route("/verify/<verification_token>")
def verify_email(verification_token):
    payload = decode_verification_token(verification_token)

    if verify(payload):
        flash("Email verification successful!", "success")
    else:
        flash("The link is invalid or expired", "warning")


    return redirect(url_for("dashboard.student_home"))


@dashboard.route('/resend-mail/')
def resend_mail():
    if resend_verification_mail():
        flash('Email re-sent successfully', 'success')
    else:
        flash('Email couldd not be sent', 'warning')
    return redirect(request.referrer or url_for("dashboard.dashboard_home")) #rediect to page that sent the request