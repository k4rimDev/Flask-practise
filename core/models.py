from extensions import db


class Product():
    ...


class Comments(db.Model):
    
    __tablename__ = "ContactUs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    message = db.Column(db.Text, nullable=False)
    product_id = 5
    user_id = 3

    def __init__(self, name, phone, message):
        self.name = name
        self.phone = phone
        self.message = message
    
    def save(self):
        db.session.add(self)
        db.session.commit()
