from simplesaleapp import csdl, app, utils
from simplesaleapp.models import LoaiSanPham, SanPham, TheSanPham, NguoiDung, VaiTroNguoiDung
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose, Admin, AdminIndexView
from flask_login import logout_user, current_user
from flask import redirect


class DaXacThucModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated\
               and current_user.vai_tro_nguoi_dung == VaiTroNguoiDung.QUANTRIVIEN


class SanPhamView(DaXacThucModelView):
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


class DaXacThucBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class DangXuatView(DaXacThucBaseView):
    @expose('/')
    def index(self):
        logout_user()

        return redirect('/admin')


class ThongKeBaoCaoView(DaXacThucBaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


class AdminIndexViewCuaToi(AdminIndexView):
    @expose('/')
    def index(self):
        thong_ke_bao_cao = utils.dem_san_pham_theo_danh_muc()
        return self.render('admin/index.html',
                           thong_ke_bao_cao=thong_ke_bao_cao)


admin = Admin(app=app,
              name='QUẢN TRỊ BÁN HÀNG ONLINE',
              template_mode='bootstrap4',
              index_view=AdminIndexViewCuaToi())
admin.add_view(DaXacThucModelView(LoaiSanPham,
                                  csdl.session,
                                  name='Danh mục'))
admin.add_view(SanPhamView(SanPham,
                           csdl.session,
                           name='Sản phẩm'))
admin.add_view(DaXacThucModelView(TheSanPham,
                                  csdl.session,
                                  name='Nhãn'))
admin.add_view(DaXacThucModelView(NguoiDung,
                                  csdl.session,
                                  name='Người dùng'))
admin.add_view(ThongKeBaoCaoView(name='Thống kê báo cáo'))
admin.add_view(DangXuatView(name='Đăng xuất'))
