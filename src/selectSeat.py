import sys, os
from PyQt6 import QtWidgets, QtSql, QtCore, QtGui

current_dir = os.path.dirname(os.path.realpath(__file__))

class SelectSeat():
    def __init__(self, form, window, screeningID, mrow):
        self.dbPath = os.path.join(current_dir, "cineManage.db")
        self.form = form
        self.screeningID = screeningID
        self.mrow = mrow
        self.window = window
        self.activePage = self.form.stackedWidget.setCurrentWidget(self.form.selectPage)
    
    def run(self):
        for i in range(self.mrow):
            self.render(i)
            
        screen = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        screen.setMinimumSize(QtCore.QSize(150, 40))
        screen.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        screen.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #000000;\n"
"            border-radius: 0px;\n"
"        }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #0445A9\n"
"}")
        screen.setText("Screen")
        screen.setObjectName("screen")
        self.form.verticalLayout_2.addWidget(screen)
        self.form.scrollArea.setWidget(self.form.scrollAreaWidgetContents)
        
        """order = dict()
        for i in range(self.mrow):
            for j in range(27):
                item = self.form.verticalLayout_2.itemAt(i).itemAt(j)
                if item != None:
                    if isinstance(item.widget(), QtWidgets.QPushButton):
                        if item.widget().isChecked():
                            order.update({item.widget().objectName():self.screeningID})
            
        if len(order) != 0:
            self.form.bookSeatsButton.setEnabled(True)
            self.form.bookSeatsButton.clicked.connect(self.success())
            
        else:
            self.form.bookSeatsButton.setEnabled(False)"""
                
    
    def render(self, x):
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        horizontalLayout.setObjectName("horizontalLayout")
        seat_1 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_1.setMinimumSize(QtCore.QSize(40, 40))
        seat_1.setMaximumSize(QtCore.QSize(40, 40))
        seat_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_1.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_1.setText("")
        seat_1.setCheckable(True)
        seat_1.setObjectName("seat_1")
        horizontalLayout.addWidget(seat_1)
        seat_2 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_2.setMinimumSize(QtCore.QSize(40, 40))
        seat_2.setMaximumSize(QtCore.QSize(40, 40))
        seat_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_2.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_2.setText("")
        seat_2.setCheckable(True)
        seat_2.setObjectName("seat_2")
        horizontalLayout.addWidget(seat_2)
        seat_3 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_3.setMinimumSize(QtCore.QSize(40, 40))
        seat_3.setMaximumSize(QtCore.QSize(40, 40))
        seat_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_3.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_3.setText("")
        seat_3.setCheckable(True)
        seat_3.setObjectName("seat_3")
        horizontalLayout.addWidget(seat_3)
        seat_4 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_4.setMinimumSize(QtCore.QSize(40, 40))
        seat_4.setMaximumSize(QtCore.QSize(40, 40))
        seat_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_4.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_4.setText("")
        seat_4.setCheckable(True)
        seat_4.setObjectName("seat_4")
        horizontalLayout.addWidget(seat_4)
        seat_5 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_5.setMinimumSize(QtCore.QSize(40, 40))
        seat_5.setMaximumSize(QtCore.QSize(40, 40))
        seat_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_5.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_5.setText("")
        seat_5.setCheckable(True)
        seat_5.setObjectName("seat_5")
        horizontalLayout.addWidget(seat_5)
        seat_6 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_6.setMinimumSize(QtCore.QSize(40, 40))
        seat_6.setMaximumSize(QtCore.QSize(40, 40))
        seat_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_6.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_6.setText("")
        seat_6.setCheckable(True)
        seat_6.setObjectName("seat_6")
        horizontalLayout.addWidget(seat_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        horizontalLayout.addItem(spacerItem4)
        seat_7 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_7.setMinimumSize(QtCore.QSize(40, 40))
        seat_7.setMaximumSize(QtCore.QSize(40, 40))
        seat_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_7.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_7.setText("")
        seat_7.setCheckable(True)
        seat_7.setObjectName("seat_7")
        horizontalLayout.addWidget(seat_7)
        seat_8 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_8.setMinimumSize(QtCore.QSize(40, 40))
        seat_8.setMaximumSize(QtCore.QSize(40, 40))
        seat_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_8.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_8.setText("")
        seat_8.setCheckable(True)
        seat_8.setObjectName("seat_8")
        horizontalLayout.addWidget(seat_8)
        seat_9 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_9.setMinimumSize(QtCore.QSize(40, 40))
        seat_9.setMaximumSize(QtCore.QSize(40, 40))
        seat_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_9.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_9.setText("")
        seat_9.setCheckable(True)
        seat_9.setObjectName("seat_9")
        horizontalLayout.addWidget(seat_9)
        seat_10 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_10.setMinimumSize(QtCore.QSize(40, 40))
        seat_10.setMaximumSize(QtCore.QSize(40, 40))
        seat_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_10.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_10.setText("")
        seat_10.setCheckable(True)
        seat_10.setObjectName("seat_10")
        horizontalLayout.addWidget(seat_10)
        seat_11 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_11.setMinimumSize(QtCore.QSize(40, 40))
        seat_11.setMaximumSize(QtCore.QSize(40, 40))
        seat_11.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_11.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_11.setText("")
        seat_11.setCheckable(True)
        seat_11.setObjectName("seat_11")
        horizontalLayout.addWidget(seat_11)
        seat_12 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_12.setMinimumSize(QtCore.QSize(40, 40))
        seat_12.setMaximumSize(QtCore.QSize(40, 40))
        seat_12.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_12.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_12.setText("")
        seat_12.setCheckable(True)
        seat_12.setObjectName("seat_12")
        horizontalLayout.addWidget(seat_12)
        seat_13 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_13.setMinimumSize(QtCore.QSize(40, 40))
        seat_13.setMaximumSize(QtCore.QSize(40, 40))
        seat_13.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_13.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_13.setText("")
        seat_13.setCheckable(True)
        seat_13.setObjectName("seat_13")
        horizontalLayout.addWidget(seat_13)
        seat_14 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_14.setMinimumSize(QtCore.QSize(40, 40))
        seat_14.setMaximumSize(QtCore.QSize(40, 40))
        seat_14.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_14.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_14.setText("")
        seat_14.setCheckable(True)
        seat_14.setObjectName("seat_14")
        horizontalLayout.addWidget(seat_14)
        seat_15 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_15.setMinimumSize(QtCore.QSize(40, 40))
        seat_15.setMaximumSize(QtCore.QSize(40, 40))
        seat_15.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_15.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_15.setText("")
        seat_15.setCheckable(True)
        seat_15.setObjectName("seat_15")
        horizontalLayout.addWidget(seat_15)
        seat_16 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_16.setMinimumSize(QtCore.QSize(40, 40))
        seat_16.setMaximumSize(QtCore.QSize(40, 40))
        seat_16.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_16.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_16.setText("")
        seat_16.setCheckable(True)
        seat_16.setObjectName("seat_16")
        horizontalLayout.addWidget(seat_16)
        seat_17 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_17.setMinimumSize(QtCore.QSize(40, 40))
        seat_17.setMaximumSize(QtCore.QSize(40, 40))
        seat_17.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_17.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_17.setText("")
        seat_17.setCheckable(True)
        seat_17.setObjectName("seat_17")
        horizontalLayout.addWidget(seat_17)
        seat_18 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_18.setMinimumSize(QtCore.QSize(40, 40))
        seat_18.setMaximumSize(QtCore.QSize(40, 40))
        seat_18.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_18.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_18.setText("")
        seat_18.setCheckable(True)
        seat_18.setObjectName("seat_18")
        horizontalLayout.addWidget(seat_18)
        seat_19 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_19.setMinimumSize(QtCore.QSize(40, 40))
        seat_19.setMaximumSize(QtCore.QSize(40, 40))
        seat_19.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_19.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_19.setText("")
        seat_19.setCheckable(True)
        seat_19.setObjectName("seat_19")
        horizontalLayout.addWidget(seat_19)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        horizontalLayout.addItem(spacerItem5)
        seat_20 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_20.setMinimumSize(QtCore.QSize(40, 40))
        seat_20.setMaximumSize(QtCore.QSize(40, 40))
        seat_20.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_20.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_20.setText("")
        seat_20.setCheckable(True)
        seat_20.setObjectName("seat_20")
        horizontalLayout.addWidget(seat_20)
        seat_21 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_21.setMinimumSize(QtCore.QSize(40, 40))
        seat_21.setMaximumSize(QtCore.QSize(40, 40))
        seat_21.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_21.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_21.setText("")
        seat_21.setCheckable(True)
        seat_21.setObjectName("seat_21")
        horizontalLayout.addWidget(seat_21)
        seat_22 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_22.setMinimumSize(QtCore.QSize(40, 40))
        seat_22.setMaximumSize(QtCore.QSize(40, 40))
        seat_22.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_22.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_22.setText("")
        seat_22.setCheckable(True)
        seat_22.setObjectName("seat_22")
        horizontalLayout.addWidget(seat_22)
        seat_23 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_23.setMinimumSize(QtCore.QSize(40, 40))
        seat_23.setMaximumSize(QtCore.QSize(40, 40))
        seat_23.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_23.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_23.setText("")
        seat_23.setCheckable(True)
        seat_23.setObjectName("seat_23")
        horizontalLayout.addWidget(seat_23)
        seat_24 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_24.setMinimumSize(QtCore.QSize(40, 40))
        seat_24.setMaximumSize(QtCore.QSize(40, 40))
        seat_24.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_24.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_24.setText("")
        seat_24.setCheckable(True)
        seat_24.setObjectName("seat_24")
        horizontalLayout.addWidget(seat_24)
        seat_25 = QtWidgets.QPushButton(self.form.scrollAreaWidgetContents)
        seat_25.setMinimumSize(QtCore.QSize(40, 40))
        seat_25.setMaximumSize(QtCore.QSize(40, 40))
        seat_25.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        seat_25.setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #3084D1;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
        seat_25.setText("")
        seat_25.setCheckable(True)
        seat_25.setObjectName("seat_25")
        horizontalLayout.addWidget(seat_25)
        
        
        seats = (seat_1, seat_2, seat_3, seat_4, seat_5, seat_6, seat_7, seat_8, seat_9, seat_10, seat_11, seat_12, seat_13, seat_14, seat_15, 
                 seat_16, seat_17, seat_18, seat_19, seat_20, seat_21, seat_22, seat_23, seat_24, seat_25)
            
        for i in range(25):
            name = str(f"{chr(65+x)}{i+1}")
            seats[i].setText(name)
            seats[i].setObjectName(name)
            
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM ticket WHERE ticket.screeningid=:screeningID;")
        query.bindValue(":screeningID", self.screeningID)
        query.exec()
        if query.first():
            for i in range(25):
                if query.value("seatid") == seats[i].objectName():
                    seats[i].setStyleSheet("QPushButton {\n"
"            font-family: \'Inter\';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 20px;\n"
"            line-height: 87.69%;\n"
"\n"
"            color: #FFFFFF;\n"
"            background: #EB311F;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton:on {\n"
"    background: #0445A9\n"
"}")
                    seats[i].setCheckable(False)
                    seats[i].setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        
        self.form.verticalLayout_2.addLayout(horizontalLayout)
        
    def success(self):
        self.activePage = self.form.stackedWidget.setCurrentWidget(self.form.successPage)