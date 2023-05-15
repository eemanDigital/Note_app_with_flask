from flask import Flask

def create_app():
    app = Flask(__name__)
    '''enable sucirty fof the app'''
    app.config['SECRET_KEY'] = 'salmandjdjgh dkkdfkdijds'

    '''register blueprints'''
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix  ='/')
    app.register_blueprint(auth, url_prefix ='/')


    return app