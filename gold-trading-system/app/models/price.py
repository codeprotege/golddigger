from datetime import datetime
from run import db

class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gold_id = db.Column(db.Integer, db.ForeignKey('gold.id'))
    price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Price {self.gold_id} {self.price}>'
