import sys, os
from PyQt6 import QtWidgets, QtSql, QtCore, QtGui

current_dir = os.path.dirname(os.path.realpath(__file__))
class ScreeningInfo():
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
        query.exec("SELECT * FROM film;")
        
        if query.first():
            self.render(query)
            while query.next():
                self.render(query)
    
    def render(self, query):
        screeningInfoFrame = QtWidgets.QFrame(self.mainWindow.screeningScrollAreaWidgetContents)
        screeningInfoFrame.setMinimumSize(QtCore.QSize(1047, 576))
        screeningInfoFrame.setMaximumSize(QtCore.QSize(1047, 576))
        screeningInfoFrame.setStyleSheet("QFrame {background: #FFFFFF;border-radius: 20px }")
        screeningInfoFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        screeningInfoFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        screeningInfoFrame.setObjectName("screeningInfoFrame")
        gridLayout = QtWidgets.QGridLayout(screeningInfoFrame)
        gridLayout.setObjectName("gridLayout_5")
        deskripsiFilm = QtWidgets.QLabel(screeningInfoFrame)
        deskripsiFilm.setMinimumSize(QtCore.QSize(0, 250))
        deskripsiFilm.setMaximumSize(QtCore.QSize(16777215, 500))
        deskripsiFilm.setStyleSheet("QLabel {font-size: 14px}")
        deskripsiFilm.setScaledContents(True)
        deskripsiFilm.setWordWrap(True)
        deskripsiFilm.setObjectName("deskripsiFilm")
        gridLayout.addWidget(deskripsiFilm, 1, 1, 1, 1)
        judulFilm = QtWidgets.QLabel(screeningInfoFrame)
        judulFilm.setMinimumSize(QtCore.QSize(0, 40))
        judulFilm.setMaximumSize(QtCore.QSize(16777215, 40))
        judulFilm.setStyleSheet("QLabel {\n"
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
        judulFilm.setScaledContents(True)
        judulFilm.setObjectName("judulFilm")
        gridLayout.addWidget(judulFilm, 0, 0, 1, 1)
        posterFilm = QtWidgets.QLabel(screeningInfoFrame)
        posterFilm.setMinimumSize(QtCore.QSize(375, 500))
        posterFilm.setMaximumSize(QtCore.QSize(375, 500))
        posterFilm.setScaledContents(True)
        posterFilm.setObjectName("posterFilm")
        gridLayout.addWidget(posterFilm, 1, 0, 1, 1)
        playingOrNot = QtWidgets.QLabel(screeningInfoFrame)
        playingOrNot.setMinimumSize(QtCore.QSize(0, 200))
        playingOrNot.setMaximumSize(QtCore.QSize(16777215, 200))
        playingOrNot.setStyleSheet("QLabel {font-size: 14px}")
        playingOrNot.setScaledContents(True)
        playingOrNot.setObjectName("playingOrNot")
        gridLayout.addWidget(playingOrNot, 2, 1, 1, 1)
        durasiFilm = QtWidgets.QLabel(screeningInfoFrame)
        durasiFilm.setMinimumSize(QtCore.QSize(0, 40))
        durasiFilm.setMaximumSize(QtCore.QSize(16777215, 40))
        durasiFilm.setStyleSheet("QLabel {font-size: 18px}")
        durasiFilm.setScaledContents(True)
        durasiFilm.setObjectName("durasiFilm")
        gridLayout.addWidget(durasiFilm, 0, 1, 1, 1)
        
        judulFilm.setText(query.value(1))
        durasiFilm.setText("Runtime: " + str(query.value(2)) + " Minute(s)")
        deskripsiFilm.setText(query.value(3))
        posterFilm.setPixmap(QtGui.QPixmap(query.value(4)))
        query_ = QtSql.QSqlQuery()
        query_.prepare(f"SELECT * FROM screening where screening.filmtitle=:filmTitle;")
        query_.bindValue(":filmTitle", judulFilm.text())
        if (not query_.exec()):
            QtCore.qDebug(query_.lastError().text())
        if (not query_.first()):
            playingOrNot.setText("COMING SOON")
        else:
            playingOrNot.setText("PLAYING NOW")
            getTickets = QtWidgets.QPushButton(screeningInfoFrame)
            getTickets.setMinimumSize(QtCore.QSize(150, 80))
            getTickets.setMaximumSize(QtCore.QSize(150, 80))
            getTickets.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            getTickets.setStyleSheet("QPushButton {\n"
    "            font-family: \'Inter\';\n"
    "            font-style: normal;\n"
    "            font-weight: 700;\n"
    "            font-size: 20px;\n"
    "            line-height: 87.69%;\n"
    "\n"
    "            color: #FFFFFF;\n"
    "            background: #32F478;\n"
    "            border-radius: 20px;\n"
    "        }\n"
    "\n"
    "QPushButton:pressed {\n"
    "    background: #25A654 \n"
    "}")
            
            getTickets.setObjectName("getTickets")
            getTickets.setText("Get Tickets")
            gridLayout.addWidget(getTickets, 2, 2, 1, 1)
                
        
        self.mainWindow.verticalLayout_4.addWidget(screeningInfoFrame)