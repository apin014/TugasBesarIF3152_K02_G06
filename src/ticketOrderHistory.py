import sys, os
from PyQt6 import QtWidgets, QtSql, QtCore, QtGui

current_dir = os.path.dirname(os.path.realpath(__file__))
class TicketOrderHistory():
    def __init__(self, mainWindow):
        self.dbPath = os.path.join(current_dir, "cineManage.db")
        self.mainWindow = mainWindow
        
    def run(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.dbPath)
        if not db.open():
            print("CONNECTION FAILED")
            return
        else:
            print("CONNECTED TO DB SUCCESSFULLY")
        query = QtSql.QSqlQuery()
        query.exec("SELECT * FROM ticket ORDER BY DATETIME(orderdatetime, 'auto') DESC;")
        
        if query.first():
            self.render(query)
            while query.next():
                self.render(query)
    
    def render(self, query):
        ticketHistoryFrame = QtWidgets.QFrame(self.mainWindow.ticketScrollAreaWidgetContents_7)
        ticketHistoryFrame.setMinimumSize(QtCore.QSize(500, 350))
        ticketHistoryFrame.setMaximumSize(QtCore.QSize(500, 350))
        ticketHistoryFrame.setStyleSheet("QFrame {background: #FFFFFF;border-radius:20px }")
        ticketHistoryFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        ticketHistoryFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        ticketHistoryFrame.setObjectName("ticketHistoryFrame")
        gridLayout_8 = QtWidgets.QGridLayout(ticketHistoryFrame)
        gridLayout_8.setObjectName("gridLayout_8")
        jamTiket = QtWidgets.QLabel(ticketHistoryFrame)
        jamTiket.setStyleSheet("QLabel {font-size: 14px}")
        jamTiket.setScaledContents(True)
        jamTiket.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        jamTiket.setObjectName("jamTiket")
        gridLayout_8.addWidget(jamTiket, 3, 1, 1, 1)
        barisKursi = QtWidgets.QLabel(ticketHistoryFrame)
        barisKursi.setStyleSheet("QLabel {font-size: 14px}")
        barisKursi.setScaledContents(True)
        barisKursi.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        barisKursi.setObjectName("barisKursi")
        gridLayout_8.addWidget(barisKursi, 3, 2, 1, 1)
        tanggalTiket = QtWidgets.QLabel(ticketHistoryFrame)
        tanggalTiket.setStyleSheet("QLabel {font-size: 14px}")
        tanggalTiket.setScaledContents(True)
        tanggalTiket.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        tanggalTiket.setObjectName("tanggalTiket")
        gridLayout_8.addWidget(tanggalTiket, 3, 0, 1, 1)
        nomorKursi = QtWidgets.QLabel(ticketHistoryFrame)
        nomorKursi.setStyleSheet("QLabel {font-size: 14px}")
        nomorKursi.setScaledContents(True)
        nomorKursi.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        nomorKursi.setObjectName("nomorKursi")
        gridLayout_8.addWidget(nomorKursi, 3, 3, 1, 1)
        idTiket = QtWidgets.QLabel(ticketHistoryFrame)
        idTiket.setStyleSheet("QLabel {font-size: 14px}")
        idTiket.setScaledContents(True)
        idTiket.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        idTiket.setObjectName("idTiket")
        gridLayout_8.addWidget(idTiket, 4, 1, 1, 3)
        judulFilmTicketPage = QtWidgets.QLabel(ticketHistoryFrame)
        judulFilmTicketPage.setStyleSheet("QLabel {\n"
"            width: 89px;\n"
"            height: 18px;\n"
"\n"
"            font-family: \'Roboto\';\n"
"            font-style: normal;\n"
"            font-weight: 600;\n"
"            font-size: 18px;\n"
"            line-height: 18px;\n"
"\n"
"            color: #000000;\n"
"            background: #FFFFFF;\n"
"}")
        judulFilmTicketPage.setScaledContents(True)
        judulFilmTicketPage.setObjectName("judulFilmTicketPage")
        gridLayout_8.addWidget(judulFilmTicketPage, 0, 0, 1, 2)
        studioTicketPage = QtWidgets.QLabel(ticketHistoryFrame)
        studioTicketPage.setStyleSheet("QLabel {\n"
"            width: 89px;\n"
"            height: 18px;\n"
"\n"
"            font-family: \'Roboto\';\n"
"            font-style: normal;\n"
"            font-weight: 600;\n"
"            font-size: 18px;\n"
"            line-height: 18px;\n"
"\n"
"            color: #000000;\n"
"            background: #FFFFFF;\n"
"}")
        studioTicketPage.setScaledContents(True)
        studioTicketPage.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        studioTicketPage.setObjectName("studioTicketPage")
        gridLayout_8.addWidget(studioTicketPage, 0, 2, 1, 2)
        
        query_ = QtSql.QSqlQuery()
        query_.prepare("SELECT * FROM screening WHERE screeningid=:screeningID")
        query_.bindValue(":screeningID", query.value(2))
        if (not query_.exec()):
            QtCore.qDebug(query_.lastError().text())
        
        query_2 = QtSql.QSqlQuery()
        query_2.prepare("SELECT name FROM studio WHERE studioid=:studioID")
        query_2.bindValue(":studioID", query.value(1))
        if (not query_2.exec()):
            QtCore.qDebug(query_2.lastError().text())
        
        if (query_.first() and query_2.first()):
            judulFilmTicketPage.setText(query_.value(2))
            studioTicketPage.setText(query_2.value(0))
            jamTiket.setText("Time:\n" + query_.value(3) + " - " + query_.value(4))
            tanggalTiket.setText("Date:\n" + query_.value(5))
            barisKursi.setText("Seat Row:\n" + query.value(0)[0])
            nomorKursi.setText("Seat No:\n" + query.value(0)[1])
            idTiket.setText("Ticket No.: " + query.value("seatid")+"-"+query.value("orderdatetime"))
        
        self.mainWindow.verticalLayout_6.addWidget(ticketHistoryFrame)