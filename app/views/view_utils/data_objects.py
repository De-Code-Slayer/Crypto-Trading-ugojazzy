from app.database.models import User, Transactions, TraderProfile
from werkzeug.utils import secure_filename
from .email import send_mail
from flask_login import current_user
from app import db, UPLOADS_PATH
import logging
from os import path



ALLOWED_EXTENSIONS = {'png', 'jpg','jpeg'}

basedir = path.abspath(path.dirname(__file__))

def follow_trader(traded_plan, traded_amount, trader_id):
    try:
        current_user.trader_profile_id = trader_id
        current_user.traded_plan = traded_plan
        current_user.traded_amount = traded_amount
        db.session.commit()
    except Exception as e:
        # Handle specific exceptions or provide a general error message
        logging.error(f'Error occurred: {str(e)}')
        return False
    else:
        return True


def get_trader(request_data=None, user_trader=None):
    if request_data:
        # return trader by trader id
        trader_id = request_data.get('trader_id')
        return TraderProfile.query.filter((TraderProfile.id == trader_id)).first()
    if user_trader:
        # return current user followed trader if passed
        return TraderProfile.query.filter((TraderProfile.id == user_trader)).first()
    else:
        # return list of all traders
         return TraderProfile.query.all()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file) -> str:
    if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(path.join(UPLOADS_PATH, filename))
            # return url_for('static', filename="images/{filename}")
            return filename


def update_profile_info(form_data,file=None):

    profile_photo = file.get('profile_photo')
    username = form_data.get('username')

    # try to update userinfo section
    try:
        if profile_photo:
            current_user.display_photo = save_file(profile_photo)
        
        if username:
            current_user.username = username

        db.session.commit()
    except Exception as e:
        # Handle specific exceptions or provide a general error message
        logging.error(f'Error occurred: {str(e)}')
        return False

    #  update Security Informations
    email = form_data.get('email')
    password = form_data.get('password')

    try:
        if email:
            current_user.email = email
        
        if password:
            current_user.password = password

        db.session.commit()
    except Exception as e:    
        # Handle specific exceptions or provide a general error message
        logging.error(f'Error occurred: {str(e)}')
        return False




    # try to update personal informations
    dob                 = form_data.get('dob')
    present_address     = form_data.get('present_address')
    permanent_address   = form_data.get('permanent_address')
    postal_code         = form_data.get('postal_code')
    city                = form_data.get('city')
    


    try:
        if dob:
            current_user.dob = dob

        if present_address:
            current_user.temporary_address = present_address

        if permanent_address:
            current_user.permanent_address = permanent_address

        if postal_code:
            current_user.postal_code = postal_code

        if city:
            current_user.city = city



        db.session.commit()
    except Exception as e:
        # Handle specific exceptions or provide a general error message
        logging.error(f'Error occurred: {str(e)}')
        return False
        

    return True


def proccess_withdrawal(request_data):
    amount = request_data.get('amount')
    address = request_data.get('address')

    message = f'withdrawal request to address: {address} for amount {amount}'
    subject =  f'Withdrawal Request from {current_user.full_name}'
    mail_address = current_user.email

    # send email to site owner
    emailed = send_mail(mail_address, subject, message)

    # create transaction record
    trx = Transactions(thether_account_user_id=current_user.id, amount=amount, transaction_type='debit', status='pending')

    db.session.add(trx)
    db.session.commit()
    if emailed:
    #   debit user
        return True
    else:
        return False









