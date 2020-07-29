#from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from app.domains.car.exceptions import InvalidCarException
from sqlalchemy.orm import validates
from database import db, ma


class Car(db.Model):
    __tablename__ = 'car'

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    brand = db.Column(db.String(40), nullable=False)
    color = db.Column(db.String(40), nullable=False)
    ports = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'color': self.color,
            'ports': self.ports
        }

# class CarSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Car()

    @validates('brand')
    def validate_brand(self,key, brand):
        if not brand:
            raise InvalidCarException(msg='The brand is invalid')

        return brand
