# Nơi để truy cấp dữ liệu (giống DAO)

from simplesaleapp.models import NguoiDung
import hashlib

def lay_nguoi_dung_theo_id(id_nguoi_dung):
    return NguoiDung.query.get(id_nguoi_dung)


def kiem_tra_dang_nhap(ten_dang_nhap, mat_khau_dang_nhap):
    if ten_dang_nhap and mat_khau_dang_nhap:
        mat_khau_dang_nhap =\
            str(hashlib.md5(mat_khau_dang_nhap.strip().encode('utf-8')).hexdigest())

        return NguoiDung.query.filter(NguoiDung.ten_tai_khoan.__eq__(ten_dang_nhap.strip()),
                                      NguoiDung.mat_khau_tai_khoan.__eq__(mat_khau_dang_nhap)).first()

    return None
