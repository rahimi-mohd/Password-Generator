from app import db

class PasswordDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plain_password = db.Column(db.String(128))
    save_for = db.Column(db.String(128))

    def __repr__(self):
        return f"{self.id}\t{self.plain_password}\t{self.save_for}"