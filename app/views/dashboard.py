from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask_login import login_user, logout_user, login_required, current_user
from .view_utils.authentication import login_user_from_db
from .view_utils.data_objects import update_profile_info, get_trader, follow_trader
from .view_utils.currency_price import get_usd_to_



dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard.route('/')
@login_required
def dashboard_home():
    return render_template('dashboard/index.html')

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
    'usd_btc_rate'  : get_usd_to_('BTC'),
    'usd_usdt_rate' : get_usd_to_('USDT'),
    'usd_eth_rate'  : get_usd_to_('ETH'),
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
        traded_plan = request.get_json()['traded_plan']
        traded_amount = request.get_json()['amount']

        # follow trader
        followed = follow_trader(traded_plan, traded_amount, trader_id)
        if not followed:
            flash('Could not Follow','warning')
        else:
            flash('Followed','success')
    
    return render_template('dashboard/exchange.html', **exchange_rates, trader=trader, trader_list=trader_list)



@dashboard.route('/wallets')
@login_required
def wallet():

    exchange_rates = {
    'usd_btc_rate'  : get_usd_to_('BTC'),
    'usd_usdt_rate' : get_usd_to_('USDT'),
    'usd_eth_rate'  : get_usd_to_('ETH'),
    }
    return render_template('dashboard/wallet.html', **exchange_rates)

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