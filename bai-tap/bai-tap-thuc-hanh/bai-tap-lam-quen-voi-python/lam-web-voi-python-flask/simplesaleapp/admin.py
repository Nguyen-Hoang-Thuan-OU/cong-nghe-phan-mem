from simplesaleapp import admin, csdl
from simplesaleapp.models import LoaiSanPham, SanPham, TheSanPham
from flask_admin.contrib.sqla import ModelView


class SanPhamView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_exclude_list = ['hinh_anh_san_pham']
    column_filters = ['ten_san_pham', 'gia_tien']
    column_searchable_list = ['ten_san_pham', 'mo_ta_chi_tiet_san_pham']
    column_labels = {
        'id': 'Mã sản phẩm',
        'ten_san_pham': 'Tên sản phẩm',
        'mo_ta_chi_tiet_san_pham': 'Mô tả chi tiết sản phẩm',
        'gia_tien': 'Giá bán',
        'kich_hoat': 'Đang kinh doanh',
        'hinh_anh_san_pham': 'Hình ảnh minh hoạ',
        'ngay_tao_san_pham': 'Ngày nhập kho',
        'loai_san_pham': 'Danh mục sản phẩm',
    }
    form_excluded_columns = ['cac_the_san_pham']

admin.add_view(ModelView(LoaiSanPham,
                         csdl.session,
                         name='Danh mục'))
admin.add_view(SanPhamView(SanPham,
                           csdl.session,
                           name='Sản phẩm'))
admin.add_view(ModelView(TheSanPham,
                         csdl.session,
                         name='Nhãn'))
