# -*- coding: utf-8 -*-

import os
import sys
import datetime
from PyQt4 import QtCore, QtGui  # import graphics module core for project, import graphics module ui for project
from PyQt4.QtCore import QObject
# This part will recreate window design from window.ui to main_window.py
# Make sure that pyuic4.bat file exist
#os.popen(r'C:\Python34\Lib\site-packages\PyQt4\pyuic4 window.ui>>main_window.py')
from main_window import Ui_MainWindow  # import generated window

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Main(QtGui.QMainWindow):  # QMainWindow is a base class with needed methods from main_window.py
    def __init__(self):
        """
        Call base init method for all window component generation.
        Create own object self.ui and setup window components on the screen
        Resize window to optimal size (try drag any application corner)
        """
        QtGui.QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(self.sizeHint())
        self.today = datetime.date.today()

        self.days_counter()
        self.counting()

        # conections
        QObject.connect(self.ui.date_start, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.days_counter)
        QObject.connect(self.ui.date_end, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.days_counter)
        QObject.connect(self.ui.spinBox_prepainment, QtCore.SIGNAL(_fromUtf8("valueChanged(QString)")), self.counting)
        QObject.connect(self.ui.SpinBox_square, QtCore.SIGNAL(_fromUtf8("valueChanged(QString)")), self.counting)
        QObject.connect(self.ui.spinBox_price, QtCore.SIGNAL(_fromUtf8("valueChanged(QString)")), self.counting)

    def days_counter(self):
        first_day = self.ui.date_start.date()
        last_day = self.ui.date_end.date()
        different_from_today = self.today - first_day.toPyDate()
        all_term = last_day.toPyDate() - first_day.toPyDate()
        Main.month_total = round(all_term.days / 30)
        Main.month_from_now = round(different_from_today.days / 30)
        #print( Main.month_total, Main.month_from_now) #debug
        self.counting()
    
    def counting(self):
        Main.total_price = round(self.ui.SpinBox_square.value() * self.ui.spinBox_price.value())
        Main.balance_amount = Main.total_price - self.ui.spinBox_prepainment.value()
        Main.month_payment = Main.balance_amount / (Main.month_total-1)
        self.ui.spinBox_total.setValue(int(Main.total_price))
        self.ui.spinBox_balance_amount.setValue(int(Main.balance_amount))
        self.ui.spinBox_mon_pay.setValue(int(Main.month_payment))



if __name__ == '__main__':  # check for execution from main.py file
    app = QtGui.QApplication(sys.argv)  # Add arguments processing possibility for application
    app.setWindowIcon(QtGui.QIcon("main.ico"))  # Set application icon file path
    myClipBoard = QtGui.QApplication.clipboard()  # Add clipboard processing possibility for application
    window = Main()  # QMainWindow object creation
    window.show()  # Show QMainWindow on the screen
    sys.exit(app.exec_())  # Add system exit processing
