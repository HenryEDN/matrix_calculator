import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

def matrix_multiply(matrix1, matrix2):

    res_matrix = [] #Список с конечным результатом вычисления
    mul_row = [] #Список в котором находятся промежуточные вычисления
    res_row = 0 #Переменная в которой находится промежуточные вычисления

    if len(matrix1) == len(matrix2): #Проверка на равенство двух матриц
        
        for row in range(len(matrix1)): #Строка матрицы

            for column in range(len(matrix2[0])): #Столбец матрицы
                
                for row2 in range(len(matrix2)): #Строка 2-й матрицы
                    try:    
                        res_row += matrix1[row][row2] * matrix2[row2][column]
                    except IndexError:
                        pass
                    
                mul_row.insert(0, res_row) 
                res_row = 0   
            res_matrix.insert(0, mul_row[::-1])
            mul_row = []
        

    else: pass

    return res_matrix[::-1]

def matrix_sub(matrix1, matrix2) -> list:

    res_matrix = [] #Список с конечным результатом вычисления
    sub_row = [] #Список в котором находятся промежуточные вычисления

    if len(matrix1) == len(matrix2): #Проверка на равенство двух матриц

        for row in range(len(matrix1)): #Строка матрицы

            for column in range(len(matrix1[0])): #Столбец матрицы
                sub_row.insert(0, matrix1[row][column] - matrix2[row][column])
                
            res_matrix.insert(0, sub_row[::-1])
            sub_row = []

    else: pass

    return res_matrix[::-1]

def matrix_sum(matrix1, matrix2) -> list:

    res_matrix = [] #Список с конечным результатом вычисления
    sum_row = [] #Список в котором находятся промежуточные вычисления

    if len(matrix1) == len(matrix2): #Проверка на равенство двух матриц

        for row in range(len(matrix1)): #Строка матрицы

            for column in range(len(matrix1[0])): #Столбец матрицы
                sum_row.insert(0, matrix1[row][column] + matrix2[row][column])

            res_matrix.insert(0, sum_row[::-1])
            sum_row = []

    else: pass

    return res_matrix[::-1]

def matrix_equal(matrix1, matrix2) -> list:

    if matrix1 == matrix2: #Матрицы равны
        return "Матрицы равны"
    elif matrix1 > matrix2: #Первая матрица больше второй
        return "Матрица 1 > Матрица 2"
    elif matrix1 < matrix2: #Вторая матрица больше первой
        return "Матрица 1 < Матрица 2"
    else:
        pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 683)
        MainWindow.setFixedSize(700, 683)
        MainWindow.setStyleSheet("background-color: #5A5A5A;\n"
"color: white;")
        MainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #414040;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 230, 161, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.multiply_by_number_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.multiply_by_number_1.setStyleSheet("#multiply_by_number_1{\n"
