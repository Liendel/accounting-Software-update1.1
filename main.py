#first window == main.py
#second window == grade_level.py
#Third Window == kinder1Table.py
#Fourth Window == kinder2Table.py

# Main Application
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QFormLayout, 
                            QLineEdit, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QMenuBar, QMenu, QAction, QTableWidget,
                            QHeaderView,QMessageBox, QDialog,QTableWidgetItem,
                            QGridLayout)
import sqlite3
import time 
from grade_level  import Grade_Level

appStyle = QApplication([])
# Force the style to be the same on all OSs:
appStyle.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette = QPalette() 
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
appStyle.setPalette(palette)

# first window to appear the log in window
class Login_window(QWidget):
    def __init__(self):
        super(Login_window, self).__init__()
        self.setWindowIcon(QIcon('logo/sacred_logo.png'))
        self.setWindowTitle('SHHS Log In')
        self.ui()

    def ui(self):
        # layout
        self.main_layout = QVBoxLayout()
        self.form_layout = QFor = QFormLayout()
        self.button_Layout = QHBoxLayout()

        # create label and label font size
        labelFont = QtGui.QFont()
        labelFont.setPointSize(15)

        self.username_label = QtWidgets.QLabel()
        self.username_label.setText('Username')
        self.username_label.setFont(labelFont)

        self.password_label = QtWidgets.QLabel()
        self.password_label.setText('Password')
        self.password_label.setFont(labelFont)

        # create lineEdit
        lineEdit_font = QtGui.QFont()
        lineEdit_font.setPointSize(15)

        self.username_lineEdit = QtWidgets.QLineEdit()
        self.username_lineEdit.setFont(lineEdit_font)

        self.password_lineEdit = QtWidgets.QLineEdit()
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_lineEdit.setFont(lineEdit_font)

        # create Button widget
        button_font = QtGui.QFont()
        button_font.setPointSize(12)

        self.okbtn = QtWidgets.QPushButton('Ok')
        self.okbtn.setFont(button_font)
        self.okbtn.clicked.connect(self.ok_method)  

        self.cancelbtn = QtWidgets.QPushButton('Cancel')
        self.cancelbtn.setFont(button_font)
        self.cancelbtn.clicked.connect(self.cancel_function)

        # add label and lineEdit widget to the layout
        self.form_layout.addRow(self.username_label, self.username_lineEdit)
        self.form_layout.addRow(self.password_label, self.password_lineEdit)

        # add button widget to the layout
        self.button_Layout.addWidget(self.okbtn)
        self.button_Layout.addWidget(self.cancelbtn)

        # nested layout
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_Layout)

        # set application layout
        self.setLayout(self.main_layout)

    def ok_method(self):
        username_text = self.username_lineEdit.text()
        password_text = self.password_lineEdit.text()
        if username_text == '' and password_text == '':
            self.close()
            self.gradeLevelWindow = Grade_Level()
            self.gradeLevelWindow.show()
        else:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('logo/sacred_logo.png'))
            msg.setWindowTitle('SHHS')
            msg.setText('Invalid Credentials')
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
            self.password_lineEdit.clear()

    def cancel_function(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login_window()
    window.show()
    sys.exit(app.exec_())