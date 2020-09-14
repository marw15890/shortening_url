import string
from random import choices
from .db import db
from datetime import datetime

SHORT_LENGTH = 6


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256))
    shortcode = db.Column(db.String(SHORT_LENGTH), unique=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    last_redirect = db.Column(db.DateTime)
    redirect_count = db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shortcode = self.generate_shortcode()

    def update_stats(self):
        '''
        Updates stats for number of visits and the last visit.
        '''
        self.redirect_count += 1
        self.last_redirect = datetime.utcnow()

    def generate_shortcode(self):
        '''
        Generates a shortcode consisting of alphanumeric characters and underscore.
        :return: shortcode
        '''
        characters = string.ascii_letters + string.digits + '_'
        shortcode = ''.join(choices(characters, k=SHORT_LENGTH))

        url = self.query.filter_by(shortcode=shortcode).first()

        if url:
            return self.generate_shortcode()

        return shortcode

