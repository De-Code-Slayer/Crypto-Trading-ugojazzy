from app.database.models import User, Referrals
from app import db
import logging

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

def check_if_user_exists_in_db(email, username=None):
    return User.query.filter((User.username == username) | (User.email == email)).first()

def handle_registration(form_data):
    
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
        if referer:
            referal = Referrals(reffered_user_name=full_name, username=referer)
            db.session.add(referal)

        # Save the user to the database
        db.session.add(user)
        db.session.commit()

        # Return a response indicating successful registration
        return True

    except Exception as e:
        # Handle specific exceptions or provide a general error message
        logging.error(f'Error occurred during user registration: {str(e)}')
        return False


