import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_migrate import Migrate
from os.path import join, dirname, realpath
from dotenv import load_dotenv
from sqlalchemy.engine.url import make_url

# Load environment variables from .env file
load_dotenv()

# create the extension
db = SQLAlchemy()


heroku_database_url = os.getenv('DATABASE_URL')
# Create a URL object from the Heroku database URL
parsed_url = make_url(heroku_database_url)

# Modify the drivername to match SQLAlchemy's PostgreSQL dialect
parsed_url_str = str(parsed_url).replace("postgres://", "postgresql://")

# upload path
UPLOADS_PATH = join(dirname(realpath(__file__)), u'static\\uploads')

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),    
    )

    print(os.getenv('DATABASE_URL'),parsed_url_str,'----------===========>>>>>>')
    # upload folder
    app.config['UPLOAD_FOLDER'] = UPLOADS_PATH
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI') #local testing
    app.config["SQLALCHEMY_DATABASE_URI"] = parsed_url_str

    # init flask migrate
    migrate = Migrate(app, db)


    # initialize the app with the extension
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import db models
    from .database.models import User

    with app.app_context():
        db.create_all()

    #  register views
    from .views.front import frontend
    from .views.dashboard import dashboard
    app.register_blueprint(frontend)
    app.register_blueprint(dashboard)

    # setup login manager
    login_manager = LoginManager(app)
    login_manager.login_view = 'dashboard.sign_in'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    return app

app = create_app()