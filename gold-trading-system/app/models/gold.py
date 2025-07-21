from run import db

class Gold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    symbol = db.Column(db.String(10), index=True, unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<Gold {self.symbol}>'
