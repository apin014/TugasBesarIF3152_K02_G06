import time

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

import sys


class MainMenuCashier(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)

        self.login = None

        # Top Bar

        whiteBar = QLabel(self)
        pixmapWhiteBar = QPixmap('../img/top_white_bar.png')
        whiteBar.setPixmap(pixmapWhiteBar)
        whiteBar.move(0, 0)

        profile = QLabel(self)
        pixmapProfile = QPixmap('../img/profile.png')
        profile.setPixmap(pixmapProfile)
        profile.setStyleSheet("background: #FFFFFF")
        profile.move(30, 20)

        buttonLogout = QPushButton("Logout", self)
        buttonLogout.setProperty("class", "button")
        buttonLogout.clicked.connect(self.logout)
        buttonLogout.move(1120, 30)

        labelLoggedIn = QLabel("You're logged in as", self)
        labelLoggedIn.setProperty("class", "normal")
        labelLoggedIn.setStyleSheet("font-weight: 700")
        labelLoggedIn.move(110, 20)

        buttonUser = QPushButton("Cashier", self)
        buttonUser.setProperty("class", "button")
        buttonUser.setStyleSheet("background: #F04D4D")
        buttonUser.move(110, 45)

        # Middle

        cmmain = QLabel(self)
        pixmapCmmain = QPixmap('../img/cmmain.png')
        cmmain.setPixmap(pixmapCmmain)
        cmmain.move(470, 140)

        buttonPesanTiket = QPushButton("Pesan Tiket", self)
        buttonPesanTiket.setProperty("class", "option")
        # buttonPesanTiket.clicked.connect()
        buttonPesanTiket.move(430, 300)

        buttonRincianPenayangan = QPushButton("Rincian Penayangan", self)
        buttonRincianPenayangan.setProperty("class", "option")
        # buttonRincianPenayangan.clicked.connect()
        buttonRincianPenayangan.move(430, 410)

        buttonRiwayatPemesanan = QPushButton("Riwayat Pemesanan", self)
        buttonRiwayatPemesanan.setProperty("class", "option")
        # buttonRiwayatPemesanan.clicked.connect()
        buttonRiwayatPemesanan.move(430, 520)

    def logout(self):
        time.sleep(1)
        self.login = LoginWindow()
        self.login.show()
        self.close()

class MainMenuAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)

        self.login = None

        # Top Bar

        whiteBar = QLabel(self)
        pixmapWhiteBar = QPixmap('../img/top_white_bar.png')
        whiteBar.setPixmap(pixmapWhiteBar)
        whiteBar.move(0, 0)

        profile = QLabel(self)
        pixmapProfile = QPixmap('../img/profile.png')
        profile.setPixmap(pixmapProfile)
        profile.setStyleSheet("background: #FFFFFF")
        profile.move(30, 20)

        buttonLogout = QPushButton("Logout", self)
        buttonLogout.setProperty("class", "button")
        buttonLogout.clicked.connect(self.logout)
        buttonLogout.move(1120, 30)

        labelLoggedIn = QLabel("You're logged in as", self)
        labelLoggedIn.setProperty("class", "normal")
        labelLoggedIn.setStyleSheet("font-weight: 700")
        labelLoggedIn.move(110, 20)

        buttonUser = QPushButton("Admin", self)
        buttonUser.setProperty("class", "button")
        buttonUser.setStyleSheet("background: #F04D4D")
        buttonUser.move(110, 45)

        # Middle

        cmmain = QLabel(self)
        pixmapCmmain = QPixmap('../img/cmmain.png')
        cmmain.setPixmap(pixmapCmmain)
        cmmain.move(470, 140)

        buttonEditJadwalFilm = QPushButton("Edit Jadwal Film", self)
        buttonEditJadwalFilm.setProperty("class", "option")
        # buttonEditJadwalFilm.clicked.connect()
        buttonEditJadwalFilm.move(430, 280)

        buttonSetPassword = QPushButton("Set Password", self)
        buttonSetPassword.setProperty("class", "option")
        # buttonRincianPenayangan.clicked.connect()
        buttonSetPassword.move(430, 380)

        buttonRiwayatPemesanan = QPushButton("Riwayat Pemesanan", self)
        buttonRiwayatPemesanan.setProperty("class", "option")
        # buttonRiwayatPemesanan.clicked.connect()
        buttonRiwayatPemesanan.move(430, 490)

        buttonEditStudio = QPushButton("Edit Studio", self)
        buttonEditStudio.setProperty("class", "option")
        # buttonEditStudio.clicked.connect()
        buttonEditStudio.move(430, 600)

    def logout(self):
        time.sleep(1)
        self.login = LoginWindow()
        self.login.show()
        self.close()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - Login")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.setFocus()
        self.mainMenu = None

        logo = QLabel(self)
        pixmapLogo = QPixmap('../img/cmlogin.png')
        logo.setPixmap(pixmapLogo)
        logo.move(29, 200)

        rect = QLabel(self)
        pixmapRect = QPixmap('../img/login_background.png')
        rect.setPixmap(pixmapRect)
        rect.move(870, 173)

        labelWelcome = QLabel("Welcome!", self)
        labelWelcome.setProperty("class", "heading")
        labelWelcome.move(890, 200)

        labelPass = QLabel("Password", self)
        labelPass.setProperty("class", "normal")
        labelPass.move(890, 330)

        inputPass = QLineEdit(self)
        inputPass.setFixedSize(297, 38)
        inputPass.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputPass.setPlaceholderText("Input Password")
        inputPass.setEchoMode(QLineEdit.EchoMode.Password)
        inputPass.move(890, 360)

        buttonLogin = QPushButton("Login", self)
        buttonLogin.setProperty("class", "button")
        buttonLogin.clicked.connect(lambda: self.checkCredential(inputPass.text()))
        buttonLogin.move(980, 420)

        self.connectToDB()

    def connectToDB(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./cineManage.db')

        if not db.open():
            print("CONNECTION FAILED")
        else:
            print("CONNECTED TO DB SUCCESSFULLY")

    def checkCredential(self, password):
        print("PASSWORD: " + password)
        query = QSqlQuery()
        query.prepare('SELECT * FROM user WHERE password=:pass')
        query.bindValue(':pass', password)
        query.exec()

        if query.first():
            if query.value('password') == password:
                if query.value('role') == "Cashier":
                    time.sleep(1)
                    self.mainMenu = MainMenuCashier()
                    self.mainMenu.show()
                    self.close()
                    print('LOGIN SUCCESS')
                elif query.value('role') == "Admin":
                    time.sleep(1)
                    self.mainMenu = MainMenuAdmin()
                    self.mainMenu.show()
                    self.close()
                    print('LOGIN SUCCESS')
        else:
            print("PASSWORD NOT FOUND")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            position: relative;
            width: 1440px;
            height: 1024px;
            background: #FFDE59;
        }

        .heading {
            width: 230px;
            height: 105px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 64px;
            line-height: 71px;

            text-align: right;
            letter-spacing: -0.02em;

            color: #000000;
            background: #FFFFFF;
        }

        .normal {
            width: 89px;
            height: 18px;

            font-family: 'Roboto';
            font-style: normal;
            font-weight: 400;
            font-size: 20px;
            line-height: 18px;

            color: #000000;
            background: #FFFFFF;
        }

        .button{
            width: 124px;
            height: 44px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 20px;
            line-height: 87.69%;

            color: #FFFFFF;
            background: #3084D1;
            border-radius: 20px;
        }

        .button:hover{
            background: #112F49;
        }

        .option{
            width: 420px;
            height: 90px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 30px;
            line-height: 87.69%;
            /* identical to box height, or 32px */

            letter-spacing: 0.05em;

            color: #000000;

            background: #FFFFFF;
            border-radius: 20px;
        }

        .option:hover{
            background: #3084D1;
            color: #FFFFFF;
        }

        ''')

    mainApp = LoginWindow()
    mainApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
