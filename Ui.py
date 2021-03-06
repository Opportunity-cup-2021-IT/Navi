import datetime
import plotly.express as px
import pandas as pd
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import DataSender
from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidgetItem




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):  # Настройки основоного окна
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 681)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet("background-color: rgb(169,184,250);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.programm_name = QtWidgets.QLabel(self.centralwidget)
        self.programm_name.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.programm_name.sizePolicy().hasHeightForWidth())
        self.programm_name.setSizePolicy(sizePolicy)
        self.programm_name.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.programm_name.setFont(font)
        self.programm_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.programm_name.setStyleSheet("background-color: rgb(36,102,145);\n")
        self.programm_name.setAlignment(QtCore.Qt.AlignCenter)
        self.programm_name.setObjectName("programm_name")
        self.verticalLayout_5.addWidget(self.programm_name)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_5.addWidget(self.line_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_find = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_find.sizePolicy().hasHeightForWidth())
        self.file_find.setSizePolicy(sizePolicy)
        self.file_find.setStyleSheet("color: rgb(36,102,145);")
        self.file_find.setObjectName("file_find")
        self.horizontalLayout.addWidget(self.file_find)
        self.file_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_line.sizePolicy().hasHeightForWidth())
        self.file_line.setSizePolicy(sizePolicy)
        self.file_line.setObjectName("file_line")
        self.horizontalLayout.addWidget(self.file_line)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_5.addWidget(self.line_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_4.addWidget(self.line_10)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_3.addWidget(self.line_9)
        self.start_button2 = QtWidgets.QPushButton(self.centralwidget)
        self.start_button2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.file_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.file_find.setStyleSheet("background-color: rgb(255, 255, 255);")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button2.sizePolicy().hasHeightForWidth())
        self.start_button2.setSizePolicy(sizePolicy)
        self.start_button2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.start_button2.setAutoDefault(False)
        self.start_button2.setObjectName("start_button2")
        self.verticalLayout_3.addWidget(self.start_button2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0,0,0);\n"
                                   "background-color: rgb(169,184,250);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout.addWidget(self.line_8)
        self.start_button1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button1.sizePolicy().hasHeightForWidth())
        self.start_button1.setSizePolicy(sizePolicy)
        self.start_button1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.start_button1.setAutoFillBackground(False)
        self.start_button1.setObjectName("start_button1")
        self.verticalLayout.addWidget(self.start_button1, 0, QtCore.Qt.AlignHCenter)
        self.start_button1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_function()

    def retranslateUi(self, MainWindow):  # редакция текста кнопок и лэйблов главного окна
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Navi"))
        self.programm_name.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-style:italic; color:#55ffff;\">Navi</span></p></body></html>"))
        self.file_find.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "File"))
        self.label_6.setText(
            _translate("MainWindow", "<html><head/><body><p>Рассчитать критичность событий</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "-Посмотреть количество зависимых событий"))
        self.label_7.setText(_translate("MainWindow", "-Список событий с их коэфицентом критичности"))
        self.start_button2.setText(_translate("MainWindow", "Начать"))
        self.label_3.setText(
            _translate("MainWindow", "<html><head/><body><p>Рассчитать стоимость переноса</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "-Диаграмма Ганта"))
        self.label_4.setText(_translate("MainWindow", "-Финансовые потери из-за изменения даты"))
        self.start_button1.setText(_translate("MainWindow", "Начать"))

    def add_function(self):  # Привзяка кнопок открытия окон
        self.start_button1.clicked.connect(self.open_firstwind)
        self.start_button2.clicked.connect(self.open_secondwind)
        self.file_find.clicked.connect(self.open_dialog_box)

    def openmain(self):  # Открытие главного окна
        firstwind.close()
        secondwind.close()
        MainWindow.show()

    def open_firstwind(self):  # Открытие первого окна
        MainWindow.close()
        firstwind.show()

    def open_secondwind(self):  # Открытие второго окна
        MainWindow.close()
        secondwind.show()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]

        self.file_line.setText(path)
        DataSender.init(path)

    def get_path(self):
        return self.file_line


class Ui_FirstWindow(Ui_MainWindow):
    def setupUi(self, FirstWindow):  # Настройки первого окна
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(780, 681)
        FirstWindow.setStyleSheet("background-color: rgb(169,184,250);")
        self.verticalLayout = QtWidgets.QVBoxLayout(FirstWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.backbutton1 = QtWidgets.QPushButton(FirstWindow)
        self.backbutton1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backbutton1.setObjectName("backbutton1")
        self.horizontalLayout_3.addWidget(self.backbutton1)
        self.line_2 = QtWidgets.QFrame(FirstWindow)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(FirstWindow)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.idline1 = QtWidgets.QLineEdit(FirstWindow)
        self.idline1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idline1.setObjectName("idline1")
        self.horizontalLayout.addWidget(self.idline1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.line_3 = QtWidgets.QFrame(FirstWindow)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(FirstWindow)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit12 = QtWidgets.QLineEdit(FirstWindow)
        self.lineEdit12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit12.setObjectName("lineEdit12")
        self.horizontalLayout_2.addWidget(self.lineEdit12)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gobutton1 = QtWidgets.QPushButton(FirstWindow)
        self.gobutton1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gobutton1.setObjectName("gobutton1")
        self.horizontalLayout_3.addWidget(self.gobutton1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(FirstWindow)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.diagramm_label = QtWidgets.QLabel(FirstWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diagramm_label.sizePolicy().hasHeightForWidth())
        self.diagramm_label.setSizePolicy(sizePolicy)
        self.diagramm_label.setStyleSheet("background-color: rgb(169,184,250);\n"
                                          "")
        self.diagramm_label.setText("")
        self.diagramm_label.setScaledContents(True)
        self.diagramm_label.setObjectName("diagramm_label")
        self.verticalLayout.addWidget(self.diagramm_label)
        self.line_4 = QtWidgets.QFrame(FirstWindow)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(FirstWindow)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.line_5 = QtWidgets.QFrame(FirstWindow)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_4.addWidget(self.line_5)
        self.value_label = QtWidgets.QLabel(FirstWindow)
        self.value_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_label.sizePolicy().hasHeightForWidth())
        self.value_label.setSizePolicy(sizePolicy)
        self.value_label.setText("")
        self.value_label.setObjectName("value_label")
        self.horizontalLayout_4.addWidget(self.value_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)
        self.add_function1()

    def retranslateUi(self, FirstWindow):  # редакция текста кнопок и лэйблов первого окна
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "Navi"))
        self.backbutton1.setText(_translate("FirstWindow", "Назад"))
        self.label.setText(_translate("FirstWindow", "ID события"))
        self.label_2.setText(_translate("FirstWindow", "Срок переноса"))
        self.gobutton1.setText(_translate("FirstWindow", "Начать"))
        self.label_4.setText(_translate("FirstWindow", "<html><head/><body><p>Сумма Потери:</p></body></html>"))

    def add_function1(self):  # Привязка кнопок построения диаграммы и кнопки "Назад"
        self.gobutton1.clicked.connect(self.build_diag1)
        self.backbutton1.clicked.connect(self.openmain)

    def build_diag1(self):  # Построение диаграммы
        self.idd = self.idline1.text()

        self.delta = int(self.lineEdit12.text())
        self.data = []
        event_map = []

        event = DataSender.get_event_by_id(int(self.idd), DataSender.main_events)
        if event != None:
            events = DataSender.get_all_events_majordata()

            DataSender.calculate_transfer_price(event=event, main_events=events, black_list=[], event_map=event_map,
                                                time_for_transfer=int(self.delta), first_event=event)

            data_for_dia_unchanged = DataSender.get_data_for_dia(int(self.idd), event_map)

            # Получение данных для построения диаграммы

            self.treeunchd = data_for_dia_unchanged
            self.data = []
            for tree in self.treeunchd:
                try:
                    y1, m1, d1 = map(int, tree[1].split("-"))
                    sdt1 = datetime.datetime(year=y1, month=m1, day=d1)
                    y2, m2, d2 = map(int, tree[2].split("-"))
                    sdt2 = datetime.datetime(year=y2, month=m2, day=d2)
                    edt1 = sdt1 + datetime.timedelta(self.delta)
                    edt2 = sdt2 + datetime.timedelta(self.delta)
                    self.data.append(dict(Name=f"{tree[0]}", Start=f"{sdt1}", Finish=f"{sdt2}", Resource='old'))
                    self.data.append(dict(Name=f"{tree[0]}", Start=f"{edt1}", Finish=f"{edt2}", Resource='new'))
                except Exception as ex:
                    print(ex.__str__())
            df = pd.DataFrame(self.data)
            fig = px.timeline(df, x_start="Start", x_end="Finish", y="Name", color="Resource")
            fig.update_yaxes(autorange="reversed")
            fig.show()
            self.value_label.setText(str(event.price) + ' ₽')


class Ui_SecondWind_2(Ui_MainWindow):
    def setupUi(self, SecondWind_2):  # Настройка второго окна
        SecondWind_2.setObjectName("SecondWind_2")
        SecondWind_2.resize(780, 681)
        SecondWind_2.setStyleSheet("background-color: rgb(169,184,250);")
        self.verticalLayout = QtWidgets.QVBoxLayout(SecondWind_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backbutton2 = QtWidgets.QPushButton(SecondWind_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backbutton2.sizePolicy().hasHeightForWidth())
        self.backbutton2.setSizePolicy(sizePolicy)
        self.backbutton2.setObjectName("backbutton2")
        self.horizontalLayout_2.addWidget(self.backbutton2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(SecondWind_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.idline2 = QtWidgets.QLineEdit(SecondWind_2)
        self.idline2.setObjectName("idline2")
        self.horizontalLayout.addWidget(self.idline2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gobutton2 = QtWidgets.QPushButton(SecondWind_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gobutton2.sizePolicy().hasHeightForWidth())
        self.gobutton2.setSizePolicy(sizePolicy)
        self.gobutton2.setObjectName("gobutton2")
        self.horizontalLayout_2.addWidget(self.gobutton2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(SecondWind_2)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gobutton2.setStyleSheet("background-color:  rgb(255, 255, 255);")
        self.backbutton2.setStyleSheet("background-color:  rgb(255, 255, 255);")
        self.idline2.setStyleSheet("background-color:  rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.resultlabel = QtWidgets.QLabel(SecondWind_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultlabel.sizePolicy().hasHeightForWidth())
        self.resultlabel.setSizePolicy(sizePolicy)
        self.resultlabel.setMinimumSize(QtCore.QSize(0, 20))
        self.resultlabel.setObjectName("resultlabel")
        self.verticalLayout.addWidget(self.resultlabel)
        self.resultlabel.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.retranslateUi(SecondWind_2)
        QtCore.QMetaObject.connectSlotsByName(SecondWind_2)
        self.add_function2()
        self.make_table()

    def retranslateUi(self, SecondWind_2):  # редакция текста кнопок и лэйблов первого окна
        _translate = QtCore.QCoreApplication.translate
        SecondWind_2.setWindowTitle(_translate("SecondWind_2", "Navi"))
        self.backbutton2.setText(_translate("SecondWind_2", "Назад"))
        self.label_2.setText(_translate("SecondWind_2", "ID"))
        self.gobutton2.setText(_translate("SecondWind_2", "Начать"))
        self.resultlabel.setText(
            _translate("SecondWind_2", "<html><head/><body><p>IT will be a text</p></body></html>"))

    def add_function2(self):  # Привязка кнопок
        self.backbutton2.clicked.connect(self.openmain)
        self.gobutton2.clicked.connect(self.status)
        self.tableWidget.doubleClicked.connect(self.fill_line)

    def fill_line(self):  # Вставка ID в поле для ввода по двойному клику
        for idx in self.tableWidget.selectionModel().selectedIndexes():
            self.row_number = idx.row()
        self.idline2.setText(str(DataSender.events_for_table[self.row_number][0]))

    def make_table(self):  # Создание таблицы

        array_len = len(DataSender.events_for_table)

        self.tableWidget.setRowCount(array_len)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setColumnWidth(0, 70)
        self.tableWidget.setColumnWidth(1, 160)
        self.tableWidget.setColumnWidth(2, 160)
        self.tableWidget.setColumnWidth(3, 95)
        self.tableWidget.setColumnWidth(4, 88)
        self.tableWidget.setColumnWidth(5, 95)
        self.tableWidget.setHorizontalHeaderLabels(
            ("ID", "Начало", "Конец", "Длительность", "CRP", "Зависимости"))  # название колон

        for i in range(array_len):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(DataSender.events_for_table[i][0])))

            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(DataSender.events_for_table[i][1])))

            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(DataSender.events_for_table[i][2])))

            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(DataSender.events_for_table[i][3])))

            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(DataSender.events_for_table[i][4])))

            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(DataSender.events_for_table[i][6])))

    def status(self):  # Вставка и поиск Рекомендации по событию
        array_len = len(DataSender.events_for_table)
        res = self.idline2.text()
        for i in range(array_len):
            if DataSender.events_for_table[i][0] == res:
                self.resultlabel.setText(DataSender.events_for_table[i][5])
                break


if __name__ == "__main__":
    print('start')
    DataSender.init()
    print('finish')

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('unnamed.png'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    firstwind = QtWidgets.QWidget()
    firstwind.setWindowIcon(QtGui.QIcon('unnamed.png'))
    ui_firstwind = Ui_FirstWindow()
    ui_firstwind.setupUi(firstwind)
    secondwind = QtWidgets.QWidget()
    ui_secondwind = Ui_SecondWind_2()
    ui_secondwind.setupUi(secondwind)
    MainWindow.show()
    sys.exit(app.exec_())
