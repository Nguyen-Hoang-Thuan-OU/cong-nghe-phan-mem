from  sqlalchemy import Column, Integer, String, Boolean, Float, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from simplesaleapp import csdl
from datetime import datetime
from enum import Enum as NguoiDungEnum
from flask_login import UserMixin

class VaiTroNguoiDung(NguoiDungEnum):
    QUANTRIVIEN = 1
    NGUOIDUNG = 2

# Đa kế thừa
class NguoiDung(csdl.Model, UserMixin):
    id = Column(Integer, primary_key=True,
                autoincrement=True)
    ten_nguoi_dung = Column(String(50), nullable=False)
    ten_tai_khoan = Column(String(50),
                           nullable=False,
                           unique=True)
    mat_khau_tai_khoan = Column(String(50),
                           nullable=False)
    trang_thai_hoat_dong = Column(Boolean,
                                  default=True)
    ngay_dang_ky_tai_khoan = Column(DateTime,
                                    default=datetime.now())
    anh_dai_dien = Column(String(100))
    vai_tro_nguoi_dung = Column(Enum(VaiTroNguoiDung),
                                default=VaiTroNguoiDung.NGUOIDUNG)

    def __str__(self):
        return self.ten_nguoi_dung


class LoaiSanPham(csdl.Model):
    id = Column(Integer, primary_key=True,
                autoincrement=True)
    ten_loai_san_pham = Column(String(20), nullable=False)
    cac_san_pham = relationship('SanPham',
                                backref='loai_san_pham',
                                lazy=True)

    def __str__(self):
        return self.ten_loai_san_pham


the_sanpham = csdl.Table('the_sanpham',
                         Column('id_san_pham',
                                Integer,
                                ForeignKey('san_pham.id'),
                                primary_key=True),
                         Column('id_the_san_pham',
                                Integer,
                                ForeignKey('the_san_pham.id'),
                                primary_key=True))


class SanPham(csdl.Model):
    __tablename__ = 'san_pham'
    id = Column(Integer, primary_key=True,
                autoincrement=True)
    ten_san_pham = Column(String(50), nullable=False)
    mo_ta_chi_tiet_san_pham = Column(String(255), nullable=True)
    gia_tien = Column(Float, default=0)
    kich_hoat = Column(Boolean, default=True)
    hinh_anh_san_pham = Column(String(100), nullable=True)
    ngay_tao_san_pham = Column(DateTime, default=datetime.now())
    id_loai_san_pham = Column(Integer,
                              ForeignKey(LoaiSanPham.id),
                              nullable=False)
    cac_the_san_pham = relationship('TheSanPham',
                                    secondary='the_sanpham',
                                    lazy='subquery',
                                    backref=backref('cac_san_pham', lazy=True))


class TheSanPham(csdl.Model):
    __tablename__ = 'the_san_pham'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ten_the = Column(String(50), nullable=False, unique=True)

    def __str__(self):
        return self.ten_the


if __name__ == '__main__':
    csdl.create_all()

    # Tạo sản phẩm
    # sp1 = SanPham(ten_san_pham="iPhone 7 Plus",
    #               mo_ta_chi_tiet_san_pham='Apple, 32GB',
    #               gia_tien=12,
    #               id_loai_san_pham=1)
    #
    # sp2 = SanPham(ten_san_pham="iPhone 13 Pro Max",
    #               mo_ta_chi_tiet_san_pham='Apple, 128GB',
    #               gia_tien=34,
    #               id_loai_san_pham=1)
    #
    # sp3 = SanPham(ten_san_pham="iPad Pro 2021",
    #               mo_ta_chi_tiet_san_pham='Apple, 64GB',
    #               gia_tien=26,
    #               id_loai_san_pham=2)
    #
    # sp4 = SanPham(ten_san_pham="Galaxy Tab S7 Plus",
    #               mo_ta_chi_tiet_san_pham='Samsung, 128GB',
    #               gia_tien=12,
    #               id_loai_san_pham=2)
    #
    # csdl.session.add(sp1)
    # csdl.session.add(sp2)
    # csdl.session.add(sp3)
    # csdl.session.add(sp4)
    #
    # csdl.session.commit()

    # Tạo thẻ sản phẩm
    # th1 = TheSanPham(ten_the='khuyenmai')
    # th2 = TheSanPham(ten_the='moi')
    #
    # csdl.session.add(th1)
    # csdl.session.add(th2)
    #
    # csdl.session.commit()
