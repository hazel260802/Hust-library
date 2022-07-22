-------------------------------------------- BORROW FUNCTION ------------------------------------------
SELECT MuonTraSach.MaSach, Sach.TenSach, MuonTraSach.NgayMuon, 
MuonTraSach.NgayMuon, MuonTraSach.ThoiHanMuon, MuonTraSach.NgayTraSach, MuonTraSach.TinhTrang 
FROM MuonTraSach JOIN Sach 
ON MuonTraSach.MaSach = Sach.MaSach
WHERE MuonTraSach.MSSV = '20205319'
ORDER by MuonTraSach.MaSach ASC
---------------------------------------------------
SELECT MuonTraSach.MaSach, Sach.TenSach, MuonTraSach.NgayMuon, 
MuonTraSach.NgayMuon, MuonTraSach.ThoiHanMuon, MuonTraSach.NgayTraSach, MuonTraSach.TinhTrang 
FROM MuonTraSach JOIN Sach 
ON MuonTraSach.MaSach = Sach.MaSach
WHERE MuonTraSach.MSSV = '20205319'
ORDER by Sach.TenSach ASC
------------------------------------------------
SELECT MuonTraSach.MaSach, Sach.TenSach, MuonTraSach.NgayMuon, 
MuonTraSach.NgayMuon, MuonTraSach.ThoiHanMuon, MuonTraSach.NgayTraSach, MuonTraSach.TinhTrang 
FROM MuonTraSach JOIN Sach 
ON MuonTraSach.MaSach = Sach.MaSach
WHERE MuonTraSach.MSSV = '20205319'
ORDER by MuonTraSach.ThoiHanMuon ASC
------------------------------------------------
SELECT MuonTraSach.MaSach, Sach.TenSach, MuonTraSach.NgayMuon, 
MuonTraSach.NgayMuon, MuonTraSach.ThoiHanMuon, MuonTraSach.NgayTraSach, MuonTraSach.TinhTrang 
FROM MuonTraSach JOIN Sach 
ON MuonTraSach.MaSach = Sach.MaSach
WHERE MuonTraSach.MSSV = '20205319'
ORDER by MuonTraSach.NgayTraSach ASC
-------------------------------------------- SEARCH FUNCTION ------------------------------------------

------------------- Theo Tên sách ----------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
-------------------- Sap xep theo ma sach ------------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
ORDER BY MaSach ASC

SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
ORDER BY MaSach DESC

-------------------- Sap xep theo ten sach ------------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
ORDER BY TenSach ASC

SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
ORDER BY TenSach DESC

-------------------- Sap xep theo ten tac gia ------------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
ORDER BY TenTacGia ASC

SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
ORDER BY TenTacGia DESC

-------------------- Sap xep theo NXB ------------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
ORDER BY MaNXB ASC

SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
ORDER BY MaNXB DESC
-------------------- Sap xep theo so luong ------------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
ORDER BY SoLuongConLai ASC

SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenSach like '%The%'
ORDER BY SoLuongConLai DESC

------------------- Theo Tên tac gia ----------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'

-------------------- Sap xep theo ma sach ------------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'
ORDER BY MaSach ASC

SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'
ORDER BY MaSach DESC

-------------------- Sap xep theo ten sach ------------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'
ORDER BY TenSach ASC

SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'
ORDER BY TenSach DESC

-------------------- Sap xep theo ten tac gia ------------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'
ORDER BY TenTacGia ASC

SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'
ORDER BY TenTacGia DESC

-------------------- Sap xep theo NXB ------------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'
ORDER BY MaNXB ASC

SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'
ORDER BY MaNXB DESC
-------------------- Sap xep theo so luong ------------------------------------------------
SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'
ORDER BY SoLuongConLai ASC

SELECT MaSach, TenSach, TenTacGia, MaNXB, SoLuongConLai FROM Sach 
WHERE Sach.TenTacGia like '%Mac%'
ORDER BY SoLuongConLai DESC



