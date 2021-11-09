from db import db


class ItemModel(db.Model):
    __tablename__ = 'cakes'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float(precision=2))
    name = db.Column(db.String(80))
    comment = db.Column(db.String(80))
    imgUrl = db.Column(db.String(80))
    yum_factor = db.Column(db.Float(precision=2))

    def __init__(self, name, price, comment, imgUrl, yum_factor):
        self.name = name
        self.price = price
        self.comment = comment
        self.imgUrl = imgUrl
        self.yum_factor = yum_factor

    def json(self):
        return {'name': self.name, 'price': self.price, 'comment': self.comment, 'yum factor': self.yum_factor}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
