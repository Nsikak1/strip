from app import db

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(2000), index=True, unique=True)
    trimmed_url = db.Column(db.String(50), index=True, unique=True)
    stats = db.Column(db.String(128))

    def __repr__(self):
        return '<Url = {}>'.format(self.long_url)    