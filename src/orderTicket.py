import sys, os
from PyQt6 import QtWidgets, QtSql, QtCore, QtGui
from UI_SelectSeat import Ui_Form
from selectSeat import SelectSeat


current_dir = os.path.dirname(os.path.realpath(__file__))
class OrderTicket():
    def __init__(self, mainWindow):
        self.dbPath = os.path.join(current_dir, "cineManage.db")
        self.mainWindow = mainWindow
        self.openSelection = None
        
    def run(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.dbPath)
        if not db.open():
            print("CONNECTION FAILED")
            return
        else:
            print("CONNECTED TO DB SUCCESSFULLY")
        query = QtSql.QSqlQuery()
        query.exec("SELECT * FROM screening;")
        
        if query.first():
            self.render(query)
            while query.next():
                self.render(query)
    
    def render(self, query):
        orderFrame = QtWidgets.QFrame(self.mainWindow.orderScrollAreaWidgetContents_6)
        orderFrame.setMinimumSize(QtCore.QSize(1047, 275))
        orderFrame.setMaximumSize(QtCore.QSize(1047, 275))
        orderFrame.setStyleSheet("QFrame {background: #FFFFFF; border-radius: 20px }")
        orderFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        orderFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        orderFrame.setObjectName("orderFrame")
        gridLayout_7 = QtWidgets.QGridLayout(orderFrame)
        gridLayout_7.setObjectName("gridLayout_7")
        judulFilmOrderPage = QtWidgets.QLabel(orderFrame)
        judulFilmOrderPage.setMaximumSize(QtCore.QSize(753, 16777215))
        judulFilmOrderPage.setStyleSheet("QLabel {\n"
"            width: 89px;\n"
"            height: 18px;\n"
"\n"
"            font-family: \'Roboto\';\n"
"            font-style: normal;\n"
"            font-weight: 600;\n"
"            font-size: 20px;\n"
"            line-height: 18px;\n"
"\n"
"            color: #000000;\n"
"            background: #FFFFFF;\n"
"}")
        judulFilmOrderPage.setScaledContents(True)
        judulFilmOrderPage.setWordWrap(True)
        judulFilmOrderPage.setObjectName("judulFilmOrderPage")
        gridLayout_7.addWidget(judulFilmOrderPage, 0, 0, 1, 1)
        jadwal1 = QtWidgets.QPushButton(orderFrame)
        jadwal1.setMinimumSize(QtCore.QSize(150, 80))
        jadwal1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        jadwal1.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 20px;\n"
"        }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #0445A9\n"
"}")
        jadwal1.setObjectName("jadwal1")
        gridLayout_7.addWidget(jadwal1, 1, 0, 1, 1)
        jadwal2 = QtWidgets.QPushButton(orderFrame)
        jadwal2.setMinimumSize(QtCore.QSize(150, 80))
        jadwal2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        jadwal2.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 20px;\n"
"        }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #0445A9\n"
"}")
        jadwal2.setObjectName("jadwal2")
        gridLayout_7.addWidget(jadwal2, 1, 1, 1, 1)
        studioOrderPage = QtWidgets.QLabel(orderFrame)
        studioOrderPage.setMaximumSize(QtCore.QSize(250, 16777215))
        studioOrderPage.setStyleSheet("QLabel {\n"
"            width: 89px;\n"
"            height: 18px;\n"
"\n"
"            font-family: \'Roboto\';\n"
"            font-style: normal;\n"
"            font-weight: 600;\n"
"            font-size: 20px;\n"
"            line-height: 18px;\n"
"\n"
"            color: #000000;\n"
"            background: #FFFFFF;\n"
"}")
        studioOrderPage.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        studioOrderPage.setObjectName("studioOrderPage")
        gridLayout_7.addWidget(studioOrderPage, 0, 3, 1, 1)
        jadwal4 = QtWidgets.QPushButton(orderFrame)
        jadwal4.setMinimumSize(QtCore.QSize(150, 80))
        jadwal4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        jadwal4.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 20px;\n"
"        }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #0445A9\n"
"}")
        jadwal4.setObjectName("jadwal4")
        gridLayout_7.addWidget(jadwal4, 1, 3, 1, 1)
        jadwal3 = QtWidgets.QPushButton(orderFrame)
        jadwal3.setMinimumSize(QtCore.QSize(150, 80))
        jadwal3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        jadwal3.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 20px;\n"
"        }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #0445A9\n"
"}")
        jadwal3.setObjectName("jadwal3")
        gridLayout_7.addWidget(jadwal3, 1, 2, 1, 1)
        tanggalPenayangan = QtWidgets.QLabel(orderFrame)
        tanggalPenayangan.setMaximumSize(QtCore.QSize(16777215, 16777215))
        tanggalPenayangan.setStyleSheet("QLabel {\n"
"            width: 89px;\n"
"            height: 18px;\n"
"\n"
"            font-family: \'Roboto\';\n"
"            font-style: normal;\n"
"            font-weight: 400;\n"
"            font-size: 18px;\n"
"            line-height: 18px;\n"
"\n"
"            color: #000000;\n"
"            background: #FFFFFF;\n"
"}")
        tanggalPenayangan.setScaledContents(True)
        tanggalPenayangan.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        tanggalPenayangan.setObjectName("tanggalPenayangan")
        gridLayout_7.addWidget(tanggalPenayangan, 0, 1, 1, 2)
        
        query_ = QtSql.QSqlQuery()
        query_.prepare(f"SELECT * FROM studio where studio.studioid=:studioID;")
        query_.bindValue(":studioID", query.value("studioid"))
        if (not query_.exec()):
            QtCore.qDebug(query_.lastError().text())
        
        judulFilmOrderPage.setText(query.value("filmtitle"))
        tanggalPenayangan.setText(query.value("date"))
        if (query_.first()):
            studioOrderPage.setText(query_.value("name"))
        j = (jadwal1, jadwal2, jadwal3, jadwal4)
        for i in range(4):
            if len(j[i].text()) == 0:
                j[i].setText(query.value("starttime") + " - " + query.value("endtime"))
                screeningID = query.value("screeningid")
                
                row = int(query_.value("capacity")/25)
                j[i].clicked.connect(lambda:self.selectSeat(screeningID, row))
                break
        for i in range(4):
            if len(j[i].text()) == 0:
                gridLayout_7.removeWidget(j[i])
        
        self.mainWindow.verticalLayout_5.addWidget(orderFrame)
        
    def selectSeat(self, screeningID, mrow):
        order = dict()
        self.openSelection = QtWidgets.QMainWindow()
        ui = Ui_Form()
        ui.setupUi(self.openSelection)
        select = SelectSeat(ui, self.openSelection, screeningID, mrow)
        select.run()
        self.openSelection.show()
        for i in range(select.mrow):
            for j in range(27):
                item = select.form.verticalLayout_2.itemAt(i).itemAt(j)
                if item != None:
                    if isinstance(item.widget(), QtWidgets.QPushButton):
                        if item.widget().isChecked():
                            order.update({item.widget().objectName():select.screeningID})
                        else:
                            if item.widget().objectName() in order.keys():
                                order.pop(item.widget().objectName())
            
        if len(order) != 0:
            select.form.bookSeatsButton.setEnabled(True)
            select.form.bookSeatsButton.clicked.connect(select.success())
            
        else:
            select.form.bookSeatsButton.setEnabled(False)