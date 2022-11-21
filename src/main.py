import time

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QDialog, QListWidget
)
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

import sys
import os
import math

current_dir = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(current_dir, "cineManage.db")

class MainMenuCashier(QWidget):
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
        self.nextMenu = LoginWindow()
        self.nextMenu.show()
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

        buttonRiwayatPemesanan = QPushButton("Order History", self)
        buttonRiwayatPemesanan.setProperty("class", "option")
        # buttonRiwayatPemesanan.clicked.connect()
        buttonRiwayatPemesanan.move(430, 490)

        buttonEditStudio = QPushButton("Edit Studio", self)
        buttonEditStudio.setProperty("class", "option")
        buttonEditStudio.clicked.connect(self.editStudio)
        buttonEditStudio.move(430, 600)

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

    # def debug(self):
    #     dlg = QDialog(self)
    #     dlg.setWindowTitle("CineManage - Debug")
    #     dlg.exec()

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
        buttonUser.setProperty("class", "button")
        buttonUser.setStyleSheet("background: #F04D4D")
        buttonUser.move(110, 45)

        labelTitleMenu = QLabel("Add New Studio", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(430, 20)

        #Middle

        labelNamaStudio = QLabel("Nama Studio *", self)
        labelNamaStudio.setProperty("class", "normal")
        labelNamaStudio.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelNamaStudio.move(350, 190)

        inputNamaStudio = QLineEdit(self)
        inputNamaStudio.setFixedSize(600, 38)
        inputNamaStudio.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputNamaStudio.setPlaceholderText("Input Nama Studio...")
        inputNamaStudio.move(350, 230)

        labelKapasitasStudio = QLabel("Kapasitas Studio *", self)
        labelKapasitasStudio.setProperty("class", "normal")
        labelKapasitasStudio.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelKapasitasStudio.move(350, 300)

        inputKapasitasStudio = QLineEdit(self)
        inputKapasitasStudio.setFixedSize(600, 38)
        inputKapasitasStudio.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputKapasitasStudio.setPlaceholderText("Input Kapasitas Studio...")
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
            query.bindValue(':name', name)
            query.bindValue(':capacity', int(capacity))
            query.exec()

            self.nextMenu = MenuListStudio(1)
            self.nextMenu.show()
            self.close()

        else:
            print("Error required input not filled")

        # Debug
        # print(query.lastError().text())

class MenuEditStudio(QWidget):
    def __init__(self, studioId, studioName, studioCapacity):
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
        buttonUser.setProperty("class", "button")
        buttonUser.setStyleSheet("background: #F04D4D")
        buttonUser.move(110, 45)

        labelTitleMenu = QLabel("Edit Studio", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(480, 20)

        #Middle

        labelNamaStudio = QLabel("Nama Studio *", self)
        labelNamaStudio.setProperty("class", "normal")
        labelNamaStudio.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelNamaStudio.move(350, 190)

        inputNamaStudio = QLineEdit(self)
        inputNamaStudio.setFixedSize(600, 38)
        inputNamaStudio.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputNamaStudio.setPlaceholderText("Input Nama Studio...")
        inputNamaStudio.setText(studioName)
        inputNamaStudio.move(350, 230)

        labelKapasitasStudio = QLabel("Kapasitas Studio *", self)
        labelKapasitasStudio.setProperty("class", "normal")
        labelKapasitasStudio.setStyleSheet("font-weight: 700; background: #FFDE59;")
        labelKapasitasStudio.move(350, 300)

        inputKapasitasStudio = QLineEdit(self)
        inputKapasitasStudio.setFixedSize(600, 38)
        inputKapasitasStudio.setStyleSheet("background: #F5F5F5; padding-left: 5px; font-size: 16px;")
        inputKapasitasStudio.setPlaceholderText("Input Kapasitas Studio...")
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
            query.bindValue(':name', name)
            query.bindValue(':capacity', int(capacity))
            query.bindValue(':id', studioId)
            query.exec()

            self.nextMenu = MenuListStudio(1)
            self.nextMenu.show()
            self.close()

        else:
            print("Error required input not filled")

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
        buttonUser.setProperty("class", "button")
        buttonUser.setStyleSheet("background: #F04D4D")
        buttonUser.move(110, 45)

        labelTitleMenu = QLabel("List Studio", self)
        labelTitleMenu.setProperty("class", "heading")
        labelTitleMenu.move(480, 20)

        # Middle

        # Query For Debug

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(db_path)

        if not db.open():
            print("CONNECTION FAILED")
        else:
            print("CONNECTED TO DB SUCCESSFULLY")

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
        tableHeaderCol3.move(770, 165)

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
            tableItem1Col2.move(275, 225)

            tableItem1Col3 = QLabel(str(listKapasitas[0]), self)
            tableItem1Col3.setProperty("class", "table-item")
            tableItem1Col3.move(805, 225)

            tableItem1Col4 = QPushButton("Edit", self)
            tableItem1Col4.setProperty("class", "btn-edit")
            tableItem1Col4.move(950, 218)
            tableItem1Col4.clicked.connect(lambda: self.editStudio(str(listStudioID[0]), str(listStudioName[0]), str(listKapasitas[0])))

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
            tableItem2Col4.clicked.connect(lambda: self.editStudio(str(listStudioID[1]), str(listStudioName[1]), str(listKapasitas[1])))

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
            tableItem3Col4.clicked.connect(lambda: self.editStudio(str(listStudioID[2]), str(listStudioName[2]), str(listKapasitas[2])))

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
            tableItem4Col4.clicked.connect(lambda: self.editStudio(str(listStudioID[3]), str(listStudioName[3]), str(listKapasitas[3])))

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
            tableItem3Col4.clicked.connect(lambda: self.editStudio(str(listStudioID[4]), str(listStudioName[4]), str(listKapasitas[4])))

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
        if(countRecords < (self.page * 5)):
            buttonNextPage.setProperty("class", "btn-disabled")
            buttonNextPage.move(700, 600)
        else:
            buttonNextPage.setProperty("class", "btn-page")
            buttonNextPage.move(700, 600)
            buttonNextPage.clicked.connect(lambda : self.changePage(self.page+1))

        buttonReturn = QPushButton("<< Main Menu", self)
        buttonReturn.setProperty("class", "button")
        buttonReturn.setStyleSheet("width: 200px; height: 44px")
        buttonReturn.move(30, 660)
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

    def editStudio(self, studioId, studioName, studioCapacity):
        self.nextMenu = MenuEditStudio(studioId, studioName, studioCapacity)
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
                    time.sleep(1)
                    self.nextMenu = MainMenuCashier()
                    self.nextMenu.show()
                    self.close()
                    print('LOGIN SUCCESS')
                    query.finish()
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

    mainApp = MenuListStudio(1)
    mainApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
