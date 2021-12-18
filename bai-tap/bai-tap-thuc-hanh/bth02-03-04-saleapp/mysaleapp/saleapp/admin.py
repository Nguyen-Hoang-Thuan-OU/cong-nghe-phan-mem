from saleapp import admin, db
from saleapp.models import Category, Product
from flask_admin.contrib.sqla import ModelView


class ProductView(ModelView):
    column_filters = ['name', 'price', 'category']
    column_searchable_list = ['name']
    can_export = True


admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
