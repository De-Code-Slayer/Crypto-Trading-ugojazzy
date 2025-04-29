from app.database.models import User, Referrals, BitcoinAccount, EthereumAccount, TetherAccount
from flask import (session)
from app import db
import logging
from .email import send_mail
import jwt
import datetime
import os

def login_user_from_db(form_data) -> User:
    try:
    # Extract the required data from form_data using argument unpacking
        email, password,  = (    
            form_data.get('email'),
            form_data.get('password')
        )
        # ... extract other necessary fields
        
        # return user from db
        return User.query.filter((User.email == email) & (User.password == password)).first()

    except Exception as e:
        # Handle specific exceptions or provide a general error message
        logging.error(f'Error occurred during user registration: {str(e)}')
        return False
    return None

def get_user_by_email(email):
    return User.query.filter((User.email == email)).first()

def check_if_user_exists_in_db(email, username=None):
    return User.query.filter((User.username == username) | (User.email == email)).first()

def handle_registration(form_data):
    from flask import render_template
    try:
    # Extract the required data from form_data using argument unpacking
        full_name, email, password, dob, country, phone, postal_code, referer = (
            form_data.get('fullname'),
            form_data.get('email'),
            form_data.get('password'),
            form_data.get('dob'),
            form_data.get('country'),
            form_data.get('phone'),
            form_data.get('postal_code'),
            form_data.get('referee')
        )
        # ... extract other necessary fields
        
        # check if user already exists
        if check_if_user_exists_in_db(email):
            logging.error(f'User already exists')
            return {'error': 'User already exists'}

        
        
        user = User(
            full_name=full_name,
            email=email,
            password=password,
            dob=dob,
            country=country,
            phone=phone,
            username=full_name,
            postal_code=postal_code,
        )
        email_link = f'https://www.potomaccopytrade.com/dashboard/verify/{generate_verification_token(email)}'
        if referer:
            referal = Referrals(reffered_user_name=full_name, username=referer)
            db.session.add(referal)
        # elif session.get('referral_code', None):
        #     referer = session.get('referral_code', None)  # Get the referral code from the session (if available) to mark the referrer
        #     referal = Referrals(reffered_user_name=full_name, username=referer)
        #     db.session.add(referal)



        # Save the user to the database
        db.session.add(user)
        db.session.commit()

        html_mail = render_template('email/confirmemail.html', email_link=email_link)
        send_mail(email,'Verify Email',html_mail )

    except Exception as e:
        # Handle specific exceptions or provide a general error message
        logging.error(f'Error occurred during user registration: {str(e)}')
        return False
    
    # Return a response indicating successful registration
    create_crypto_account(email)
    
    return True

def resend_verification_mail():
    from flask_login import current_user
    from flask import render_template
    email_link = f'https://www.potomaccopytrade.com/dashboard/verify/{generate_verification_token(current_user.email)}'

    html_mail = render_template('email/confirmemail.html', email_link=email_link)
    
    return send_mail(current_user.email,'Verify Email',html_mail )



def create_crypto_account(email):
    try:
    # Start creation of crypto accounts
    # get user by email
        user = get_user_by_email(email)
    # create account by user id
        tether = TetherAccount(   user_id = user.id)
        ether = EthereumAccount( user_id = user.id)
        btc = BitcoinAccount(  user_id = user.id)

        # add to database and commit
        db.session.add(tether)
        db.session.add(ether)
        db.session.add(btc)
        db.session.commit()
    except Exception as e:
        
        # Handle specific exceptions or provide a general error message
        logging.error(f'Error occurred during crypto account creation: {str(e)}')
        return False
    return True


def verify(payload):
    if "user_id" in payload:
        user_id = payload["user_id"]
        user = get_user_by_email(user_id)

        if user:
            # Check if the token is not expired
            # Assuming payload["exp"] is a Unix timestamp (an integer)
            timestamp = payload["exp"]
            exp_datetime = datetime.datetime.utcfromtimestamp(timestamp)

            if exp_datetime >= datetime.datetime.utcnow():
                # Update the 'update' column to true
                user.confirmed = True
                db.session.commit()
                return True
            
        return False
            
SECRET_KEY = os.getenv('SECRET_KEY') 
EXPIRATION_TIME = os.getenv('EXPIRATION_TIME')  # Set the expiration time in seconds (e.g., x hours)



def generate_verification_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=int(EXPIRATION_TIME))
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_verification_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Invalid token
        return None


