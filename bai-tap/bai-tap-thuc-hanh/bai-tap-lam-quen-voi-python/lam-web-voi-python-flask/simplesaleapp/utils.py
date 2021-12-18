# Nơi để truy cấp dữ liệu (giống DAO)

from simplesaleapp.models import NguoiDung, LoaiSanPham, SanPham
from sqlalchemy import func
from simplesaleapp import csdl
import hashlib


def lay_nguoi_dung_theo_id(id_nguoi_dung):
    return NguoiDung.query.get(id_nguoi_dung)


def kiem_tra_dang_nhap(ten_dang_nhap, mat_khau_dang_nhap):
    if ten_dang_nhap and mat_khau_dang_nhap:
        mat_khau_dang_nhap = \
            str(hashlib.md5(mat_khau_dang_nhap.strip().encode('utf-8')).hexdigest())

        return NguoiDung.query.filter(NguoiDung.ten_tai_khoan.__eq__(ten_dang_nhap.strip()),
                                      NguoiDung.mat_khau_tai_khoan.__eq__(mat_khau_dang_nhap)).first()

    return None


def dem_san_pham_theo_danh_muc():
    return LoaiSanPham.query.join(SanPham,
                                  SanPham.id_loai_san_pham.__eq__(LoaiSanPham.id),
                                  isouter=True) \
        .add_columns(func.count(SanPham.id)) \
        .group_by(LoaiSanPham.id) \
        .all()
