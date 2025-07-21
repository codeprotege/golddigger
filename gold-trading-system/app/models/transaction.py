from datetime import datetime
from run import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    gold_id = db.Column(db.Integer, db.ForeignKey('gold.id'))
    transaction_type = db.Column(db.String(10))  # 'buy' or 'sell'
    amount = db.Column(db.Float)
    price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Transaction {self.transaction_type} {self.amount} {self.gold_id}>'
