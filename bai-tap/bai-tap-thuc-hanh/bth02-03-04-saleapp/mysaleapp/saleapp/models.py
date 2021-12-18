from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer,
                primary_key=True,
                autoincrement=True)


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product',
                            backref='category',
                            lazy=True)


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


if __name__ == '__main__':
    db.create_all()

    # c1 = Category(name='Mobile')
    # c2 = Category(name='Tablet')
    #
    # db.session.add(c1)
    # db.session.add(c2)
    #
    # db.session.commit()

    a = [{
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image": "images/iphone-7-plus-gold-400x460-400x460.png",
        "category_id": 1
    },
        {
            "id": 2,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "images/ipad-pro-12-9-inch-wifi-128gb-2020-xam-400x460-1-400x460.png",
            "category_id": 2
        },
        {
            "id": 3,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAM: 6GB",
            "price": 24000000,
            "image": "images/samsung-galaxy-note-10-lite-chi-tiet-1-400x460.png",
            "category_id": 1
        }
    ]

    for x in a:
        p = Product(name=x['name'],
                    description=x['description'],
                    image=x['image'],
                    price=x['price'],
                    category_id=x['category_id'])
        db.session.add(p)

    db.session.commit()
