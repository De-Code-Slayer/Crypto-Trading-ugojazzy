from app import db
from flask_login import UserMixin
from datetime import datetime



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String,unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=True)
    temporary_address = db.Column(db.String,nullable=True, default='')
    permanent_address = db.Column(db.String, nullable=True, default='')
    phone= db.Column(db.String, nullable=False, default='')
    
    # traders profile
    trader_profile_id = db.Column(db.Integer, db.ForeignKey('trader_profile.id'), nullable=True)
    traded_plan = db.Column(db.String, nullable=True, default='')
    traded_amount = db.Column(db.Float, nullable=True, default=0.0)
    traded_coin = db.Column(db.String, nullable=True, default='tether')
    trader_profile = db.relationship('TraderProfile', backref='trader', uselist=False)


    # withdrawal address
    trc_tether_wallet_address = db.Column(db.String, nullable=True, default='')
    erc_tether_wallet_address = db.Column(db.String, nullable=True, default='')
    ethereum_wallet_address = db.Column(db.String, nullable=True, default='')
    bitcoin_wallet_address = db.Column(db.String, nullable=True, default='')


    # verifications
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    verified  = db.Column(db.Boolean, nullable=False, default=False) 


    # crypto accounts
    tether_account = db.relationship('TetherAccount', uselist=False, backref='tether_acct', lazy=True)
    bitcoin_account = db.relationship('BitcoinAccount', uselist=False, backref='bitcoin_acct', lazy=True)
    ethereum_account = db.relationship('EthereumAccount', uselist=False, backref='ethereum_acct', lazy=True)

    ssn = db.Column(db.String, nullable=True, default='')
    display_photo = db.Column(db.String, nullable=True)
    postal_code = db.Column(db.String, nullable=False)
    
    card_payment_method = db.relationship('PaymentMethod', uselist=False, backref='card_user', lazy=True, foreign_keys='PaymentMethod.card_user_id')
    bank_payment_method = db.relationship('PaymentMethod', uselist=False, backref='bank_user', lazy=True, foreign_keys='PaymentMethod.bank_user_id')

    
    referer = db.relationship('Referrals', backref='reff_user', lazy=True, foreign_keys='Referrals.username')
    

class PaymentMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    bank_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    method_type = db.Column(db.String)  # 'card' or 'bank'
    card_number = db.Column(db.String)  # Unique field for card payment
    card_expiration = db.Column(db.String)
    card_cvv = db.Column(db.String)
    card_address = db.Column(db.String)
    bank_account_number = db.Column(db.String)  # Unique field for bank payment
    bank_routing_number = db.Column(db.String)
    bank_account_type = db.Column(db.String)
    bank_address = db.Column(db.String)

class TetherAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)
    interest_rate = db.Column(db.Float, default=0.0)
    address = db.Column(db.String, default='TLHBGbJx1kGjCYtSkY4phwgzZ9HiceUV9G')
    address_erc = db.Column(db.String, default='0xb16Bf2Eb63b18375F4836A492a3988A7C090B2B9')
    exchange_rate = db.Column(db.Float, default=0.0)
    fee = db.Column(db.Float, default=0.0) #charge for transactions
    vat = db.Column(db.Float, default=0.0) #value added tax

    holding_balance = db.Column(db.Float, default=0.0) #referral
    available_balance = db.Column(db.Float, default=0.0) # choice of amount for cl to withdraw
    pending_balance = db.Column(db.Float, default=0.0)# total of lock and holding
    locked_balance = db.Column(db.Float, default=0.0)#trading capital
    wallet_deposit_address = db.Column(db.String, default='')

    min_withdrawable_amount = db.Column(db.Float, default=0.0)

    transactions = db.relationship('Transactions', backref='tether_trx_user', lazy=True)
    # Add more fields as needed

class BitcoinAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)
    interest_rate = db.Column(db.Float, default=0.0)
    address = db.Column(db.String, default='bc1qr4cfv9x2g24jdvvtdyq2d0aj44hfsg9vda37lw')
    exchange_rate = db.Column(db.Float, default=0.0)
    fee = db.Column(db.Float, default=0.0) #charge for transactions
    vat = db.Column(db.Float, default=0.0) #value added tax

    holding_balance = db.Column(db.Float, default=0.0)
    available_balance = db.Column(db.Float, default=0.0)
    pending_balance = db.Column(db.Float, default=0.0)
    locked_balance = db.Column(db.Float, default=0.0)
    wallet_deposit_address = db.Column(db.String, default='')

    min_withdrawable_amount = db.Column(db.Float, default=0.0)

    transactions = db.relationship('Transactions', backref='btc_trx_user', lazy=True)
    # Add more fields as needed

class EthereumAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)
    interest_rate = db.Column(db.Float, default=0.0)
    address = db.Column(db.String, default='0xb16Bf2Eb63b18375F4836A492a3988A7C090B2B9')
    exchange_rate = db.Column(db.Float, default=0.0)
    fee = db.Column(db.Float, default=0.0) #charge for transactions
    vat = db.Column(db.Float, default=0.0) #value added tax

    holding_balance = db.Column(db.Float, default=0.0)
    available_balance = db.Column(db.Float, default=0.0)
    pending_balance = db.Column(db.Float, default=0.0)
    locked_balance = db.Column(db.Float, default=0.0)
    wallet_deposit_address = db.Column(db.String, default='')

    min_withdrawable_amount = db.Column(db.Float, default=0.0)

    transactions = db.relationship('Transactions', backref='eth_trx_user', lazy=True)
    # Add more fields as needed

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thether_account_user_id = db.Column(db.Integer, db.ForeignKey('tether_account.user_id'), nullable=True)
    bitcoin_account_user_id = db.Column(db.Integer, db.ForeignKey('bitcoin_account.user_id'), nullable=True)
    ethereum_account_user_id = db.Column(db.Integer, db.ForeignKey('ethereum_account.user_id'), nullable=True)
    transaction_type = db.Column(db.String)
    amount = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String)
    # Add more fields as needed

class Referrals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), db.ForeignKey('user.username'), nullable=False)
    reffered_user_name = db.Column(db.String)
    
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    # Add more fields as needed

class TraderProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trader_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    last_days_return_usd = db.Column(db.Float, nullable=True)
    numbers_of_trades = db.Column(db.String, nullable=True)
    last_months_return_usd = db.Column(db.Float, nullable=True)
    profit_percentage = db.Column(db.Float, nullable=True)
    loss_percentage = db.Column(db.Float, nullable=True)
    trading_hours = db.Column(db.Float, nullable=True)
    followers = db.Column(db.String, nullable=True)
    status = db.Column(db.String, nullable=True)

    # Add more fields for trader profile as needed