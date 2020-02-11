# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     __init__.py
   Author:        FesonX
   Email:         fesonx@foxmail.com
   GitHub:        github.com/FesonX
   date:          20-2-10
-------------------------------------------------
"""
from os import urandom

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from config import BASE_DIR


def create_app() -> Flask:
    app = Flask(__name__, template_folder=BASE_DIR + '/src/templates',
                static_folder=BASE_DIR + '/src/static')
    # Add your own instance config folder
    # And your own config.py
    # Contents should include `QLALCHEMY_DATABASE_URI` like the following description:
    # # Default is MySQLdb, for other driver, format like `mysql{+driver_name}:uri`
    # # For example, current project use `pymysql` as driver
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost:3306/db_name'
    app.config.from_pyfile(BASE_DIR + '/instance/config.py')
    app.config.update(SQLALCHEMY_RECORD_QUERIES=False)
    random_bytes = urandom(64)
    app.secret_key = random_bytes

    return app


app = create_app()
db = SQLAlchemy(app)
