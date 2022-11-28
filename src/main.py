import time

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

import sys
import os
import math
import datetime

current_dir = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(current_dir, "cineManage_V3.db")

class MainMenuAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)

        self.nextMenu = None

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        # Middle
        cmmain = QLabel(self)
        pixmapCmmain = QPixmap('../img/cmmain.png')
        cmmain.setPixmap(pixmapCmmain)
        cmmain.move(470, 140)

        buttonEditJadwalFilm = QPushButton("Edit Film and Schedule", self)
        buttonEditJadwalFilm.setProperty("class", "option")
        buttonEditJadwalFilm.clicked.connect(self.editFilmAndSchedule)
        buttonEditJadwalFilm.move(430, 280)

        buttonSetPassword = QPushButton("Set Password", self)
        buttonSetPassword.setProperty("class", "option")
        buttonSetPassword.clicked.connect(self.setPassword)
        buttonSetPassword.move(430, 390)

        buttonOrderHistory = QPushButton("Order History", self)
        buttonOrderHistory.setProperty("class", "option")
        buttonOrderHistory.clicked.connect(self.orderHistory)
        buttonOrderHistory.move(430, 500)

        buttonEditStudio = QPushButton("Edit Studio", self)
        buttonEditStudio.setProperty("class", "option")
        buttonEditStudio.clicked.connect(self.editStudio)
        buttonEditStudio.move(430, 610)

        #Debug

        # buttonClearDebug = QPushButton("Debug", self)
        # buttonClearDebug.setProperty("class", "button")
        # buttonClearDebug.setStyleSheet("background: #7A7A7A;")
        # buttonClearDebug.move(980, 30)
        # buttonClearDebug.clicked.connect(self.debug)

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def editStudio(self):
        self.nextMenu = MenuListStudio(1)
        self.nextMenu.show()
        self.close()

    def setPassword(self):
        self.nextMenu = MenuSetPassword()
        self.nextMenu.show()
        self.close()

    def editFilmAndSchedule(self):
        self.nextMenu = MenuListFilm(1)
        self.nextMenu.show()
        self.close()

    def orderHistory(self):
        self.nextMenu = MenuListTicket(1)
        self.nextMenu.show()
        self.close()

