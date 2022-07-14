# connects/maps MySQL database to sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Log(db.Model):
    __tablename__ = 'rlogs'

    log_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)
    site_num = db.Column(db.Integer)
    action = db.Column(db.String(25))
    source_type = db.Column(db.String(25))
    source_id = db.Column(db.Integer)
    target_type = db.Column(db.String(25))
    target_id = db.Column(db.Integer)
    channel_num = db.Column(db.Integer)
    call_type = db.Column(db.Integer)

    # constructor
    def __init__(self, log_id, time, site_num, action, source_type, source_id, target_type, target_id, channel_num, call_type):
        self.log_id = log_id
        self.time = time
        self.site_num = site_num
        self.action = action
        self.source_type = source_type
        self.source_id = source_id
        self.target_type = target_type
        self.target_id = target_id
        self.channel_num = channel_num
        self.call_type = call_type

    def __repr__(self):
        return f'Log({self.log_id}, {self.time}, {self.site_num}, {self.action}, {self.source_type}, {self.source_id}, {self.target_type}, {self.target_id}, {self.channel_num}, {self.call_type})'
