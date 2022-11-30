# TugasBesarIF3152_K02_G06
Tugas besar RPL STI Kelompok K02-G06 1-2022/2023

## Penjelasan Umum:
Cinemanage adalah sebuah P/L desktop yang berfungsi sebagai media pencatatan dan pemesanan tiket bioskop oleh kasir. Perangkat lunak Cinemanage dikembangkan dengan tujuan untuk:
1. Menyediakan perangkat lunak untuk kasir dapat pemesanan tiket bioskop.
2. Membantu pencatatan admin dengan menampilkan riwayat pembelian tiket bioskop.


## Cara menjalankan:

## Daftar modul:

## Daftar tabel basis data:
## Basis data:
cineManage.db

| Film:       |
| ----------- |
| FilmID      |
| Title       |
| Duration    |
| Description |
| Poster      |
       
| Screening:  |
| ----------- |
| ScreeningID |
| StudioID    |
| FilmTitle   |
| StartTime   |
| EndTime     |
| Date        |

| Studio:  |
| ---------|
| StudioID |
| Name     |
| Capacity |

| Ticket: 	|
| ------------- |
| SeatID	|
| StudioID	|
| ScreeningID	|
| OrderDatetime |

| User:    |
| ---------|
| UserID   |
| Password |
| Role     |
