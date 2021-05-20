# fourth application
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

# Third Window
class Kinder2_table(QMainWindow):
    def __init__(self):
        super(Kinder2_table, self).__init__()
        self.setWindowIcon(QIcon('logo/sacred_logo.png'))
        self.setWindowTitle('Kinder2 Table')
        self.ui()

    def ui(self):
        # menubar
        menuBar = self.menuBar()
        self.file_menu = menuBar.addMenu("File")
        self.edit_menu = menuBar.addMenu('Edit')

        # action for menubar
        self.refresh_action = QtWidgets.QAction('Main Table',self)
        self.refresh_action.setShortcut('F1')
        self.refresh_action.triggered.connect(self.main_table)
        self.file_menu.addAction(self.refresh_action)

        self.refresh_action = QtWidgets.QAction('Refresh',self)
        self.refresh_action.setShortcut('F5')
        self.refresh_action.triggered.connect(self.load_data)
        self.file_menu.addAction(self.refresh_action)

        self.close_action = QtWidgets.QAction('Close',self)
        self.close_action.setShortcut('Esc')
        self.close_action.triggered.connect(self.close_window)
        self.file_menu.addAction(self.close_action)

        self.add_record = QtWidgets.QAction('Add Record', self)
        self.add_record.triggered.connect(self.add_record_func)
        self.edit_menu.addAction(self.add_record)

        self.search_record = QtWidgets.QAction('Search Record', self)
        self.search_record.triggered.connect(self.search_record_func)
        self.edit_menu.addAction(self.search_record)

        self.delete_record = QtWidgets.QAction('Delete Record', self)
        self.delete_record.triggered.connect(self.delete_record_func)
        self.edit_menu.addAction(self.delete_record)

        # Create a Database
        self.conn = sqlite3.connect('kinder2_database.db')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS record(id TEXT, name TEXT, status TEXT, balance TEXT, amount_due TEXT)")

        # create table widget
        self.table_widget = QtWidgets.QTableWidget()
        self.setCentralWidget(self.table_widget)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setColumnCount(5)
        self.table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.table_widget.horizontalHeader().setSortIndicatorShown(False)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.verticalHeader().setCascadingSectionResizes(False)
        self.table_widget.verticalHeader().setStretchLastSection(False)
        self.table_widget.setHorizontalHeaderLabels(('ID#','Name','Status','Balance','Amount Due'))

        # setting a font size for table widget
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table_widget.setFont(font)

        # function for loading data
    def load_data(self):
        self.conn = sqlite3.connect("database.db")
        query = "SELECT * FROM record"
        result = self.conn.execute(query)
        self.table_widget.setRowCount(0)
        self.table_widget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_widget.setItem(row_number, column_number,QTableWidgetItem(str(data)))

    # Return back to table window class
    def main_table(self):
        from grade_level import Grade_Level
        self.window = Grade_Level()
        self.window.exec_()
        self.close()

        # function for menubar close
    def close_window(self):
        self.close()

        # function for add record menu
    def add_record_func(self):
        dialog = AddRecord()
        dialog.exec_()

        # function for search menu
    def search_record_func(self):
        dialog = Search()
        dialog.exec_()

        # function for delete menu
    def delete_record_func(self):
        dialog = Delete()
        dialog.exec_()