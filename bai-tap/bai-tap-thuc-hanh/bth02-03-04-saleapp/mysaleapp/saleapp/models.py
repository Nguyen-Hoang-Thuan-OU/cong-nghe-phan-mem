from sqlalchemy import Column,\
    Integer, String, Float, Enum,\
    DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db
from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer,
                primary_key=True,
                autoincrement=True)


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2


class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False,
                      unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(255))
    email = Column(String(50))
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime,
                         default=datetime.now())
    user_role = Column(Enum(UserRole),
                       default=UserRole.USER)

    def __str__(self):
        return self.name


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product',
                            backref='category',
                            lazy=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    image = Column(String(100))
    category_id = Column(Integer,
                         ForeignKey(Category.id),
                         nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    db.create_all()

    # c1 = Category(name='Mobile')
    # c2 = Category(name='Tablet')
    #
    # db.session.add(c1)
    # db.session.add(c2)
    #
    # db.session.commit()

    # a = [{
    #     "id": 1,
    #     "name": "iPhone 7 Plus",
    #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
    #     "price": 17000000,
    #     "image": "images/iphone-7-plus-32gb-gold-600x600-600x600.jpg",
    #     "category_id": 1
    # },
    #     {
    #         "id": 2,
    #         "name": "iPad Pro 2020",
    #         "description": "Apple, 128GB, RAM: 6GB",
    #         "price": 37000000,
    #         "image": "images/ipad-pro-12-9-inch-wifi-128gb-2020-xam-400x460-1-400x460.png",
    #         "category_id": 2
    #     },
    #     {
    #         "id": 3,
    #         "name": "Galaxy Note 10 Plus",
    #         "description": "Samsung, 64GB, RAM: 6GB",
    #         "price": 24000000,
    #         "image": "images/samsung-galaxy-note-10-lite-chi-tiet-1-400x460.png",
    #         "category_id": 1
    #     }
    # ]
    #
    # for x in a:
    #     p = Product(name=x['name'],
    #                 description=x['description'],
    #                 image=x['image'],
    #                 price=x['price'],
    #                 category_id=x['category_id'])
    #     db.session.add(p)
    #
    # db.session.commit()
