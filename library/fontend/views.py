#in the views.py  inside the website folder
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import SinhVien, Sach, MuonTraSach, NhanVien
from . import db
from sqlalchemy import or_
from .form import SearchForm
from sqlalchemy import func
from datetime import datetime
from sqlalchemy import desc
#Blueprint: have a lot of routes (URLs)
views = Blueprint('views', __name__)




@views.route('/')
def home():
	return render_template("home.html",sinhVien=current_user)
@views.route('/404')
def error_404():
    return render_template('404.html'), 404
    
@views.route("/student_info/<int:MSSV>")
@login_required
def student_info(MSSV):
    sinhVien = SinhVien.query.filter_by(MSSV=MSSV).first()

    if not sinhVien:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))

    return render_template("qlythongtinsv.html", sinhVien=current_user, MSSV=MSSV)
@views.route("/timkiem/<int:MSSV>",methods = ['GET','POST'])
@login_required
def search(MSSV):
    sinhVien = SinhVien.query.filter_by(MSSV=MSSV).first()
    books=Sach.query
    if not sinhVien:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))
    
#      form = SearchForm()
#     search = form.search.data
#     if form.validate_on_submit():
#         search = form.search.data
#         # print(search)
#     books = Sach.query.filter(or_(Sach.TenSach.ilike(f'%{search}%'), Sach.TenTacGia.ilike(f'%{search}%'),Sach.MaNXB.ilike(f'%{search}%'),Sach.SoLuongConLai.ilike(f'%{search}%'))).all()
#     if books: 
#         # sort = request.args.get('sort')
#         # print(sort, books ==True)   
#         # if request.method == 'POST':
#         #     search = form.data['search']
#         #     print(search, sort)
#         #     if sort == 'MaSach':
#         #         books = Sach.query.filter(or_(Sach.TenSach.ilike(f'%{search}%'), Sach.TenTacGia.ilike(f'%{search}%'),
#         #         Sach.MaNXB.ilike(f'%{search}%'),Sach.SoLuongConLai.ilike(f'%{search}%'))).order_by(Sach.MaSach.asc()).all()
#         #     if sort == 'TenSach':
#         #         books = Sach.query.filter(or_(Sach.TenSach.ilike(f'%{search}%'), Sach.TenTacGia.ilike(f'%{search}%'),Sach.MaNXB.ilike(f'%{search}%'),
#         #         Sach.SoLuongConLai.ilike(f'%{search}%'))).order_by(Sach.TenSach.asc()).all()
#         #     if sort == 'TenTacGia':
#         #         books = Sach.query.filter(or_(Sach.TenSach.ilike(f'%{search}%'), Sach.TenTacGia.ilike(f'%{search}%'),Sach.MaNXB.ilike(f'%{search}%'),
#         #         Sach.SoLuongConLai.ilike(f'%{search}%'))).order_by(Sach.TenTacGia.asc()).all()
#         #     if sort == 'MaNXB':
#         #         books = Sach.query.filter(or_(Sach.TenSach.ilike(f'%{search}%'), Sach.TenTacGia.ilike(f'%{search}%'),Sach.MaNXB.ilike(f'%{search}%'),
#         #         Sach.SoLuongConLai.ilike(f'%{search}%'))).order_by(Sach.MaNXB.asc()).all()
#         #     if sort == 'SoLuongConLai':
#         #         books = Sach.query.filter(or_(Sach.TenSach.ilike(f'%{search}%'), Sach.TenTacGia.ilike(f'%{search}%'),Sach.MaNXB.ilike(f'%{search}%'),
#         #         Sach.SoLuongConLai.ilike(f'%{search}%'))).order_by(Sach.SoLuongConLai).all()
#         #     return render_template("timkiem.html", sinhVien=current_user, MSSV=MSSV, books = books, length = len(books), form=form, sort=sort, search=search) """
        # return render_template("timkiem.html", sinhVien=current_user, MSSV=MSSV, books = books, length = len(books))
    return render_template("timkiem.html", sinhVien=current_user, MSSV=MSSV, books = books)

@views.route("/student_borrow/<int:MSSV>", methods=['GET', 'POST'])
@login_required
def student_borrow(MSSV):
    sinhVien = SinhVien.query.filter_by(MSSV=MSSV).first()

    if not sinhVien:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))
    books = db.session.query(MuonTraSach,Sach).filter(
        sinhVien.MSSV == MuonTraSach.MSSV,
        MuonTraSach.MaSach==Sach.MaSach).all()

    if books :
        sort = request.args.get('sort')
        # print(sort)
        if sort == 'MaSach':
            books = db.session.query(MuonTraSach,Sach).filter(
        sinhVien.MSSV == MuonTraSach.MSSV,
        MuonTraSach.MaSach==Sach.MaSach).order_by(MuonTraSach.MaSach.asc()).all()
        if sort == 'TenSach':
            books = db.session.query(MuonTraSach,Sach).filter(
        sinhVien.MSSV == MuonTraSach.MSSV,
        MuonTraSach.MaSach==Sach.MaSach).order_by(Sach.TenSach.asc()).all()
        if sort == 'ThoiHanMuon':
            books = db.session.query(MuonTraSach,Sach).filter(
        sinhVien.MSSV == MuonTraSach.MSSV,
        MuonTraSach.MaSach==Sach.MaSach).order_by(MuonTraSach.ThoiHanMuon).all()
        if sort == 'NgayTraSach':
            books = db.session.query(MuonTraSach,Sach).filter(
        sinhVien.MSSV == MuonTraSach.MSSV,
        MuonTraSach.MaSach==Sach.MaSach).order_by((MuonTraSach.NgayTraSach).asc()).all()
        if sort == 'TinhTrang':
            books = db.session.query(MuonTraSach,Sach).filter(
        sinhVien.MSSV == MuonTraSach.MSSV,
        MuonTraSach.MaSach==Sach.MaSach).order_by(MuonTraSach.TinhTrang).all()
    # print(books)
    # books = MuonTraSach.query.filter_by(MSSV=MSSV).all()
    # sach= Sach.query.filter_by(books.MaSach).all()
    return render_template("qlymuontra.html", sinhVien=current_user, MSSV=MSSV, books = books, length = len(books),sort=sort)


#---------------------------------------NHAN VIEN -------------------------------------------
@views.route("/staff_info/<int:MSNV>")
@login_required
def staff_info(MSNV):
    nhanVien = NhanVien.query.filter_by(MSNV=MSNV).first()

    if not nhanVien:
        flash('No user with that username exists. ', category='error')
        return redirect(url_for('views.home'))

    return render_template("qlythongtinnv.html", nhanVien=current_user, MSNV=MSNV)