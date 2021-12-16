from  sqlalchemy import Column, Integer, String
from saleapp import csdl

class LoaiSanPham(csdl.Model):
    id = Column(Integer, primary_key=True,
                autoincrement=True)
    ten = Column(String(20), nullable=False)


if __name__ == '__main__':
    csdl.create_all()
