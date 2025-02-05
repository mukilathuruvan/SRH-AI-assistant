from flask_sqlalchemy import SQLAlchemy
import os



db=SQLAlchemy()
def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql://root:root@localhost/srh_ai_assistance')   
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return db