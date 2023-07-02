from app import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)
    dob = db.Column(db.String)
    country = db.Column(db.String)
    temporary_address = db.Column(db.String)
    permanent_address = db.Column(db.String)
    phone= db.Column(db.String)

    # crypto accounts
    tether_account = db.relationship('TetherAccount', uselist=False, backref='user', lazy=True)
    bitcoin_account = db.relationship('BitcoinAccount', uselist=False, backref='user', lazy=True)
    ethereum_account = db.relationship('EthereumAccount', uselist=False, backref='user', lazy=True)

    ssn = db.Column(db.String)
    display_photo = db.Column(db.String)
    postal_code = db.Column(db.String)
    
    card_payment_method = db.relationship('PaymentMethod', uselist=False, backref='user', lazy=True, foreign_keys='PaymentMethod.card_user_id')
    bank_payment_method = db.relationship('PaymentMethod', uselist=False, backref='user', lazy=True, foreign_keys='PaymentMethod.bank_user_id')

    
    refferals = db.relationship('Refferals', backref='user', lazy=True, foreign_keys='Refferals.user_id')

    transactions = db.relationship('Transactions', backref='user', lazy=True)

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
    balance = db.Column(db.Float)
    address = db.Column(db.String)
    # Add more fields as needed

class BitcoinAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    balance = db.Column(db.Float)
    address = db.Column(db.String)
    # Add more fields as needed

class EthereumAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    balance = db.Column(db.Float)
    address = db.Column(db.String)
    # Add more fields as needed

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    transaction_type = db.Column(db.String)
    amount = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    # Add more fields as needed

class Referrals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reffered_user_name = db.Column(db.String)
    
    timestamp = db.Column(db.DateTime)
    # Add more fields as needed

