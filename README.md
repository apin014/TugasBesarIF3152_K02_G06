# TugasBesarIF3152_K02_G06
Tugas besar RPL STI Kelompok K02-G06 1-2022/2023

## Penjelasan Umum:
Cinemanage adalah sebuah P/L desktop yang berfungsi sebagai media pencatatan dan pemesanan tiket bioskop oleh kasir. Perangkat lunak Cinemanage dikembangkan dengan tujuan untuk:
1. Menyediakan perangkat lunak untuk kasir dapat pemesanan tiket bioskop.
2. Membantu pencatatan admin dengan menampilkan riwayat pembelian tiket bioskop.


## Cara menjalankan:
1. Login aplikasi sebagai Kasir/Admin
2. Apabila pengguna masih baru, lakukan set password
3. Sebagai Kasir, pengguna bisa memilih aksi antara memesan tiket, melihat rincian penayangan, dan riwayat pemesanan
4. Setelah memilih pemesanan tiket, pengguna akan dihadapkan dengan tampilan film-film yang sedang tampil saat jangka waktu itu, harga, serta pilihan jam tayangnya
5. Setelah memilih film dan jadwal yang sesuai, pengguna dapat memilih kursi yang berwarna hijau (belum dibeli)
6. Tampilan harga akan muncul sesuai dengan jumlah tiket yang dibeli, kemudian tekan lanjut
7. Pengguna akan dihadapkan dengan tampilan verifikasi pembayaran untuk melakukan final checking sebelum tiket dibeli. Informasinya berisi titik kursi yang dipilih, harga, nama customer, serta ID tiketnya
8. Sebagai Admin, pengguna bisa memilih aksi antara mengedit jadwal film, menentukan password, melihat riwayat pemesanan, dan mengedit studio
9. Setelah memilih rincian penayangan, pengguna akan dihadapkan dengan tampilan informasi berupa details dari film yang ditayangkan
10. Untuk riwayat pemesanan, pengguna dapat melihat history transaksi pembelian tiket
11. Untuk edit studio, pengguna dapat mengisi nama studio serta kapasitasnya
12. Untuk edit jadwal film, pengguna dapat mengisi nama judul film, studio, jam tayang, dan jadwal mulainya
13. Setelah selesai melakukan kegiatan di dalam aplikasi, pengguna dapat melakukan logout

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
