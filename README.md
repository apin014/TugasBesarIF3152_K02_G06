# TugasBesarIF3152_K02_G06
Tugas besar RPL STI Kelompok 6 Kelas 02 1-2022/2023

Penjelasan:
CineManage adalah sebuah aplikasi yang digunakan untuk mengelola berbagai kebutuhan pada cinema atau bioskop.

Cara menjalankan:

Daftar modul:

Daftar tabel basis data:
Basis data: cineManage.db

Film:
	FilmID
	Title
	Duration
	Description
	Poster
       
Screening:
	ScreeningID
	StudioID
	FilmTitle
	StartTime
	EndTime
	Date
  
Seat:
	SeatID
	StudioID
	ScreeningReserved
       
Studio:
	StudioID
	Name
	Capacity
     
Ticket:
	SeatID
	StudioID
	ScreeningID
	OrderDatetime
     
User:
	UserID
	Password
	Role