class MenuSetPassword(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)

        self.nextMenu = None

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("Set Password", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(430, 20)

        #Middle

        rect = QLabel(self)
        pixmapRect = QPixmap('../img/login_background.png')
        rect.setPixmap(pixmapRect)
        rect.move(470, 173)

        labelPassword = QLabel("Password *", self)
        labelPassword.setProperty("class", "normal")
        labelPassword.setStyleSheet("font-weight: 700;")
        labelPassword.move(490, 200)

        inputPassword = QLineEdit(self)
        inputPassword.setFixedSize(297, 38)
        inputPassword.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputPassword.setPlaceholderText("Input Password...")
        inputPassword.move(490, 230)

        labelRePassword = QLabel("Retype Password *", self)
        labelRePassword.setProperty("class", "normal")
        labelRePassword.setStyleSheet("font-weight: 700;")
        labelRePassword.move(490, 300)

        inputRePassword = QLineEdit(self)
        inputRePassword.setFixedSize(297, 38)
        inputRePassword.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputRePassword.setPlaceholderText("Input Password...")
        inputRePassword.move(490, 330)

        labelRole = QLabel("Role *", self)
        labelRole.setProperty("class", "normal")
        labelRole.setStyleSheet("font-weight: 700;")
        labelRole.move(490, 400)

        inputRole = QLineEdit(self)
        inputRole.setFixedSize(297, 38)
        inputRole.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputRole.setPlaceholderText("Select the role below")
        inputRole.setReadOnly(True)
        inputRole.move(490, 430)

        buttonRoleAdmin = QPushButton("Admin", self)
        buttonRoleAdmin.setProperty("class", "btn-danger")
        buttonRoleAdmin.setStyleSheet("width: 135px; height: 30px; font-size: 16px")
        buttonRoleAdmin.move(490, 485)
        buttonRoleAdmin.clicked.connect(lambda: self.setRole(inputRole, "Admin"))

        buttonRoleCashier = QPushButton("Cashier", self)
        buttonRoleCashier.setProperty("class", "btn-success")
        buttonRoleCashier.setStyleSheet("width: 135px; height: 30px; font-size: 16px")
        buttonRoleCashier.move(651, 485)
        buttonRoleCashier.clicked.connect(lambda: self.setRole(inputRole, "Cashier"))

        buttonSubmit = QPushButton("Submit", self)
        buttonSubmit.setProperty("class", "button")
        buttonSubmit.move(577, 560)
        buttonSubmit.clicked.connect(lambda: self.setPassword(str(inputPassword.text()), str(inputRePassword.text()), str(inputRole.text())))

        buttonReturn = QPushButton("<< Main Menu", self)
        buttonReturn.setProperty("class", "option")
        buttonReturn.setStyleSheet("width: 200px; height: 44px; font-size: 20px;")
        buttonReturn.move(30, 660)
        buttonReturn.clicked.connect(lambda: self.returnToMainMenu())

        #Debug
        # db = QSqlDatabase.addDatabase('QSQLITE')
        # db.setDatabaseName(db_path)
        #
        # if not db.open():
        #     print("CONNECTION FAILED")
        # else:
        #     print("CONNECTED TO DB SUCCESSFULLY")

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def setRole(self, input, role):
        input.setText(role)

    def setPassword(self, password, rePassword, role):
        if (password == rePassword):
            query = QSqlQuery()
            query.prepare('UPDATE user SET password = :pass WHERE role = :role')
            query.bindValue(':pass', password)
            query.bindValue(':role', role)
            query.exec()
            query.finish()
            self.nextMenu = MainMenuAdmin()
            self.nextMenu.show()
            self.close()
        else:
            print("[ERROR]: Password wasn't typed correctly!")

    def returnToMainMenu(self):
        self.nextMenu = MainMenuAdmin()
        self.nextMenu.show()
        self.close()

class MenuAddStudio(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - Add New Studio")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.nextMenu = None

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("Add New Studio", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(430, 20)

        #Middle

        labelNamaStudio = QLabel("Studio Name *", self)
        labelNamaStudio.setProperty("class", "normal")
        labelNamaStudio.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelNamaStudio.move(350, 190)

        inputNamaStudio = QLineEdit(self)
        inputNamaStudio.setFixedSize(600, 38)
        inputNamaStudio.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputNamaStudio.setPlaceholderText("Input Studio Name (30 char max)")
        inputNamaStudio.setMaxLength(30)
        inputNamaStudio.move(350, 230)

        labelKapasitasStudio = QLabel("Studio Capacity *", self)
        labelKapasitasStudio.setProperty("class", "normal")
        labelKapasitasStudio.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelKapasitasStudio.move(350, 300)

        inputKapasitasStudio = QLineEdit(self)
        inputKapasitasStudio.setFixedSize(600, 38)
        inputKapasitasStudio.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputKapasitasStudio.setPlaceholderText("Insert 150 for Type 1 OR 300 for Type 2")
        inputKapasitasStudio.move(350, 340)

        buttonBatal = QPushButton("Batal", self)
        buttonBatal.setProperty("class", "btn-danger")
        buttonBatal.clicked.connect(lambda: self.returnToListStudio())
        buttonBatal.move(485, 620)

        buttonSimpan = QPushButton("Simpan", self)
        buttonSimpan.setProperty("class", "btn-success")
        buttonSimpan.clicked.connect(lambda: self.submitAddStudio(inputNamaStudio.text(), inputKapasitasStudio.text()))
        buttonSimpan.move(655, 620)

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def returnToListStudio(self):
        self.nextMenu = MenuListStudio(1)
        self.nextMenu.show()
        self.close()

    def submitAddStudio(self, name, capacity):
        if (name and capacity):
            query = QSqlQuery()
            query.prepare("INSERT INTO studio (Name, Capacity) VALUES (:name, :capacity)")
            query.bindValue(':name', name[:30])
            query.bindValue(':capacity', int(capacity))
            query.exec()

            self.nextMenu = MenuListStudio(1)
            self.nextMenu.show()
            self.close()

        else:
            print("Error required input not filled")

        # Debug
        # print(query.lastError().text())

class MenuAddFilm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - Add New Film")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.nextMenu = None

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("Add New Film", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(430, 20)

        labelNamaFilm = QLabel("Film Title *", self)
        labelNamaFilm.setProperty("class", "normal")
        labelNamaFilm.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelNamaFilm.move(350, 190)

        inputNamaFilm = QLineEdit(self)
        inputNamaFilm.setFixedSize(600, 38)
        inputNamaFilm.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputNamaFilm.setPlaceholderText("Input Film Title (30 char max)")
        inputNamaFilm.setMaxLength(30)
        inputNamaFilm.move(350, 230)

        labelDuration = QLabel("Film Duration *", self)
        labelDuration.setProperty("class", "normal")
        labelDuration.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelDuration.move(350, 300)

        inputDuration = QLineEdit(self)
        inputDuration.setFixedSize(600, 38)
        inputDuration.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputDuration.setPlaceholderText("Insert Film Duration in Minutes")
        inputDuration.setMaxLength(4)
        inputDuration.move(350, 340)

        labelDescription = QLabel("Film Description *", self)
        labelDescription.setProperty("class", "normal")
        labelDescription.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelDescription.move(350, 410)

        inputDescription = QLineEdit(self)
        inputDescription.setFixedSize(600, 38)
        inputDescription.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputDescription.setPlaceholderText("Insert Film Description")
        inputDescription.move(350, 450)

        labelPoster = QLabel("Film Poster *", self)
        labelPoster.setProperty("class", "normal")
        labelPoster.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelPoster.move(350, 520)

        inputPoster = QLineEdit(self)
        inputPoster.setFixedSize(600, 38)
        inputPoster.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputPoster.setPlaceholderText("Insert File Path to Film Poster")
        inputPoster.move(350, 560)

        buttonBatal = QPushButton("Batal", self)
        buttonBatal.setProperty("class", "btn-danger")
        buttonBatal.clicked.connect(lambda: self.returnToListFilm())
        buttonBatal.move(485, 620)

        buttonSimpan = QPushButton("Simpan", self)
        buttonSimpan.setProperty("class", "btn-success")
        buttonSimpan.clicked.connect(lambda: self.submitAddFilm(inputNamaFilm.text(), inputDuration.text(), inputDescription.text(), inputPoster.text()))
        buttonSimpan.move(655, 620)

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def returnToListFilm(self):
        self.nextMenu = MenuListFilm(1)
        self.nextMenu.show()
        self.close()

    def submitAddFilm(self, title, duration, description, poster):
        if(title and duration and description and poster):
            query = QSqlQuery()
            query.prepare("INSERT INTO film (Title, Duration, Description, Poster) VALUES (:title, :duration, :description, :poster)")
            query.bindValue(':title', title[:40])
            query.bindValue(':duration', int(duration))
            query.bindValue(':description', description)
            query.bindValue(':poster', poster)
            query.exec()

            self.nextMenu = MenuListFilm(1)
            self.nextMenu.show()
            self.close()

        else:
            print("Error required input not filled")

class MenuAddSchedule(QWidget):
    def __init__(self, filmId):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - Add Schedule")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.nextMenu = None

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("Add Schedule", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(450, 20)

        # Middle

        # Query Debug
        # db = QSqlDatabase.addDatabase('QSQLITE')
        # db.setDatabaseName(db_path)
        #
        # if not db.open():
        #     print("CONNECTION FAILED")
        # else:
        #     print("CONNECTED TO DB SUCCESSFULLY")

        query = QSqlQuery()
        query.prepare("SELECT * FROM film WHERE FilmID = :id")
        query.bindValue(':id', filmId)
        query.exec()

        filmName = ""
        filmDuration = 0

        if query.first():
            filmName = query.value(1)
            filmDuration = int(query.value(2))

        labelStudioId = QLabel("Studio ID *", self)
        labelStudioId.setProperty("class", "normal")
        labelStudioId.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelStudioId.move(350, 190)

        inputStudioId = QLineEdit(self)
        inputStudioId.setFixedSize(600, 38)
        inputStudioId.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputStudioId.setPlaceholderText("Input Studio ID...")
        inputStudioId.move(350, 230)

        labelNamaFilm = QLabel("Film Title *", self)
        labelNamaFilm.setProperty("class", "normal")
        labelNamaFilm.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelNamaFilm.move(350, 290)

        inputNamaFilm = QLineEdit(self)
        inputNamaFilm.setFixedSize(600, 38)
        inputNamaFilm.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputNamaFilm.setPlaceholderText("Input Film Title...")
        inputNamaFilm.setText(filmName)
        inputNamaFilm.move(350, 330)

        labelTanggal = QLabel("Date *", self)
        labelTanggal.setProperty("class", "normal")
        labelTanggal.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelTanggal.move(350, 400)

        inputTanggal = QLineEdit(self)
        inputTanggal.setFixedSize(600, 38)
        inputTanggal.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputTanggal.setPlaceholderText("Format (YYYY-MM-DD)")
        inputTanggal.setMaxLength(10)
        inputTanggal.move(350, 440)

        labelStartTime = QLabel("Start Time (XX:XX) *", self)
        labelStartTime.setProperty("class", "normal")
        labelStartTime.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelStartTime.move(350, 510)

        inputStartTimeHour = QLineEdit(self)
        inputStartTimeHour.setFixedSize(70, 38)
        inputStartTimeHour.setStyleSheet("background: #F5F5F5; padding-left: 25px; font-size: 16px;")
        inputStartTimeHour.setPlaceholderText("00")
        inputStartTimeHour.setText("00")
        inputStartTimeHour.setMaxLength(2)
        inputStartTimeHour.move(350, 550)

        inputStartTimeMinute = QLineEdit(self)
        inputStartTimeMinute.setFixedSize(70, 38)
        inputStartTimeMinute.setStyleSheet("background: #F5F5F5; padding-left: 25px; font-size: 16px;")
        inputStartTimeMinute.setPlaceholderText("00")
        inputStartTimeMinute.setText("00")
        inputStartTimeMinute.setMaxLength(2)
        inputStartTimeMinute.move(430, 550)

        buttonDuration = QPushButton("Generate End Time", self)
        buttonDuration.setProperty("class", "button")
        buttonDuration.setStyleSheet("width: 180px; height:30px; font-size:16px;")
        buttonDuration.move(565, 555)
        buttonDuration.clicked.connect(lambda: self.generateEndTime(inputStartTimeHour.text(), inputStartTimeMinute.text(), filmDuration, inputEndTimeHour, inputEndTimeMinute))

        labelEndTime = QLabel("End Time (XX:XX) *", self)
        labelEndTime.setProperty("class", "normal")
        labelEndTime.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelEndTime.move(770, 510)

        inputEndTimeHour = QLineEdit(self)
        inputEndTimeHour.setFixedSize(70, 38)
        inputEndTimeHour.setStyleSheet("background: #F5F5F5; padding-left: 25px; font-size: 16px;")
        inputEndTimeHour.move(800, 550)
        inputEndTimeHour.setReadOnly(True)

        inputEndTimeMinute = QLineEdit(self)
        inputEndTimeMinute.setFixedSize(70, 38)
        inputEndTimeMinute.setStyleSheet("background: #F5F5F5; padding-left: 25px; font-size: 16px;")
        inputEndTimeMinute.move(880, 550)
        inputEndTimeMinute.setReadOnly(True)

        buttonBatal = QPushButton("Batal", self)
        buttonBatal.setProperty("class", "btn-danger")
        buttonBatal.clicked.connect(lambda: self.returnToListFilm())
        buttonBatal.move(505, 620)

        buttonSimpan = QPushButton("Simpan", self)
        buttonSimpan.setProperty("class", "btn-success")
        buttonSimpan.clicked.connect(lambda: self.submitAddSchedule(inputStudioId.text(), inputNamaFilm.text(), inputStartTimeHour.text(), inputStartTimeMinute.text(), inputEndTimeHour.text(), inputEndTimeMinute.text(), inputTanggal.text()))
        buttonSimpan.move(675, 620)

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def returnToListFilm(self):
        self.nextMenu = MenuListFilm(1)
        self.nextMenu.show()
        self.close()

    def generateEndTime(self, startHour, startMinute, duration, endHour, endMinute):

        print("Duration = ")
        start = datetime.datetime(1,1,1,int(startHour) % 24,int(startMinute) % 60,0)
        end = start + datetime.timedelta(minutes=duration)
        print(str(end.time()))
        endHour.setText(str(end.time())[:2])
        endMinute.setText(str(end.time())[3:5])

    def submitAddSchedule(self, studioId, filmTitle, startHour, startMinute, endHour, endMinute, date):

        query = QSqlQuery()
        query.prepare("SELECT * FROM screening WHERE studioId = :id AND Date LIKE :date")
        query.bindValue(':id', studioId)
        query.bindValue(':date', date)
        query.exec()

        listStartTime = []
        listEndTime = []
        if query.first():
            listStartTime.append(query.value(3))
            listEndTime.append(query.value(4))
            while query.next():
                listStartTime.append(query.value(3))
                listEndTime.append(query.value(4))

        query.finish()



        if len(listStartTime) > 4:
            print("This Studio has reached max screening for this date")

        else:
            badSchedule = False
            for i in range(len(listStartTime)):
                if (((int(startHour) * 60 + int(startMinute)) >= int(str(listStartTime[i])[:2]) * 60 + int(str(listStartTime[i])[3:5])) and ((int(startHour) * 60 + int(startMinute) )< int(str(listEndTime[i])[:2]) * 60 + int(str(listEndTime[i])[3:5]))):
                    badSchedule = True

            if (badSchedule == False):
                if (studioId and filmTitle and startHour and startMinute and endHour and endMinute and date):
                    query = QSqlQuery()
                    query.prepare("INSERT INTO screening (StudioID, FilmTitle, StartTime, EndTime, Date) VALUES (:studio, :title, :start, :end, :date)")
                    query.bindValue(':studio', studioId)
                    query.bindValue(':title', filmTitle)
                    query.bindValue(':start', str(startHour) + ":" + str(startMinute))
                    query.bindValue(':end', str(endHour) + ":" + str(endMinute))
                    query.bindValue(':date', date)
                    query.exec()

                    self.nextMenu = MenuListSchedule(1)
                    self.nextMenu.show()
                    self.close()

                else:
                    print("Error required input not filled")
            else:
                print('This Schedule clashes with existing schedule for this studio')

class MenuEditStudio(QWidget):
    def __init__(self, studioId):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - Edit Studio")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.nextMenu = None

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("Edit Studio", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(480, 20)

        # Middle

        query = QSqlQuery()
        query.prepare("SELECT * FROM studio WHERE StudioID = :id")
        query.bindValue(':id', studioId)
        query.exec()

        studioName = ""
        studioCapacity = ""

        if query.first():
            studioName = query.value(1)
            studioCapacity = str(query.value(2))

        labelNamaStudio = QLabel("Studio Name *", self)
        labelNamaStudio.setProperty("class", "normal")
        labelNamaStudio.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelNamaStudio.move(350, 190)

        inputNamaStudio = QLineEdit(self)
        inputNamaStudio.setFixedSize(600, 38)
        inputNamaStudio.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputNamaStudio.setPlaceholderText("Input Studio Name (30 char max)")
        inputNamaStudio.setText(studioName)
        inputNamaStudio.setMaxLength(30)
        inputNamaStudio.move(350, 230)

        labelKapasitasStudio = QLabel("Studio Capacity *", self)
        labelKapasitasStudio.setProperty("class", "normal")
        labelKapasitasStudio.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelKapasitasStudio.move(350, 300)

        inputKapasitasStudio = QLineEdit(self)
        inputKapasitasStudio.setFixedSize(600, 38)
        inputKapasitasStudio.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputKapasitasStudio.setPlaceholderText("Insert 150 for Type 1 OR 300 for Type 2")
        inputKapasitasStudio.setText(studioCapacity)
        inputKapasitasStudio.move(350, 340)


        buttonBatal = QPushButton("Batal", self)
        buttonBatal.setProperty("class", "btn-danger")
        buttonBatal.clicked.connect(lambda: self.returnToListStudio())
        buttonBatal.move(485, 620)

        buttonSimpan = QPushButton("Simpan", self)
        buttonSimpan.setProperty("class", "btn-success")
        buttonSimpan.clicked.connect(lambda: self.submitEditStudio(inputNamaStudio.text(), inputKapasitasStudio.text(), studioId))
        buttonSimpan.move(655, 620)



    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def returnToListStudio(self):
        self.nextMenu = MenuListStudio(1)
        self.nextMenu.show()
        self.close()

    def submitEditStudio(self, name, capacity, studioId):
        if (name and capacity):
            query = QSqlQuery()
            query.prepare("UPDATE studio SET Name = :name, Capacity = :capacity WHERE StudioID = :id")
            query.bindValue(':name', name[:30])
            query.bindValue(':capacity', int(capacity))
            query.bindValue(':id', studioId)
            query.exec()

            self.nextMenu = MenuListStudio(1)
            self.nextMenu.show()
            self.close()

        else:
            print("Error required input not filled")

class MenuEditFilm(QWidget):
    def __init__(self, filmId):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - Edit Film")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.nextMenu = None

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("Edit Film", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(510, 20)

        # Middle

        query = QSqlQuery()
        query.prepare("SELECT * FROM film WHERE filmid = :id")
        query.bindValue(':id', filmId)
        query.exec()

        filmName = ""
        filmDuration = ""
        filmDescription = ""
        filmPoster = ""

        if query.first():
            filmName = query.value(1)
            filmDuration = str(query.value(2))
            filmDescription = query.value(3)
            filmPoster = query.value(4)

        labelNamaFilm = QLabel("Film Title *", self)
        labelNamaFilm.setProperty("class", "normal")
        labelNamaFilm.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelNamaFilm.move(350, 150)

        inputNamaFilm = QLineEdit(self)
        inputNamaFilm.setFixedSize(600, 38)
        inputNamaFilm.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputNamaFilm.setPlaceholderText("Input Film Title (30 char max)")
        inputNamaFilm.setText(filmName)
        inputNamaFilm.setMaxLength(30)
        inputNamaFilm.move(350, 190)

        labelDuration = QLabel("Film Duration *", self)
        labelDuration.setProperty("class", "normal")
        labelDuration.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelDuration.move(350, 260)

        inputDuration = QLineEdit(self)
        inputDuration.setFixedSize(600, 38)
        inputDuration.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputDuration.setPlaceholderText("Insert Film Duration in Minutes")
        inputDuration.setText(filmDuration)
        inputDuration.setMaxLength(4)
        inputDuration.move(350, 300)

        labelDescription = QLabel("Film Description *", self)
        labelDescription.setProperty("class", "normal")
        labelDescription.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelDescription.move(350, 370)

        inputDescription = QLineEdit(self)
        inputDescription.setFixedSize(600, 38)
        inputDescription.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputDescription.setPlaceholderText("Insert Film Description")
        inputDescription.setText(filmDescription)
        inputDescription.move(350, 410)

        labelPoster = QLabel("Film Poster *", self)
        labelPoster.setProperty("class", "normal")
        labelPoster.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelPoster.move(350, 480)

        inputPoster = QLineEdit(self)
        inputPoster.setFixedSize(600, 38)
        inputPoster.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputPoster.setPlaceholderText("Insert File Path to Film Poster")
        inputPoster.setText(filmPoster)
        inputPoster.move(350, 520)

        buttonBatal = QPushButton("Batal", self)
        buttonBatal.setProperty("class", "btn-danger")
        buttonBatal.clicked.connect(lambda: self.returnToListFilm())
        buttonBatal.move(485, 620)

        buttonSimpan = QPushButton("Simpan", self)
        buttonSimpan.setProperty("class", "btn-success")
        buttonSimpan.clicked.connect(lambda: self.submitAddFilm(inputNamaFilm.text(), inputDuration.text(), inputDescription.text(), inputPoster.text(), filmId))
        buttonSimpan.move(655, 620)

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def returnToListFilm(self):
        self.nextMenu = MenuListFilm(1)
        self.nextMenu.show()
        self.close()

    def submitAddFilm(self, title, duration, description, poster, filmId):
        if(title and duration and description and poster):
            query = QSqlQuery()
            query.prepare("UPDATE film SET Title = :title, Duration = :duration, Description = :description,  Poster = :poster WHERE FilmID = :filmid")
            query.bindValue(':title', title[:40])
            query.bindValue(':duration', int(duration))
            query.bindValue(':description', description)
            query.bindValue(':poster', poster)
            query.bindValue(':filmid', filmId)
            query.exec()

            self.nextMenu = MenuListFilm(1)
            self.nextMenu.show()
            self.close()

        else:
            print("Error required input not filled")

class MenuEditSchedule(QWidget):
    def __init__(self, scheduleId):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - Edit Schedule")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.nextMenu = None

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("Edit Schedule", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(450, 20)

        # Middle

        # Query Debug
        # db = QSqlDatabase.addDatabase('QSQLITE')
        # db.setDatabaseName(db_path)
        #
        # if not db.open():
        #     print("CONNECTION FAILED")
        # else:
        #     print("CONNECTED TO DB SUCCESSFULLY")

        query = QSqlQuery()
        query.prepare("SELECT * FROM screening WHERE ScreeningID = :id")
        query.bindValue(':id', scheduleId)
        query.exec()

        studioId = ""
        filmName = ""
        startTime = ""
        date = ""

        if query.first():
            studioId = query.value(1)
            filmName = query.value(2)
            startTime = query.value(3)
            date = query.value(5)

        query = QSqlQuery()
        query.prepare("SELECT * FROM film WHERE Title LIKE :title")
        query.bindValue(':title', filmName)
        query.exec()

        filmDuration = 0

        if query.first():
            filmDuration = int(query.value(2))

        labelStudioId = QLabel("Studio ID *", self)
        labelStudioId.setProperty("class", "normal")
        labelStudioId.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelStudioId.move(350, 190)

        inputStudioId = QLineEdit(self)
        inputStudioId.setFixedSize(600, 38)
        inputStudioId.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputStudioId.setPlaceholderText("Input Studio ID...")
        inputStudioId.setText(str(studioId))
        inputStudioId.move(350, 230)

        labelNamaFilm = QLabel("Film Title *", self)
        labelNamaFilm.setProperty("class", "normal")
        labelNamaFilm.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelNamaFilm.move(350, 290)

        inputNamaFilm = QLineEdit(self)
        inputNamaFilm.setFixedSize(600, 38)
        inputNamaFilm.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputNamaFilm.setPlaceholderText("Input Film Title...")
        inputNamaFilm.setText(filmName)
        inputNamaFilm.setReadOnly(True)
        inputNamaFilm.move(350, 330)

        labelTanggal = QLabel("Date *", self)
        labelTanggal.setProperty("class", "normal")
        labelTanggal.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelTanggal.move(350, 400)

        inputTanggal = QLineEdit(self)
        inputTanggal.setFixedSize(600, 38)
        inputTanggal.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputTanggal.setPlaceholderText("Format (YYYY-MM-DD)")
        inputTanggal.setMaxLength(10)
        inputTanggal.setText(date)
        inputTanggal.move(350, 440)

        labelStartTime = QLabel("Start Time (XX:XX) *", self)
        labelStartTime.setProperty("class", "normal")
        labelStartTime.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelStartTime.move(350, 510)

        inputStartTimeHour = QLineEdit(self)
        inputStartTimeHour.setFixedSize(70, 38)
        inputStartTimeHour.setStyleSheet("background: #F5F5F5; padding-left: 25px; font-size: 16px;")
        inputStartTimeHour.setPlaceholderText("00")
        inputStartTimeHour.setMaxLength(2)
        inputStartTimeHour.setText(startTime[:2])
        inputStartTimeHour.move(350, 550)

        inputStartTimeMinute = QLineEdit(self)
        inputStartTimeMinute.setFixedSize(70, 38)
        inputStartTimeMinute.setStyleSheet("background: #F5F5F5; padding-left: 25px; font-size: 16px;")
        inputStartTimeMinute.setPlaceholderText("00")
        inputStartTimeMinute.setMaxLength(2)
        inputStartTimeMinute.setText(startTime[3:5])
        inputStartTimeMinute.move(430, 550)

        buttonDuration = QPushButton("Generate End Time", self)
        buttonDuration.setProperty("class", "button")
        buttonDuration.setStyleSheet("width: 180px; height:30px; font-size:16px;")
        buttonDuration.move(565, 555)
        buttonDuration.clicked.connect(
            lambda: self.generateEndTime(inputStartTimeHour.text(), inputStartTimeMinute.text(), filmDuration,
                                         inputEndTimeHour, inputEndTimeMinute))

        labelEndTime = QLabel("End Time (XX:XX) *", self)
        labelEndTime.setProperty("class", "normal")
        labelEndTime.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelEndTime.move(770, 510)

        inputEndTimeHour = QLineEdit(self)
        inputEndTimeHour.setFixedSize(70, 38)
        inputEndTimeHour.setStyleSheet("background: #F5F5F5; padding-left: 25px; font-size: 16px;")
        inputEndTimeHour.move(800, 550)
        inputEndTimeHour.setReadOnly(True)

        inputEndTimeMinute = QLineEdit(self)
        inputEndTimeMinute.setFixedSize(70, 38)
        inputEndTimeMinute.setStyleSheet("background: #F5F5F5; padding-left: 25px; font-size: 16px;")
        inputEndTimeMinute.move(880, 550)
        inputEndTimeMinute.setReadOnly(True)

        buttonBatal = QPushButton("Batal", self)
        buttonBatal.setProperty("class", "btn-danger")
        buttonBatal.clicked.connect(lambda: self.returnToListSchedule())
        buttonBatal.move(505, 620)

        buttonSimpan = QPushButton("Simpan", self)
        buttonSimpan.setProperty("class", "btn-success")
        buttonSimpan.clicked.connect(lambda: self.submitAddSchedule(inputStudioId.text(), inputNamaFilm.text(), inputStartTimeHour.text(), inputStartTimeMinute.text(), inputEndTimeHour.text(), inputEndTimeMinute.text(), inputTanggal.text(), scheduleId))
        buttonSimpan.move(675, 620)

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def returnToListSchedule(self):
        self.nextMenu = MenuListSchedule(1)
        self.nextMenu.show()
        self.close()

    def generateEndTime(self, startHour, startMinute, duration, endHour, endMinute):
        start = datetime.datetime(1, 1, 1, int(startHour) % 24, int(startMinute) % 60, 0)
        end = start + datetime.timedelta(minutes=duration)
        print(str(end.time()))
        endHour.setText(str(end.time())[:2])
        endMinute.setText(str(end.time())[3:5])

    def submitAddSchedule(self, studioId, filmTitle, startHour, startMinute, endHour, endMinute, date, scheduleId):

        query = QSqlQuery()
        query.prepare("SELECT * FROM screening WHERE studioId = :id AND Date LIKE :date")
        query.bindValue(':id', studioId)
        query.bindValue(':date', date)
        query.exec()

        listStartTime = []
        listEndTime = []
        if query.first():
            listStartTime.append(query.value(3))
            listEndTime.append(query.value(4))
            while query.next():
                listStartTime.append(query.value(3))
                listEndTime.append(query.value(4))

        query.finish()

        if len(listStartTime) > 4:
            print("This Studio has reached max screening for this date")

        else:
            badSchedule = False
            for i in range(len(listStartTime)):
                if (((int(startHour) * 60 + int(startMinute)) >= int(str(listStartTime[i])[:2]) * 60 + int(
                        str(listStartTime[i])[3:5])) and (
                        (int(startHour) * 60 + int(startMinute)) < int(str(listEndTime[i])[:2]) * 60 + int(
                        str(listEndTime[i])[3:5]))):
                    badSchedule = True

            if (badSchedule == False):
                if (studioId and filmTitle and startHour and startMinute and endHour and endMinute and date):
                    query = QSqlQuery()
                    query.prepare(
                        "UPDATE screening SET StudioID = :studio, FilmTitle = :title, StartTime = :start, EndTime = :end, Date = :date WHERE ScreeningID = :id) VALUES (:studio, :title, :start, :end, :date)")
                    query.bindValue(':studio', studioId)
                    query.bindValue(':title', filmTitle)
                    query.bindValue(':start', str(startHour) + ":" + str(startMinute))
                    query.bindValue(':end', str(endHour) + ":" + str(endMinute))
                    query.bindValue(':date', date)
                    query.bindValue(':id', scheduleId)
                    query.exec()

                    self.nextMenu = MenuListSchedule(1)
                    self.nextMenu.show()
                    self.close()

                else:
                    print("Error required input not filled")
            else:
                print('This Schedule clashes with existing schedule for this studio')

class MenuListStudio(QWidget):
    def __init__(self, page):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - List Studio")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.nextMenu = None
        self.page = page

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("List Studio", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(480, 20)

        # Middle

        # Query Debug

        # db = QSqlDatabase.addDatabase('QSQLITE')
        # db.setDatabaseName(db_path)
        #
        # if not db.open():
        #     print("CONNECTION FAILED")
        # else:
        #     print("CONNECTED TO DB SUCCESSFULLY")

        query = QSqlQuery()
        query.prepare("SELECT * FROM STUDIO")
        query.exec()

        countRecords = 0

        if query.first():
            countRecords += 1
            while query.next():
                countRecords += 1

        query.finish()

        limit = 5
        offset = (self.page - 1) * limit
        pages = math.ceil(countRecords / limit)

        query = QSqlQuery()
        query.prepare("SELECT * FROM STUDIO LIMIT 5 OFFSET :offset")
        query.bindValue(':offset', offset)
        query.exec()

        listStudioID = []
        listStudioName = []
        listKapasitas = []

        if query.first():
            listStudioID.append(query.value(0))
            listStudioName.append(query.value(1))
            listKapasitas.append(query.value(2))
            while query.next():
                listStudioID.append(query.value(0))
                listStudioName.append(query.value(1))
                listKapasitas.append(query.value(2))

        query.finish()

        #Table Heading

        tableHeader = QPushButton("", self)
        tableHeader.setProperty("class", "table-heading")
        tableHeader.move(90, 150)

        tableHeaderCol1 = QLabel("ID Studio", self)
        tableHeaderCol1.setProperty("class", "table-heading")
        tableHeaderCol1.move(140, 165)

        tableHeaderCol2 = QLabel("Studio Name", self)
        tableHeaderCol2.setProperty("class", "table-heading")
        tableHeaderCol2.move(400, 165)

        tableHeaderCol3 = QLabel("Capacity", self)
        tableHeaderCol3.setProperty("class", "table-heading")
        tableHeaderCol3.move(780, 165)

        tableHeaderCol4 = QLabel("Action", self)
        tableHeaderCol4.setProperty("class", "table-heading")
        tableHeaderCol4.move(1030, 165)

        #Table Items

        #ITEM 1
        tableItem1 = QPushButton("", self)
        tableItem1.setProperty("class", "table-item")
        tableItem1.move(90, 210)

        if len(listStudioID) > 0:
            tableItem1Col1 = QLabel(str(listStudioID[0]), self)
            tableItem1Col1.setProperty("class", "table-item")
            tableItem1Col1.move(165, 225)

            tableItem1Col2 = QLabel(str(listStudioName[0]), self)
            tableItem1Col2.setProperty("class", "table-item")
            tableItem1Col2.setStyleSheet("")
            tableItem1Col2.move(275, 225)

            tableItem1Col3 = QLabel(str(listKapasitas[0]), self)
            tableItem1Col3.setProperty("class", "table-item")
            tableItem1Col3.move(805, 225)

            tableItem1Col4 = QPushButton("Edit", self)
            tableItem1Col4.setProperty("class", "btn-edit")
            tableItem1Col4.move(950, 218)
            tableItem1Col4.clicked.connect(lambda: self.editStudio(str(listStudioID[0])))

            tableItem1Col5 = QPushButton("Delete", self)
            tableItem1Col5.setProperty("class", "btn-del")
            tableItem1Col5.move(1070, 218)
            tableItem1Col5.clicked.connect(lambda: self.delStudio(listStudioID[0]))

        #ITEM 2
        tableItem2 = QPushButton("", self)
        tableItem2.setProperty("class", "table-item")
        tableItem2.move(90, 270)

        if len(listStudioID) > 1 :
            tableItem2Col1 = QLabel(str(listStudioID[1]), self)
            tableItem2Col1.setProperty("class", "table-item")
            tableItem2Col1.move(165, 285)

            tableItem2Col2 = QLabel(str(listStudioName[1]), self)
            tableItem2Col2.setProperty("class", "table-item")
            tableItem2Col2.move(275, 285)

            tableItem2Col3 = QLabel(str(listKapasitas[1]), self)
            tableItem2Col3.setProperty("class", "table-item")
            tableItem2Col3.move(805, 285)

            tableItem2Col4 = QPushButton("Edit", self)
            tableItem2Col4.setProperty("class", "btn-edit")
            tableItem2Col4.move(950, 278)
            tableItem2Col4.clicked.connect(lambda: self.editStudio(str(listStudioID[1])))

            tableItem2Col5 = QPushButton("Delete", self)
            tableItem2Col5.setProperty("class", "btn-del")
            tableItem2Col5.move(1070, 278)
            tableItem2Col5.clicked.connect(lambda: self.delStudio(listStudioID[1]))

        #ITEM 3
        tableItem3 = QPushButton("", self)
        tableItem3.setProperty("class", "table-item")
        tableItem3.move(90, 330)

        if len(listStudioID) > 2:
            tableItem3Col1 = QLabel(str(listStudioID[2]), self)
            tableItem3Col1.setProperty("class", "table-item")
            tableItem3Col1.move(165, 345)

            tableItem3Col2 = QLabel(str(listStudioName[2]), self)
            tableItem3Col2.setProperty("class", "table-item")
            tableItem3Col2.move(275, 345)

            tableItem3Col3 = QLabel(str(listKapasitas[2]), self)
            tableItem3Col3.setProperty("class", "table-item")
            tableItem3Col3.move(805, 345)

            tableItem3Col4 = QPushButton("Edit", self)
            tableItem3Col4.setProperty("class", "btn-edit")
            tableItem3Col4.move(950, 338)
            tableItem3Col4.clicked.connect(lambda: self.editStudio(str(listStudioID[2])))

            tableItem3Col5 = QPushButton("Delete", self)
            tableItem3Col5.setProperty("class", "btn-del")
            tableItem3Col5.move(1070, 338)
            tableItem3Col5.clicked.connect(lambda: self.delStudio(listStudioID[2]))

        #ITEM 4
        tableItem4 = QPushButton("", self)
        tableItem4.setProperty("class", "table-item")
        tableItem4.move(90, 390)

        if len(listStudioID) > 3:
            tableItem4Col1 = QLabel(str(listStudioID[3]), self)
            tableItem4Col1.setProperty("class", "table-item")
            tableItem4Col1.move(165, 405)

            tableItem4Col2 = QLabel(str(listStudioName[3]), self)
            tableItem4Col2.setProperty("class", "table-item")
            tableItem4Col2.move(275, 405)

            tableItem4Col3 = QLabel(str(listKapasitas[3]), self)
            tableItem4Col3.setProperty("class", "table-item")
            tableItem4Col3.move(805, 405)

            tableItem4Col4 = QPushButton("Edit", self)
            tableItem4Col4.setProperty("class", "btn-edit")
            tableItem4Col4.move(950, 398)
            tableItem4Col4.clicked.connect(lambda: self.editStudio(str(listStudioID[3])))

            tableItem4Col5 = QPushButton("Delete", self)
            tableItem4Col5.setProperty("class", "btn-del")
            tableItem4Col5.move(1070, 398)
            tableItem3Col5.clicked.connect(lambda: self.delStudio(listStudioID[3]))

        #ITEM 5
        tableItem5 = QPushButton("", self)
        tableItem5.setProperty("class", "table-item")
        tableItem5.move(90, 450)

        if len(listStudioID) > 4:
            tableItem5Col1 = QLabel(str(listStudioID[4]), self)
            tableItem5Col1.setProperty("class", "table-item")
            tableItem5Col1.move(165, 465)

            tableItem5Col2 = QLabel(str(listStudioName[4]), self)
            tableItem5Col2.setProperty("class", "table-item")
            tableItem5Col2.move(275, 465)

            tableItem5Col3 = QLabel(str(listKapasitas[4]), self)
            tableItem5Col3.setProperty("class", "table-item")
            tableItem5Col3.move(805, 465)

            tableItem5Col4 = QPushButton("Edit", self)
            tableItem5Col4.setProperty("class", "btn-edit")
            tableItem5Col4.move(950, 458)
            tableItem3Col4.clicked.connect(lambda: self.editStudio(str(listStudioID[4])))

            tableItem5Col5 = QPushButton("Delete", self)
            tableItem5Col5.setProperty("class", "btn-del")
            tableItem5Col5.move(1070, 458)
            tableItem3Col5.clicked.connect(lambda: self.delStudio(listStudioID[4]))

        buttonAdd = QPushButton("Add New Studio", self)
        buttonAdd.setProperty("class", "button")
        buttonAdd.setStyleSheet("width: 200px; height: 44px")
        buttonAdd.move(540, 530)
        buttonAdd.clicked.connect(lambda: self.addNewStudio())

        # Pagination

        buttonPrevPage = QPushButton("<< Prev Page", self)
        if (self.page == 1):
            buttonPrevPage.setProperty("class", "btn-disabled")
            buttonPrevPage.move(400, 600)
        else:
            buttonPrevPage.setProperty("class", "btn-page")
            buttonPrevPage.move(400, 600)
            buttonPrevPage.clicked.connect(lambda: self.changePage(self.page-1))

        buttonNextPage = QPushButton("Next Page >>", self)
        if(countRecords < (self.page * 5 + 1)):
            buttonNextPage.setProperty("class", "btn-disabled")
            buttonNextPage.move(700, 600)
        else:
            buttonNextPage.setProperty("class", "btn-page")
            buttonNextPage.move(700, 600)
            buttonNextPage.clicked.connect(lambda : self.changePage(self.page+1))

        buttonReturn = QPushButton("<< Main Menu", self)
        buttonReturn.setProperty("class", "option")
        buttonReturn.setStyleSheet("width: 200px; height: 44px; font-size: 20px;")
        buttonReturn.move(90, 660)
        buttonReturn.clicked.connect(lambda: self.returnToMainMenu())

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def changePage(self, next):
        self.nextMenu = MenuListStudio(next)
        self.nextMenu.show()
        self.close()

    def delStudio(self, studioId):
        query = QSqlQuery()
        query.prepare("DELETE FROM studio WHERE StudioID = :id")
        query.bindValue(':id', studioId)
        query.exec()
        query.finish()

        self.nextMenu = MenuListStudio(self.page)
        self.nextMenu.show()
        self.close()

    def editStudio(self, studioId):
        self.nextMenu = MenuEditStudio(studioId)
        self.nextMenu.show()
        self.close()

    def addNewStudio(self):
        self.nextMenu = MenuAddStudio()
        self.nextMenu.show()
        self.close()

    def returnToMainMenu(self):
        self.nextMenu = MainMenuAdmin()
        self.nextMenu.show()
        self.close()

class MenuListFilm(QWidget):
    def __init__(self, page):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - List Studio")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.nextMenu = None
        self.page = page

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("List Film", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(510, 20)

        # Middle

        # Query Debug

        # db = QSqlDatabase.addDatabase('QSQLITE')
        # db.setDatabaseName(db_path)
        #
        # if not db.open():
        #     print("CONNECTION FAILED")
        # else:
        #     print("CONNECTED TO DB SUCCESSFULLY")

        query = QSqlQuery()
        query.prepare("SELECT * FROM film")
        query.exec()

        countRecords = 0

        if query.first():
            countRecords += 1
            while query.next():
                countRecords += 1

        query.finish()

        limit = 5
        offset = (self.page - 1) * limit
        pages = math.ceil(countRecords / limit)

        query = QSqlQuery()
        query.prepare("SELECT * FROM film ORDER BY FilmID DESC LIMIT 5  OFFSET :offset")
        query.bindValue(':offset', offset)
        query.exec()

        listFilmID = []
        listFilmTitle = []
        listFilmDuration = []
        listFilmDescription = []

        if query.first():
            listFilmID.append(query.value(0))
            listFilmTitle.append(query.value(1))
            listFilmDuration.append(query.value(2))
            listFilmDescription.append(query.value(3))
            while query.next():
                listFilmID.append(query.value(0))
                listFilmTitle.append(query.value(1))
                listFilmDuration.append(query.value(2))
                listFilmDescription.append(query.value(3))

        query.finish()

        # Table Heading

        tableHeader = QPushButton("", self)
        tableHeader.setProperty("class", "table-heading")
        tableHeader.move(90, 150)

        tableHeaderCol1 = QLabel("ID Film", self)
        tableHeaderCol1.setProperty("class", "table-heading")
        tableHeaderCol1.move(140, 165)

        tableHeaderCol2 = QLabel("Film Title", self)
        tableHeaderCol2.setProperty("class", "table-heading")
        tableHeaderCol2.move(400, 165)

        tableHeaderCol3 = QLabel("Duration", self)
        tableHeaderCol3.setProperty("class", "table-heading")
        tableHeaderCol3.move(740, 165)

        tableHeaderCol4 = QLabel("Action", self)
        tableHeaderCol4.setProperty("class", "table-heading")
        tableHeaderCol4.move(990, 165)

        # Table Items

        # ITEM 1
        tableItem1 = QPushButton("", self)
        tableItem1.setProperty("class", "table-item")
        tableItem1.move(90, 210)

        if len(listFilmID) > 0:
            tableItem1Col1 = QLabel(str(listFilmID[0]), self)
            tableItem1Col1.setProperty("class", "table-item")
            tableItem1Col1.move(165, 225)

            tableItem1Col2 = QLabel(str(listFilmTitle[0]), self)
            tableItem1Col2.setProperty("class", "table-item")
            tableItem1Col2.move(245, 225)

            tableItem1Col3 = QLabel(str(listFilmDuration[0]), self)
            tableItem1Col3.setProperty("class", "table-item")
            tableItem1Col3.move(760, 225)

            tableItem1Col4 = QPushButton("Edit", self)
            tableItem1Col4.setProperty("class", "btn-edit")
            tableItem1Col4.move(860, 218)
            tableItem1Col4.clicked.connect(lambda: self.editFilm(str(listFilmID[0])))

            tableItem1Col5 = QPushButton("Delete", self)
            tableItem1Col5.setProperty("class", "btn-del")
            tableItem1Col5.move(970, 218)
            tableItem1Col5.clicked.connect(lambda: self.delFilm(listFilmID[0]))

            tableItem1Col6 = QPushButton("Schedule", self)
            tableItem1Col6.setProperty("class", "button")
            tableItem1Col6.setStyleSheet("width: 100px; height: 35px; font-size: 18px;")
            tableItem1Col6.move(1080, 218)
            tableItem1Col6.clicked.connect(lambda: self.addSchedule(str(listFilmID[0])))

        # ITEM 2
        tableItem2 = QPushButton("", self)
        tableItem2.setProperty("class", "table-item")
        tableItem2.move(90, 270)

        if len(listFilmID) > 1:
            tableItem2Col1 = QLabel(str(listFilmID[1]), self)
            tableItem2Col1.setProperty("class", "table-item")
            tableItem2Col1.move(165, 285)

            tableItem2Col2 = QLabel(str(listFilmTitle[1]), self)
            tableItem2Col2.setProperty("class", "table-item")
            tableItem2Col2.move(245, 285)

            tableItem2Col3 = QLabel(str(listFilmDuration[1]), self)
            tableItem2Col3.setProperty("class", "table-item")
            tableItem2Col3.move(760, 285)

            tableItem2Col4 = QPushButton("Edit", self)
            tableItem2Col4.setProperty("class", "btn-edit")
            tableItem2Col4.move(860, 278)
            tableItem2Col4.clicked.connect(lambda: self.editFilm(str(listFilmID[1])))

            tableItem2Col5 = QPushButton("Delete", self)
            tableItem2Col5.setProperty("class", "btn-del")
            tableItem2Col5.move(970, 278)
            tableItem2Col5.clicked.connect(lambda: self.delFilm(listFilmID[1]))

            tableItem2Col6 = QPushButton("Schedule", self)
            tableItem2Col6.setProperty("class", "button")
            tableItem2Col6.setStyleSheet("width: 100px; height: 35px; font-size: 18px;")
            tableItem2Col6.move(1080, 278)
            tableItem2Col6.clicked.connect(lambda: self.addSchedule(str(listFilmID[1])))

        # ITEM 3
        tableItem3 = QPushButton("", self)
        tableItem3.setProperty("class", "table-item")
        tableItem3.move(90, 330)

        if len(listFilmID) > 2:
            tableItem3Col1 = QLabel(str(listFilmID[2]), self)
            tableItem3Col1.setProperty("class", "table-item")
            tableItem3Col1.move(165, 345)

            tableItem3Col2 = QLabel(str(listFilmTitle[2]), self)
            tableItem3Col2.setProperty("class", "table-item")
            tableItem3Col2.move(245, 345)

            tableItem3Col3 = QLabel(str(listFilmDuration[2]), self)
            tableItem3Col3.setProperty("class", "table-item")
            tableItem3Col3.move(760, 345)

            tableItem3Col4 = QPushButton("Edit", self)
            tableItem3Col4.setProperty("class", "btn-edit")
            tableItem3Col4.move(860, 338)
            tableItem3Col4.clicked.connect(lambda: self.editFilm(str(listFilmID[2])))

            tableItem3Col5 = QPushButton("Delete", self)
            tableItem3Col5.setProperty("class", "btn-del")
            tableItem3Col5.move(970, 338)
            tableItem3Col5.clicked.connect(lambda: self.delFilm(listFilmID[2]))

            tableItem3Col6 = QPushButton("Schedule", self)
            tableItem3Col6.setProperty("class", "button")
            tableItem3Col6.setStyleSheet("width: 100px; height: 35px; font-size: 18px;")
            tableItem3Col6.move(1080, 338)
            tableItem3Col6.clicked.connect(lambda: self.addSchedule(str(listFilmID[2])))

        # ITEM 4
        tableItem4 = QPushButton("", self)
        tableItem4.setProperty("class", "table-item")
        tableItem4.move(90, 390)

        if len(listFilmID) > 3:
            tableItem4Col1 = QLabel(str(listFilmID[3]), self)
            tableItem4Col1.setProperty("class", "table-item")
            tableItem4Col1.move(165, 405)

            tableItem4Col2 = QLabel(str(listFilmTitle[3]), self)
            tableItem4Col2.setProperty("class", "table-item")
            tableItem4Col2.move(245, 405)

            tableItem4Col3 = QLabel(str(listFilmDuration[3]), self)
            tableItem4Col3.setProperty("class", "table-item")
            tableItem4Col3.move(760, 405)

            tableItem4Col4 = QPushButton("Edit", self)
            tableItem4Col4.setProperty("class", "btn-edit")
            tableItem4Col4.move(860, 398)
            tableItem4Col4.clicked.connect(lambda: self.editFilm(str(listFilmID[3])))

            tableItem4Col5 = QPushButton("Delete", self)
            tableItem4Col5.setProperty("class", "btn-del")
            tableItem4Col5.move(970, 398)
            tableItem4Col5.clicked.connect(lambda: self.delFilm(listFilmID[3]))

            tableItem4Col6 = QPushButton("Schedule", self)
            tableItem4Col6.setProperty("class", "button")
            tableItem4Col6.setStyleSheet("width: 100px; height: 35px; font-size: 18px;")
            tableItem4Col6.move(1080, 398)
            tableItem4Col6.clicked.connect(lambda: self.addSchedule(str(listFilmID[3])))

        # ITEM 5
        tableItem5 = QPushButton("", self)
        tableItem5.setProperty("class", "table-item")
        tableItem5.move(90, 450)

        if len(listFilmID) > 4:
            tableItem5Col1 = QLabel(str(listFilmID[4]), self)
            tableItem5Col1.setProperty("class", "table-item")
            tableItem5Col1.move(165, 465)

            tableItem5Col2 = QLabel(str(listFilmTitle[4]), self)
            tableItem5Col2.setProperty("class", "table-item")
            tableItem5Col2.move(245, 465)

            tableItem5Col3 = QLabel(str(listFilmDuration[4]), self)
            tableItem5Col3.setProperty("class", "table-item")
            tableItem5Col3.move(760, 465)

            tableItem5Col4 = QPushButton("Edit", self)
            tableItem5Col4.setProperty("class", "btn-edit")
            tableItem5Col4.move(860, 458)
            tableItem5Col4.clicked.connect(lambda: self.editFilm(str(listFilmID[4])))

            tableItem5Col5 = QPushButton("Delete", self)
            tableItem5Col5.setProperty("class", "btn-del")
            tableItem5Col5.move(970, 458)
            tableItem5Col5.clicked.connect(lambda: self.delFilm(listFilmID[4]))

            tableItem5Col6 = QPushButton("Schedule", self)
            tableItem5Col6.setProperty("class", "button")
            tableItem5Col6.setStyleSheet("width: 100px; height: 35px; font-size: 18px;")
            tableItem5Col6.move(1080, 458)
            tableItem5Col6.clicked.connect(lambda: self.addSchedule(str(listFilmID[4])))

        buttonAdd = QPushButton("Add New Film", self)
        buttonAdd.setProperty("class", "button")
        buttonAdd.setStyleSheet("width: 200px; height: 44px")
        buttonAdd.move(540, 530)
        buttonAdd.clicked.connect(lambda: self.addNewFilm())

        # Pagination

        buttonPrevPage = QPushButton("<< Prev Page", self)
        if (self.page == 1):
            buttonPrevPage.setProperty("class", "btn-disabled")
            buttonPrevPage.move(400, 600)
        else:
            buttonPrevPage.setProperty("class", "btn-page")
            buttonPrevPage.move(400, 600)
            buttonPrevPage.clicked.connect(lambda: self.changePage(self.page - 1))

        buttonNextPage = QPushButton("Next Page >>", self)
        if (countRecords < (self.page * 5 + 1)):
            buttonNextPage.setProperty("class", "btn-disabled")
            buttonNextPage.move(700, 600)
        else:
            buttonNextPage.setProperty("class", "btn-page")
            buttonNextPage.move(700, 600)
            buttonNextPage.clicked.connect(lambda: self.changePage(self.page + 1))

        buttonReturn = QPushButton("<< Main Menu", self)
        buttonReturn.setProperty("class", "option")
        buttonReturn.setStyleSheet("width: 200px; height: 44px; font-size: 20px;")
        buttonReturn.move(90, 660)
        buttonReturn.clicked.connect(lambda: self.returnToMainMenu())

        buttonScheduleMenu = QPushButton("List Schedule >>", self)
        buttonScheduleMenu.setProperty("class", "option")
        buttonScheduleMenu.setStyleSheet("width: 200px; height: 44px; font-size: 20px;")
        buttonScheduleMenu.move(980, 660)
        buttonScheduleMenu.clicked.connect(lambda: self.toSchedule())

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def changePage(self, next):
        self.nextMenu = MenuListFilm(next)
        self.nextMenu.show()
        self.close()

    def returnToMainMenu(self):
        self.nextMenu = MainMenuAdmin()
        self.nextMenu.show()
        self.close()

    def editFilm(self, filmId):
        self.nextMenu = MenuEditFilm(filmId)
        self.nextMenu.show()
        self.close()

    def delFilm(self, filmId):
        query = QSqlQuery()
        query.prepare("DELETE FROM film WHERE filmid = :id")
        query.bindValue(':id', filmId)
        query.exec()
        query.finish()

        self.nextMenu = MenuListFilm(self.page)
        self.nextMenu.show()
        self.close()

    def addNewFilm(self):
        self.nextMenu = MenuAddFilm()
        self.nextMenu.show()
        self.close()

    def addSchedule(self, filmId):
        self.nextMenu = MenuAddSchedule(filmId)
        self.nextMenu.show()
        self.close()

    def toSchedule(self):
        self.nextMenu = MenuListSchedule(1)
        self.nextMenu.show()
        self.close()

class MenuListSchedule(QWidget):
    def __init__(self, page):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - List Schedule")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.nextMenu = None
        self.page = page

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("List Schedule", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(450, 20)

        # Middle

        # Query Debug

        # db = QSqlDatabase.addDatabase('QSQLITE')
        # db.setDatabaseName(db_path)
        #
        # if not db.open():
        #     print("CONNECTION FAILED")
        # else:
        #     print("CONNECTED TO DB SUCCESSFULLY")

        query = QSqlQuery()
        query.prepare("SELECT * FROM screening")
        query.exec()

        countRecords = 0

        if query.first():
            countRecords += 1
            while query.next():
                countRecords += 1

        query.finish()

        limit = 5
        offset = (self.page - 1) * limit
        pages = math.ceil(countRecords / limit)

        query = QSqlQuery()
        query.prepare("SELECT * FROM screening ORDER BY ScreeningID DESC LIMIT 5  OFFSET :offset")
        query.bindValue(':offset', offset)
        query.exec()

        listScreeningID = []
        listStudioID = []
        listFilmTitle = []
        listStartTime = []
        listEndTime = []
        listDate = []

        if query.first():
            listScreeningID.append(query.value(0))
            listStudioID.append(query.value(1))
            listFilmTitle.append(query.value(2))
            listStartTime.append(query.value(3))
            listEndTime.append(query.value(4))
            listDate.append(query.value(5))

            while query.next():
                listScreeningID.append(query.value(0))
                listStudioID.append(query.value(1))
                listFilmTitle.append(query.value(2))
                listStartTime.append(query.value(3))
                listEndTime.append(query.value(4))
                listDate.append(query.value(5))

        query.finish()

        # Table Heading

        tableHeader = QPushButton("", self)
        tableHeader.setProperty("class", "table-heading")
        tableHeader.setStyleSheet('background: #3084D1')
        tableHeader.move(90, 150)

        tableHeaderCol1 = QLabel("ID Sch", self)
        tableHeaderCol1.setProperty("class", "table-heading")
        tableHeaderCol1.setStyleSheet('background: #3084D1')
        tableHeaderCol1.move(110, 165)

        tableHeaderCol2 = QLabel("ID Studio", self)
        tableHeaderCol2.setProperty("class", "table-heading")
        tableHeaderCol2.setStyleSheet('background: #3084D1')
        tableHeaderCol2.move(200, 165)

        tableHeaderCol3 = QLabel("Film Title", self)
        tableHeaderCol3.setProperty("class", "table-heading")
        tableHeaderCol3.setStyleSheet('background: #3084D1')
        tableHeaderCol3.move(450, 165)

        tableHeaderCol4 = QLabel("Time", self)
        tableHeaderCol4.setProperty("class", "table-heading")
        tableHeaderCol4.setStyleSheet('background: #3084D1')
        tableHeaderCol4.move(800, 165)

        tableHeaderCol5 = QLabel("Action", self)
        tableHeaderCol5.setProperty("class", "table-heading")
        tableHeaderCol5.setStyleSheet('background: #3084D1')
        tableHeaderCol5.move(1040, 165)

        # ITEM 1

        tableItem1 = QPushButton("", self)
        tableItem1.setProperty("class", "table-item")
        tableItem1.move(90, 210)

        if len(listScreeningID) > 0:
            tableItem1Col1 = QLabel(str(listScreeningID[0]), self)
            tableItem1Col1.setProperty("class", "table-item")
            tableItem1Col1.move(135, 225)

            tableItem1Col2 = QLabel(str(listStudioID[0]), self)
            tableItem1Col2.setProperty("class", "table-item")
            tableItem1Col2.move(235, 225)

            tableItem1Col3 = QLabel(str(listFilmTitle[0]), self)
            tableItem1Col3.setProperty("class", "table-item")
            tableItem1Col3.move(320, 225)

            tableItem1Col4 = QLabel(str(listStartTime[0]) + " - " + str(listEndTime[0] + " | " + str(listDate[0])), self)
            tableItem1Col4.setProperty("class", "table-item")
            tableItem1Col4.move(700, 225)

            tableItem1Col5 = QPushButton("Edit", self)
            tableItem1Col5.setProperty("class", "btn-edit")
            tableItem1Col5.move(970, 218)
            tableItem1Col5.clicked.connect(lambda: self.editSchedule(str(listScreeningID[0])))

            tableItem1Col6 = QPushButton("Delete", self)
            tableItem1Col6.setProperty("class", "btn-del")
            tableItem1Col6.move(1080, 218)
            tableItem1Col6.clicked.connect(lambda: self.delSchedule(listScreeningID[0]))

        # ITEM 2

        tableItem2 = QPushButton("", self)
        tableItem2.setProperty("class", "table-item")
        tableItem2.move(90, 270)

        if len(listScreeningID) > 1:
            tableItem2Col1 = QLabel(str(listScreeningID[1]), self)
            tableItem2Col1.setProperty("class", "table-item")
            tableItem2Col1.move(135, 285)

            tableItem2Col2 = QLabel(str(listStudioID[1]), self)
            tableItem2Col2.setProperty("class", "table-item")
            tableItem2Col2.move(235, 285)

            tableItem2Col3 = QLabel(str(listFilmTitle[1]), self)
            tableItem2Col3.setProperty("class", "table-item")
            tableItem2Col3.move(320, 285)

            tableItem2Col4 = QLabel(str(listStartTime[1]) + " - " + str(listEndTime[1] + " | " + str(listDate[1])), self)
            tableItem2Col4.setProperty("class", "table-item")
            tableItem2Col4.move(700, 285)

            tableItem2Col5 = QPushButton("Edit", self)
            tableItem2Col5.setProperty("class", "btn-edit")
            tableItem2Col5.move(970, 278)
            tableItem2Col5.clicked.connect(lambda: self.editSchedule(str(listScreeningID[1])))

            tableItem2Col6 = QPushButton("Delete", self)
            tableItem2Col6.setProperty("class", "btn-del")
            tableItem2Col6.move(1080, 278)
            tableItem2Col6.clicked.connect(lambda: self.delSchedule(listScreeningID[1]))

        # ITEM 3

        tableItem3 = QPushButton("", self)
        tableItem3.setProperty("class", "table-item")
        tableItem3.move(90, 330)

        if len(listScreeningID) > 2:
            tableItem3Col1 = QLabel(str(listScreeningID[2]), self)
            tableItem3Col1.setProperty("class", "table-item")
            tableItem3Col1.move(135, 345)

            tableItem3Col2 = QLabel(str(listStudioID[2]), self)
            tableItem3Col2.setProperty("class", "table-item")
            tableItem3Col2.move(235, 345)

            tableItem3Col3 = QLabel(str(listFilmTitle[2]), self)
            tableItem3Col3.setProperty("class", "table-item")
            tableItem3Col3.move(320, 345)

            tableItem3Col4 = QLabel(str(listStartTime[2]) + " - " + str(listEndTime[2] + " | " + str(listDate[2])), self)
            tableItem3Col4.setProperty("class", "table-item")
            tableItem3Col4.move(700, 345)

            tableItem3Col5 = QPushButton("Edit", self)
            tableItem3Col5.setProperty("class", "btn-edit")
            tableItem3Col5.move(970, 338)
            tableItem3Col5.clicked.connect(lambda: self.editSchedule(str(listScreeningID[2])))

            tableItem3Col6 = QPushButton("Delete", self)
            tableItem3Col6.setProperty("class", "btn-del")
            tableItem3Col6.move(1080, 338)
            tableItem3Col6.clicked.connect(lambda: self.delSchedule(listScreeningID[2]))

        # ITEM 4

        tableItem4 = QPushButton("", self)
        tableItem4.setProperty("class", "table-item")
        tableItem4.move(90, 390)

        if len(listScreeningID) > 3:
            tableItem4Col1 = QLabel(str(listScreeningID[3]), self)
            tableItem4Col1.setProperty("class", "table-item")
            tableItem4Col1.move(135, 405)

            tableItem4Col2 = QLabel(str(listStudioID[3]), self)
            tableItem4Col2.setProperty("class", "table-item")
            tableItem4Col2.move(235, 405)

            tableItem4Col3 = QLabel(str(listFilmTitle[3]), self)
            tableItem4Col3.setProperty("class", "table-item")
            tableItem4Col3.move(320, 405)

            tableItem4Col4 = QLabel(str(listStartTime[3]) + " - " + str(listEndTime[3] + " | " + str(listDate[3])), self)
            tableItem4Col4.setProperty("class", "table-item")
            tableItem4Col4.move(700, 405)

            tableItem4Col5 = QPushButton("Edit", self)
            tableItem4Col5.setProperty("class", "btn-edit")
            tableItem4Col5.move(970, 398)
            tableItem4Col5.clicked.connect(lambda: self.editSchedule(str(listScreeningID[3])))

            tableItem4Col6 = QPushButton("Delete", self)
            tableItem4Col6.setProperty("class", "btn-del")
            tableItem4Col6.move(1080, 398)
            tableItem4Col6.clicked.connect(lambda: self.delSchedule(listScreeningID[3]))

        # ITEM 5

        tableItem5 = QPushButton("", self)
        tableItem5.setProperty("class", "table-item")
        tableItem5.move(90, 450)

        if len(listScreeningID) > 4:
            tableItem5Col1 = QLabel(str(listScreeningID[4]), self)
            tableItem5Col1.setProperty("class", "table-item")
            tableItem5Col1.move(135, 465)

            tableItem5Col2 = QLabel(str(listStudioID[4]), self)
            tableItem5Col2.setProperty("class", "table-item")
            tableItem5Col2.move(235, 465)

            tableItem5Col3 = QLabel(str(listFilmTitle[4]), self)
            tableItem5Col3.setProperty("class", "table-item")
            tableItem5Col3.move(320, 465)

            tableItem5Col4 = QLabel(str(listStartTime[4]) + " - " + str(listEndTime[4] + " | " + str(listDate[4])), self)
            tableItem5Col4.setProperty("class", "table-item")
            tableItem5Col4.move(700, 465)

            tableItem5Col5 = QPushButton("Edit", self)
            tableItem5Col5.setProperty("class", "btn-edit")
            tableItem5Col5.move(970, 458)
            tableItem5Col5.clicked.connect(lambda: self.editSchedule(str(listScreeningID[4])))

            tableItem5Col6 = QPushButton("Delete", self)
            tableItem5Col6.setProperty("class", "btn-del")
            tableItem5Col6.move(1080, 458)
            tableItem5Col6.clicked.connect(lambda: self.delSchedule(listScreeningID[4]))

        # Pagination

        buttonPrevPage = QPushButton("<< Prev Page", self)
        if (self.page == 1):
            buttonPrevPage.setProperty("class", "btn-disabled")
            buttonPrevPage.move(400, 520)
        else:
            buttonPrevPage.setProperty("class", "btn-page")
            buttonPrevPage.move(400, 520)
            buttonPrevPage.clicked.connect(lambda: self.changePage(self.page - 1))

        buttonNextPage = QPushButton("Next Page >>", self)
        if (countRecords < (self.page * 5 + 1)):
            buttonNextPage.setProperty("class", "btn-disabled")
            buttonNextPage.move(700, 520)
        else:
            buttonNextPage.setProperty("class", "btn-page")
            buttonNextPage.move(700, 520)
            buttonNextPage.clicked.connect(lambda: self.changePage(self.page + 1))

        buttonFilmMenu = QPushButton("<< List Film", self)
        buttonFilmMenu.setProperty("class", "option")
        buttonFilmMenu.setStyleSheet("width: 200px; height: 44px; font-size: 20px;")
        buttonFilmMenu.move(90, 660)
        buttonFilmMenu.clicked.connect(lambda: self.toFilm())

        buttonScheduleMenu = QPushButton("Main Menu >>", self)
        buttonScheduleMenu.setProperty("class", "option")
        buttonScheduleMenu.setStyleSheet("width: 200px; height: 44px; font-size: 20px;")
        buttonScheduleMenu.move(980, 660)
        buttonScheduleMenu.clicked.connect(lambda: self.returnToMainMenu())

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def changePage(self, next):
        self.nextMenu = MenuListSchedule(next)
        self.nextMenu.show()
        self.close()

    def editSchedule(self, scheduleId):
        self.nextMenu = MenuEditSchedule(scheduleId)
        self.nextMenu.show()
        self.close()

    def delSchedule(self, scheduleId):
        query = QSqlQuery()
        query.prepare("DELETE FROM screening WHERE ScreeningID = :id")
        query.bindValue(':id', scheduleId)
        query.exec()
        query.finish()

        self.nextMenu = MenuListFilm(self.page)
        self.nextMenu.show()
        self.close()

    def returnToMainMenu(self):
        self.nextMenu = MainMenuAdmin()
        self.nextMenu.show()
        self.close()

    def toFilm(self):
        self.nextMenu = MenuListFilm(1)
        self.nextMenu.show()
        self.close()

class MenuListTicket(QWidget):
    def __init__(self, page):
        super().__init__()
        self.setWindowIcon(QIcon("../img/cinemanage.png"))
        self.setWindowTitle("CineManage - List Ticket")
        self.setContentsMargins(20, 20, 20, 20)
        screenWidth = 1280
        screenHeight = 720
        self.setFixedSize(screenWidth, screenHeight)
        self.nextMenu = None
        self.page = page

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
        buttonUser.setProperty("class", "btn-danger")
        buttonUser.setStyleSheet("background: #F04D4D; width: 180px; height: 35px;")
        buttonUser.move(110, 47)

        labelTitleMenu = QLabel("List Ticket", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(480, 20)

        # Middle

        # Query For Debug

        # db = QSqlDatabase.addDatabase('QSQLITE')
        # db.setDatabaseName(db_path)
        #
        # if not db.open():
        #     print("CONNECTION FAILED")
        # else:
        #     print("CONNECTED TO DB SUCCESSFULLY")

        query = QSqlQuery()
        query.prepare("SELECT * FROM ticket")
        query.exec()

        countRecords = 0

        if query.first():
            countRecords += 1
            while query.next():
                countRecords += 1

        query.finish()

        limit = 5
        offset = (self.page - 1) * limit
        pages = math.ceil(countRecords / limit)

        query = QSqlQuery()
        query.prepare("SELECT * FROM ticket ORDER BY ScreeningID DESC LIMIT 5  OFFSET :offset")
        query.bindValue(':offset', offset)
        query.exec()

        listSeatID = []
        listStudioID = []
        listScreeningID = []
        listOrderDate = []

        if query.first():
            listSeatID.append(query.value(0))
            listStudioID.append(query.value(1))
            listScreeningID.append(query.value(2))
            listOrderDate.append(query.value(3))
            while query.next():
                listSeatID.append(query.value(0))
                listStudioID.append(query.value(1))
                listScreeningID.append(query.value(2))
                listOrderDate.append(query.value(3))

        query.finish()

        # Table Heading

        tableHeader = QPushButton("", self)
        tableHeader.setProperty("class", "table-heading")
        tableHeader.move(90, 150)

        tableHeaderCol1 = QLabel("ID Seat", self)
        tableHeaderCol1.setProperty("class", "table-heading")
        tableHeaderCol1.move(110, 165)

        tableHeaderCol2 = QLabel("ID Studio", self)
        tableHeaderCol2.setProperty("class", "table-heading")
        tableHeaderCol2.move(220, 165)

        tableHeaderCol3 = QLabel("ID Schedule", self)
        tableHeaderCol3.setProperty("class", "table-heading")
        tableHeaderCol3.move(350, 165)

        tableHeaderCol4 = QLabel("Order Date", self)
        tableHeaderCol4.setProperty("class", "table-heading")
        tableHeaderCol4.move(660, 165)

        tableHeaderCol5 = QLabel("Action", self)
        tableHeaderCol5.setProperty("class", "table-heading")
        tableHeaderCol5.move(1040, 165)

        # ITEM 1

        tableItem1 = QPushButton("", self)
        tableItem1.setProperty("class", "table-item")
        tableItem1.move(90, 210)

        if len(listScreeningID) > 0:
            tableItem1Col1 = QLabel(str(listSeatID[0]), self)
            tableItem1Col1.setProperty("class", "table-item")
            tableItem1Col1.move(120, 225)

            tableItem1Col2 = QLabel(str(listStudioID[0]), self)
            tableItem1Col2.setProperty("class", "table-item")
            tableItem1Col2.move(260, 225)

            tableItem1Col3 = QLabel(str(listScreeningID[0]), self)
            tableItem1Col3.setProperty("class", "table-item")
            tableItem1Col3.move(400, 225)

            tableItem1Col4 = QLabel((str(listOrderDate[0])), self)
            tableItem1Col4.setProperty("class", "table-item")
            tableItem1Col4.move(600, 225)

            tableItem1Col5 = QPushButton("Delete", self)
            tableItem1Col5.setProperty("class", "btn-del")
            tableItem1Col5.move(1020, 218)
            tableItem1Col5.clicked.connect(lambda: self.delTicket(listOrderDate[0]))

        # ITEM 2

        tableItem2 = QPushButton("", self)
        tableItem2.setProperty("class", "table-item")
        tableItem2.move(90, 270)

        if len(listScreeningID) > 1:
            tableItem2Col1 = QLabel(str(listSeatID[1]), self)
            tableItem2Col1.setProperty("class", "table-item")
            tableItem2Col1.move(120, 285)

            tableItem2Col2 = QLabel(str(listStudioID[1]), self)
            tableItem2Col2.setProperty("class", "table-item")
            tableItem2Col2.move(260, 285)

            tableItem2Col3 = QLabel(str(listScreeningID[1]), self)
            tableItem2Col3.setProperty("class", "table-item")
            tableItem2Col3.move(400, 285)

            tableItem2Col4 = QLabel((str(listOrderDate[1])), self)
            tableItem2Col4.setProperty("class", "table-item")
            tableItem2Col4.move(600, 285)

            tableItem2Col5 = QPushButton("Delete", self)
            tableItem2Col5.setProperty("class", "btn-del")
            tableItem2Col5.move(1020, 278)
            tableItem2Col5.clicked.connect(lambda: self.delTicket(listOrderDate[1]))

        # ITEM 3

        tableItem3 = QPushButton("", self)
        tableItem3.setProperty("class", "table-item")
        tableItem3.move(90, 330)

        if len(listScreeningID) > 2:
            tableItem3Col1 = QLabel(str(listSeatID[2]), self)
            tableItem3Col1.setProperty("class", "table-item")
            tableItem3Col1.move(120, 345)

            tableItem3Col2 = QLabel(str(listStudioID[2]), self)
            tableItem3Col2.setProperty("class", "table-item")
            tableItem3Col2.move(260, 345)

            tableItem3Col3 = QLabel(str(listScreeningID[2]), self)
            tableItem3Col3.setProperty("class", "table-item")
            tableItem3Col3.move(400, 345)

            tableItem3Col4 = QLabel((str(listOrderDate[2])), self)
            tableItem3Col4.setProperty("class", "table-item")
            tableItem3Col4.move(600, 345)

            tableItem3Col5 = QPushButton("Delete", self)
            tableItem3Col5.setProperty("class", "btn-del")
            tableItem3Col5.move(1020, 338)
            tableItem3Col5.clicked.connect(lambda: self.delTicket(listOrderDate[2]))

        # ITEM 4

        tableItem4 = QPushButton("", self)
        tableItem4.setProperty("class", "table-item")
        tableItem4.move(90, 390)

        if len(listScreeningID) > 3:
            tableItem4Col1 = QLabel(str(listSeatID[3]), self)
            tableItem4Col1.setProperty("class", "table-item")
            tableItem4Col1.move(120, 405)

            tableItem4Col2 = QLabel(str(listStudioID[3]), self)
            tableItem4Col2.setProperty("class", "table-item")
            tableItem4Col2.move(260, 405)

            tableItem4Col3 = QLabel(str(listScreeningID[3]), self)
            tableItem4Col3.setProperty("class", "table-item")
            tableItem4Col3.move(400, 405)

            tableItem4Col4 = QLabel((str(listOrderDate[3])), self)
            tableItem4Col4.setProperty("class", "table-item")
            tableItem4Col4.move(600, 405)

            tableItem4Col5 = QPushButton("Delete", self)
            tableItem4Col5.setProperty("class", "btn-del")
            tableItem4Col5.move(1020, 398)
            tableItem4Col5.clicked.connect(lambda: self.delTicket(listOrderDate[3]))

        # ITEM 5

        tableItem5 = QPushButton("", self)
        tableItem5.setProperty("class", "table-item")
        tableItem5.move(90, 450)

        if len(listScreeningID) > 4:
            tableItem5Col1 = QLabel(str(listSeatID[4]), self)
            tableItem5Col1.setProperty("class", "table-item")
            tableItem5Col1.move(120, 465)

            tableItem5Col2 = QLabel(str(listStudioID[4]), self)
            tableItem5Col2.setProperty("class", "table-item")
            tableItem5Col2.move(260, 465)

            tableItem5Col3 = QLabel(str(listScreeningID[4]), self)
            tableItem5Col3.setProperty("class", "table-item")
            tableItem5Col3.move(400, 465)

            tableItem5Col4 = QLabel((str(listOrderDate[4])), self)
            tableItem5Col4.setProperty("class", "table-item")
            tableItem5Col4.move(600, 465)

            tableItem5Col5 = QPushButton("Delete", self)
            tableItem5Col5.setProperty("class", "btn-del")
            tableItem5Col5.move(1020, 458)
            tableItem5Col5.clicked.connect(lambda: self.delTicket(listOrderDate[4]))

        # Pagination

        buttonPrevPage = QPushButton("<< Prev Page", self)
        if (self.page == 1):
            buttonPrevPage.setProperty("class", "btn-disabled")
            buttonPrevPage.move(400, 520)
        else:
            buttonPrevPage.setProperty("class", "btn-page")
            buttonPrevPage.clicked.connect(lambda: self.changePage(self.page - 1))
            buttonPrevPage.move(400, 520)

        buttonNextPage = QPushButton("Next Page >>", self)
        if (countRecords < (self.page * 5 + 1)):
            buttonNextPage.setProperty("class", "btn-disabled")
            buttonNextPage.move(700, 520)
        else:
            buttonNextPage.setProperty("class", "btn-page")
            buttonNextPage.move(700, 520)
            buttonNextPage.clicked.connect(lambda: self.changePage(self.page + 1))

        buttonReturn = QPushButton("<< Main Menu", self)
        buttonReturn.setProperty("class", "option")
        buttonReturn.setStyleSheet("width: 200px; height: 44px; font-size: 20px;")
        buttonReturn.move(90, 660)
        buttonReturn.clicked.connect(lambda: self.returnToMainMenu())

    def logout(self):
        time.sleep(1)
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
        self.close()

    def changePage(self, next):
        self.nextMenu = MenuListTicket(next)
        self.nextMenu.show()
        self.close()

    def delTicket(self, orderTime):
        query = QSqlQuery()
        query.prepare("DELETE FROM ticket WHERE OrderDateTime LIKE :order")
        query.bindValue(':order', orderTime)
        query.exec()
        query.finish()

        self.nextMenu = MenuListTicket(self.page)
        self.nextMenu.show()
        self.close()

    def returnToMainMenu(self):
        self.nextMenu = MainMenuAdmin()
        self.nextMenu.show()
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
        self.nextMenu = None

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
        inputPass.returnPressed.connect(lambda: self.checkCredential(inputPass.text()))

        buttonLogin = QPushButton("Login", self)
        buttonLogin.setProperty("class", "button")
        buttonLogin.clicked.connect(lambda: self.checkCredential(inputPass.text()))
        buttonLogin.move(980, 420)

        self.connectToDB()

    def connectToDB(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(db_path)

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
                    self.close()
                    print('LOGIN SUCCESS')
                    query.finish()
                    os.system('python MenuKasir.py')

                elif query.value('role') == "Admin":
                    time.sleep(1)
                    self.nextMenu = MainMenuAdmin()
                    self.nextMenu.show()
                    self.close()
                    print('LOGIN SUCCESS')
                    query.finish()
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
        
        .btn-page{
            width: 180px;
            height: 44px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 20px;
            line-height: 87.69%;

            color: #FFFFFF;
            background: #EB8446;
            border-radius: 20px;
        }
        
        .btn-disabled{
            width: 180px;
            height: 44px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 20px;
            line-height: 87.69%;

            color: #FFFFFF;
            background: #666666;
            border-radius: 20px;
        }

        .btn-page:hover{
            background: #7C4525;
        }
        
        .btn-edit{
            width: 100px;
            height: 35px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 18px;
            line-height: 87.69%;

            color: #FFFFFF;
            background: #50B058;
            border-radius: 20px;
        }

        .btn-edit:hover{
            background: #27562B;
        }
        
        .btn-del{
            width: 100px;
            height: 35px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 18px;
            line-height: 87.69%;

            color: #FFFFFF;
            background: #F04D4D;
            border-radius: 20px;
        }

        .btn-del:hover{
            background: #632020;
        }
        
        .btn-success{
            width: 135px;
            height: 55px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 25px;
            line-height: 87.69%;

            color: #FFFFFF;
            background: #50B058;
            border-radius: 10px;
        }
        
        .btn-success:hover{
            background: #27562B;
        }
        
        .btn-danger{
            width: 135px;
            height: 55px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 25px;
            line-height: 87.69%;

            color: #FFFFFF;
            background: #F04D4D;
            border-radius: 10px;
        }
        
        .btn-danger:hover{
            background: #632020;
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

        .table-heading{
            width: 1100px;
            height: 50px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 20px;
            line-height: 87.69%;

            color: #FFFFFF;
            background: #EB8446;
            border-radius: 5px;
            text-align: left;
        }
        
        .table-item{
            width: 1100px;
            height: 50px;

            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 20px;
            line-height: 87.69%;

            color: #000000;
            background: #FFFFFF;
            border-radius: 5px;
            text-align: left;
        }
        
        ''')

    mainApp = LoginWindow()
    mainApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
