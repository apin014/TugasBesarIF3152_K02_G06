import sys
from PyQt6 import QtWidgets
from UI_Kasir import Ui_MainWindow
from screeningInfo import ScreeningInfo
from ticketOrderHistory import TicketOrderHistory
from orderTicket import OrderTicket
from selectSeat import SelectSeat

class MainMenuCashier:
    def __init__(self):
        self.next = None
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.screeningMenu)
        
        ScreeningInfo(self.ui).run()
        TicketOrderHistory(self.ui).run()
        OrderTicket(self.ui).run()
        
        self.ui.orderTicketButton.clicked.connect(self.changeToOrder)
        self.ui.screeningInfoButton.clicked.connect(self.changeToScreeningInfo)
        self.ui.orderHistoryButton.clicked.connect(self.changeToHistory)
        
    def show(self):
        self.mainWindow.show()
        
    def changeToOrder(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.orderMenu)
    
    def changeToScreeningInfo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.screeningMenu)
        
    def changeToHistory(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.historyMenu)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainMenuCashier = MainMenuCashier()
    MainMenuCashier.show()
    sys.exit(app.exec())