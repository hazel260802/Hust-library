from pickle import FALSE
from tarfile import RECORDSIZE
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=FALSE
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import SinhVien
    from .models import NhanVien


    

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        global record
        if 'user_type' in session:
            if session["user_type"] == "sinhvien":
                record = SinhVien.query.get(int(user_id))
            if session["user_type"] == "nhanvien":
                record = NhanVien.query.get(int(user_id))
            return record

    # def load_user(user_id):
    #     if user_id == SinhVien.MSSV:
    #         return SinhVien.query.get(user_id)
    #     elif user_id == NhanVien.MSNV:
    #         return NhanVien.query.get(user_id)
    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created database!")



