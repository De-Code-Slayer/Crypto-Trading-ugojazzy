from app.database.models import User, Referrals
from flask_login import current_user
from app import db
import logging


def save_file() -> str:
    pass


def update_profile_info(form_data):
    profile_photo = form_data.get('profile_photo')
    username = form_data.get('username')

    # try to update userinfo section
    try:
        if profile_photo:
            profile_photo = save_file()
            current_user.display_photo = profile_photo
        
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
            current_user.present_address = present_address

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


    