"    background-color:  #B6B6B6;\n"
"    border: 2px solid blue; \n"
"    color: Black;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#multiply_by_number_1:hover{\n"
"    background-color: #99CCFF;\n"
"}")
        self.multiply_by_number_1.setObjectName("multiply_by_number_1")
        self.verticalLayout_3.addWidget(self.multiply_by_number_1)
        self.det_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.det_1.setStyleSheet("#det_1{\n"
"    background-color:  #B6B6B6;\n"
"    border: 2px solid blue; \n"
"    color: Black;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#det_1:hover{\n"
"    background-color: #99CCFF;\n"
"}")
        self.det_1.setObjectName("det_1")
        self.verticalLayout_3.addWidget(self.det_1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(490, 230, 161, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.multiply_by_number_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.multiply_by_number_2.setStyleSheet("#multiply_by_number_2{\n"
"    background-color:  #B6B6B6;\n"
"    border: 2px solid blue; \n"
"    color: Black;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#multiply_by_number_2:hover{\n"
"    background-color: #99CCFF;\n"
"}")
        self.multiply_by_number_2.setObjectName("multiply_by_number_2")
        self.verticalLayout_4.addWidget(self.multiply_by_number_2)
        self.det_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.det_2.setStyleSheet("#det_2{\n"
"    background-color:  #B6B6B6;\n"
"    border: 2px solid blue; \n"
"    color: Black;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#det_2:hover{\n"
"    background-color: #99CCFF;\n"
"}")
        self.det_2.setObjectName("det_2")
        self.verticalLayout_4.addWidget(self.det_2)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(-10, 380, 721, 231))
        self.frame_4.setStyleSheet("background-color: #696969;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(40, 10, 181, 21))
        self.label.setStyleSheet("font-size: 16px;\n"
"color: silver;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(400, 70, 111, 21))
        self.label_2.setStyleSheet("font-size: 16px;\n"
"color: silver;")
        self.label_2.setObjectName("label_2")
        self.det_res = QtWidgets.QLineEdit(self.frame_4)
        self.det_res.setGeometry(QtCore.QRect(420, 100, 71, 21))
        self.det_res.setStyleSheet("\n"
"background-color: #82875F;\n"
"border:2px solid #FFFF99; \n"
"")
        self.det_res.setAlignment(QtCore.Qt.AlignCenter)
        self.det_res.setReadOnly(True)
        self.det_res.setObjectName("det_res")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(380, 10, 161, 31))
        self.label_3.setStyleSheet("font-size: 16px;\n"
"color: silver;")
        self.label_3.setObjectName("label_3")
        self.equal_res = QtWidgets.QLineEdit(self.frame_4)
        self.equal_res.setGeometry(QtCore.QRect(310, 40, 281, 21))
        self.equal_res.setStyleSheet("\n"
"#equal_res{\n"
"background-color: #82875F;\n"
"border: 2px solid #FFFF99;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.equal_res.setText("")
        self.equal_res.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_res.setReadOnly(True)
        self.equal_res.setObjectName("equal_res")
        self.matrix_res = QtWidgets.QTableWidget(self.frame_4)
        self.matrix_res.setGeometry(QtCore.QRect(36, 36, 177, 153))
        self.matrix_res.setStyleSheet("background-color: #82875F;\n"
"")
        self.matrix_res.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.matrix_res.setRowCount(0)
        self.matrix_res.setColumnCount(0)
        self.matrix_res.setObjectName("matrix_res")
        self.matrix_res.horizontalHeader().setVisible(False)
        self.matrix_res.horizontalHeader().setDefaultSectionSize(30)
        self.matrix_res.horizontalHeader().setMinimumSectionSize(23)
        self.matrix_res.verticalHeader().setVisible(False)
        self.matrix_res.verticalHeader().setDefaultSectionSize(30)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(270, 230, 160, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.multiply_value = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.multiply_value.setStyleSheet("#multiply_value{\n"
"background-color:  #B6B6B6;\n"
"border: 2px solid blue; \n"
"color: gray;\n"
"}\n"
"\n"
"#multiply_value:hover{\n"
"    background-color: #99CCFF;\n"
"}\n"
"\n"
"\n"
"")
        self.multiply_value.setText("")
        self.multiply_value.setAlignment(QtCore.Qt.AlignCenter)
        self.multiply_value.setObjectName("multiply_value")
        self.verticalLayout.addWidget(self.multiply_value)
        self.clear = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.clear.setStyleSheet("#clear{\n"
"    background-color:  #B6B6B6;\n"
"    border: 2px solid gray; \n"
"    color: Black;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#clear:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}")
        self.clear.setObjectName("clear")
        self.verticalLayout.addWidget(self.clear)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 10, 161, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.matrix_size = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.matrix_size.setStyleSheet("#matrix_size{\n"
"background-color: silver;\n"
"border: 2px solid #546B52; \n"
"color: gray\n"
"}\n"
"\n"
"#matrix_size:hover{\n"
"    background-color: #8FBC8F;\n"
"}\n"
"\n"
"")
        self.matrix_size.setAlignment(QtCore.Qt.AlignCenter)
        self.matrix_size.setObjectName("matrix_size")
        self.verticalLayout_2.addWidget(self.matrix_size)
        self.draw = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.draw.setAutoFillBackground(False)
        self.draw.setStyleSheet("#draw{\n"
"    background-color:  #B6B6B6;\n"
"    border: 2px solid #546B52;\n"
"    color: Black;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#draw:hover{\n"
"    background-color: #8FBC8F;\n"
"}")
        self.draw.setObjectName("draw")
        self.verticalLayout_2.addWidget(self.draw)
        self.sum_but = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sum_but.setStyleSheet("#sum_but{\n"
"    background-color: #B6B6B6;\n"
"    border: 2px solid red; \n"
"    color: Black;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#sum_but:hover{\n"
"    background-color: #FF9999;\n"
"    color: white;\n"
"}")
        self.sum_but.setObjectName("sum_but")
        self.verticalLayout_2.addWidget(self.sum_but)
        self.multi = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.multi.setStyleSheet("#multi{\n"
"    background-color:  #B6B6B6;\n"
"    border: 2px solid red; \n"
"    color: Black;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#multi:hover{\n"
"    background-color: #FF9999;\n"
"    color: white;\n"
"}")
        self.multi.setObjectName("multi")
        self.verticalLayout_2.addWidget(self.multi)
        self.sub = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sub.setStyleSheet("#sub{\n"
"    background-color:  #B6B6B6;\n"
"    border: 2px solid red; \n"
"    color: Black;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#sub:hover{\n"
"    background-color: #FF9999;\n"
"    color: white;\n"
"}")
        self.sub.setObjectName("sub")
        self.verticalLayout_2.addWidget(self.sub)
        self.equal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.equal.setStyleSheet("#equal{\n"
"    background-color:  #B6B6B6;\n"
"    border: 2px solid red; \n"
"    color: Black;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#equal:hover{\n"
"    background-color: #FF9999;\n"
"    color: white;\n"
"}")
        self.equal.setObjectName("equal")
        self.verticalLayout_2.addWidget(self.equal)
        self.matrix1 = QtWidgets.QTableWidget(self.centralwidget)
        self.matrix1.setGeometry(QtCore.QRect(30, 20, 177, 153))
        self.matrix1.setStyleSheet("background-color: #546B52;")
        self.matrix1.setRowCount(0)
        self.matrix1.setColumnCount(0)
        self.matrix1.setObjectName("matrix1")
        self.matrix1.horizontalHeader().setVisible(False)
        self.matrix1.horizontalHeader().setDefaultSectionSize(30)
        self.matrix1.horizontalHeader().setMinimumSectionSize(23)
        self.matrix1.verticalHeader().setVisible(False)
        self.matrix1.verticalHeader().setDefaultSectionSize(30)
        self.matrix1.verticalHeader().setMinimumSectionSize(23)
        self.matrix2 = QtWidgets.QTableWidget(self.centralwidget)
        self.matrix2.setGeometry(QtCore.QRect(470, 20, 177, 153))
        self.matrix2.setStyleSheet("background-color: #546B52;")
        self.matrix2.setRowCount(0)
        self.matrix2.setColumnCount(0)
        self.matrix2.setObjectName("matrix2")
        self.matrix2.horizontalHeader().setVisible(False)
        self.matrix2.horizontalHeader().setDefaultSectionSize(30)
        self.matrix2.horizontalHeader().setMinimumSectionSize(23)
        self.matrix2.verticalHeader().setVisible(False)
        self.matrix2.verticalHeader().setDefaultSectionSize(30)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Кнопки
        self.draw.clicked.connect(lambda: self.draw_mat())
        self.multiply_by_number_1.clicked.connect(lambda: self.matrix_multiply_by_number())
        self.multiply_by_number_2.clicked.connect(lambda: self.matrix_multiply_by_number2())
        self.det_1.clicked.connect(lambda: self.determination())
        self.det_2.clicked.connect(lambda: self.determination2())
        self.clear.clicked.connect(lambda: self.clear_it())
        self.sum_but.clicked.connect(lambda: self.sum())
        self.equal.clicked.connect(lambda: self.equal_mat())
        self.sub.clicked.connect(lambda: self.sub_mat())
        self.multi.clicked.connect(lambda: self.multi_mat())


        #Функции

    def multi_mat(self):
        self.statusbar.showMessage('')
        matrix1 = []
        matrix2 = []
        matrix_row = []

        try:
                size = int(self.matrix_size.text())
        except ValueError:
                return None

        try:
                for i in range(size):
                        for j in range(size):
                                if self.matrix1.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix1.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix1.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix1 = matrix1[::-1]

                for i in range(size):
                        for j in range(size):
                                if self.matrix2.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix2.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix2.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix2 = matrix2[::-1]

                for row in range(len(matrix_multiply(matrix1, matrix2))):

                        for column in range(len(matrix_multiply(matrix1, matrix2)[0])):
                                item = QTableWidgetItem()
                                item.setText(str(matrix_multiply(matrix1, matrix2)[row][column]))
                                self.matrix_res.setItem(row, column, item)

                
        except AttributeError:
                self.statusbar.showMessage("Пожалуйста заполните матрицу полностью.")
                return None
                
        except AttributeError:
                self.statusbar.showMessage("Пожалуйста заполните матрицу полностью.")
                return None

    def equal_mat(self):
        self.statusbar.showMessage('')
        matrix1 = []
        matrix2 = []
        matrix_row = []

        try:
                size = int(self.matrix_size.text())
        except ValueError:
                return None

        try:
                for i in range(size):
                        for j in range(size):
                                if self.matrix1.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix1.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix1.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix1 = matrix1[::-1]

                for i in range(size):
                        for j in range(size):
                                if self.matrix2.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix2.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix2.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix2 = matrix2[::-1]

                self.equal_res.setText(matrix_equal(matrix1, matrix2))
                
        except AttributeError:
                self.statusbar.showMessage("Пожалуйста заполните матрицу полностью.")
                return None

    def sub_mat(self):
        self.statusbar.showMessage('')
        matrix1 = []
        matrix2 = []
        matrix_row = []

        try:
                size = int(self.matrix_size.text())
        except ValueError:
                return None

        try:
                for i in range(size):
                        for j in range(size):
                                if self.matrix1.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix1.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix1.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix1 = matrix1[::-1]

                for i in range(size):
                        for j in range(size):
                                if self.matrix2.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix2.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix2.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix2 = matrix2[::-1]

                for row in range(len(matrix_sub(matrix1, matrix2))):

                        for column in range(len(matrix_sub(matrix1, matrix2)[0])):
                                item = QTableWidgetItem()
                                item.setText(str(matrix_sub(matrix1, matrix2)[row][column]))
                                self.matrix_res.setItem(row, column, item)

                
        except AttributeError:
                self.statusbar.showMessage("Пожалуйста заполните матрицу полностью.")
                return None

    def equal_mat(self):
        self.statusbar.showMessage('')
        matrix1 = []
        matrix2 = []
        matrix_row = []

        try:
                size = int(self.matrix_size.text())
        except ValueError:
                return None

        try:
                for i in range(size):
                        for j in range(size):
                                if self.matrix1.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix1.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix1.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix1 = matrix1[::-1]

                for i in range(size):
                        for j in range(size):
                                if self.matrix2.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix2.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix2.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix2 = matrix2[::-1]

                self.equal_res.setText(matrix_equal(matrix1, matrix2))
                
        except AttributeError:
                self.statusbar.showMessage("Пожалуйста заполните матрицу полностью.")
                return None

    def sum(self):
        self.statusbar.showMessage('')
        matrix1 = []
        matrix2 = []
        matrix_row = []

        try:
                size = int(self.matrix_size.text())
        except ValueError:
                return None

        try:
                for i in range(size):
                        for j in range(size):
                                if self.matrix1.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix1.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix1.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix1 = matrix1[::-1]

                for i in range(size):
                        for j in range(size):
                                if self.matrix2.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix2.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix2.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix2 = matrix2[::-1]

                for row in range(len(matrix_sum(matrix1, matrix2))):

                        for column in range(len(matrix_sum(matrix1, matrix2)[0])):
                                item = QTableWidgetItem()
                                item.setText(str(matrix_sum(matrix1, matrix2)[row][column]))
                                self.matrix_res.setItem(row, column, item)
        except AttributeError:
                self.statusbar.showMessage("Пожалуйста заполните матрицу полностью.")
                return None



    def draw_mat(self):
        self.statusbar.showMessage('')
        try:
                size = int(self.matrix_size.text())
        except ValueError:
                return None

        if  size not in [1,2,3,4,5]:
                self.statusbar.showMessage("max size 5")
                return None
        self.matrix_res.setRowCount(size)
        self.matrix_res.setColumnCount(size)
        self.matrix1.setRowCount(size)
        self.matrix1.setColumnCount(size)
        self.matrix2.setRowCount(size)
        self.matrix2.setColumnCount(size)

    def matrix_multiply_by_number(self):
        self.statusbar.showMessage('')
        matrix = []
        multiply_mat = []
        matrix_row = []

        try:
                size = int(self.matrix_size.text())
        except ValueError:
                return None
        
        try:
                multiply = int(self.multiply_value.text())
        except ValueError:
                self.statusbar.showMessage("Пожалуйста введите множитель.")
                return None
        
        try:
                for i in range(size):
                        for j in range(size):
                                if self.matrix1.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix1.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix = matrix[::-1]

                for row in range(len(matrix)):

                        for column in range(len(matrix[0])):
                                matrix_row.insert(0, matrix[row][column] * multiply)
                                
                        multiply_mat.insert(0, matrix_row[::-1])
                        matrix_row = []

                multiply_mat = multiply_mat[::-1]

                for row in range(len(multiply_mat)):

                        for column in range(len(multiply_mat[0])):
                                item = QTableWidgetItem()
                                item.setText(str(multiply_mat[row][column]))
                                self.matrix_res.setItem(row, column, item)
        except AttributeError:
                self.statusbar.showMessage("Пожалуйста заполните матрицу полностью.")
                return None                
 
    def matrix_multiply_by_number2(self):
        self.statusbar.showMessage('')
        matrix = []
        multiply_mat = []
        matrix_row = []

        try:
                size = int(self.matrix_size.text())
        except ValueError:
                return None
        
        try:
                multiply = int(self.multiply_value.text())
        except ValueError:
                self.statusbar.showMessage("Пожалуйста введите множитель.")
                return None
        
        try:
                for i in range(size):
                        for j in range(size):
                                if self.matrix2.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix2.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix = matrix[::-1]

                for row in range(len(matrix)):

                        for column in range(len(matrix[0])):
                                matrix_row.insert(0, matrix[row][column] * multiply)
                                
                        multiply_mat.insert(0, matrix_row[::-1])
                        matrix_row = []

                multiply_mat = multiply_mat[::-1]

                for row in range(len(multiply_mat)):

                        for column in range(len(multiply_mat[0])):
                                item = QTableWidgetItem()
                                item.setText(str(multiply_mat[row][column]))
                                self.matrix_res.setItem(row, column, item)
        except AttributeError:
                self.statusbar.showMessage("Пожалуйста заполните матрицу полностью.")
                return None


    def determination(self):
        self.statusbar.showMessage('')
        matrix = []
        matrix_row = []

        try:
                size = int(self.matrix_size.text())
        except ValueError:
                return None
        
        try:
                for i in range(size):
                        for j in range(size):
                                if self.matrix1.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix1.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix = matrix[::-1]
                if matrix:
                        self.det_res.setText(str(round(np.linalg.det(matrix), 0)))
                else:
                        pass
        except AttributeError:
                return None 

    def determination2(self):
        self.statusbar.showMessage('')
        matrix = []
        matrix_row = []

        try:
                size = int(self.matrix_size.text())
        except ValueError:
                return None
        
        try:
                for i in range(size):
                        for j in range(size):
                                if self.matrix2.item(i, j).text():
                                        matrix_row.insert(0, int(self.matrix2.item(i, j).text()))
                                else:
                                        matrix_row.insert(0, 0)
                        matrix.insert(0, matrix_row[::-1])
                        matrix_row = []
                matrix = matrix[::-1]
                if matrix:
                        self.det_res.setText(str(round(np.linalg.det(matrix), 0)))
                else:
                        pass
        except AttributeError:
                return None 

    def clear_it(self):
        self.statusbar.showMessage('')
        self.matrix_res.setRowCount(0)
        self.matrix_res.setColumnCount(0)
        self.matrix1.setRowCount(0)
        self.matrix1.setColumnCount(0)
        self.matrix2.setRowCount(0)
        self.matrix2.setColumnCount(0)
        self.multiply_value.clear()
        self.matrix_size.clear()
        self.det_res.clear()
        self.equal_res.clear()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Matrix calculator"))
        self.multiply_by_number_1.setText(_translate("MainWindow", "Умножить на число"))
        self.det_1.setText(_translate("MainWindow", "Определитель"))
        self.multiply_by_number_2.setText(_translate("MainWindow", "Умножить на число"))
        self.det_2.setText(_translate("MainWindow", "Определитель"))
        self.label.setText(_translate("MainWindow", "Результат вычисления:"))
        self.label_2.setText(_translate("MainWindow", "Определитель:"))
        self.label_3.setText(_translate("MainWindow", "Сравнение Матриц:"))
        self.multiply_value.setPlaceholderText(_translate("MainWindow", "Множитель"))
        self.clear.setText(_translate("MainWindow", "Очистить"))
        self.matrix_size.setPlaceholderText(_translate("MainWindow", "Размер матрицы (max 5x5)"))
        self.draw.setText(_translate("MainWindow", "Нарисовать"))
        self.sum_but.setText(_translate("MainWindow", "Сложить"))
        self.multi.setText(_translate("MainWindow", "Умножить"))
        self.sub.setText(_translate("MainWindow", "Вычесть"))
        self.equal.setText(_translate("MainWindow", "Сравнить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
