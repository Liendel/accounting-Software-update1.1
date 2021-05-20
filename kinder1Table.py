# third application
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
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
class Kinder1_table(QMainWindow):
    def __init__(self):
        super(Kinder1_table, self).__init__()
        self.setWindowIcon(QIcon('logo/sacred_logo.png'))
        self.setWindowTitle('Kinder1 Table')
        self.ui()

    def ui(self):
        # menubar
        menuBar = self.menuBar()
        self.file_menu = menuBar.addMenu("File")
        self.edit_menu = menuBar.addMenu('Edit')

        # action for menubar
        self.tableWindow = QtWidgets.QAction('Main Table',self)
        self.tableWindow.setShortcut('F1')
        self.tableWindow.triggered.connect(self.main_table)
        self.file_menu.addAction(self.tableWindow)

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
        self.conn = sqlite3.connect('kinder1_database.db')
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

        # this will keep the tablewindow update
        self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.load_data)
        self.timer.start()

        # function for loading data
    def load_data(self):
        self.conn = sqlite3.connect("kinder1_database.db")
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

class AddRecord(QDialog):
    
    def __init__(self):
        super(AddRecord,self).__init__()
        self.setWindowTitle('AddRecord')
        self.setWindowIcon(QIcon('logo/sacred_logo.png'))
        self.ui()

    def ui(self):

        # Creating Font
        font = QtGui.QFont()
        font.setPointSize(12)
        
        # create layout
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()

        # create label
        self.id = QtWidgets.QLabel()
        self.id.setText('ID#')
        self.id.setFont(font)

        self.name = QtWidgets.QLabel()
        self.name.setText('Name')
        self.name.setFont(font)

        self.status = QtWidgets.QLabel()
        self.status.setText('Status')
        self.status.setFont(font)

        self.balance = QtWidgets.QLabel()
        self.balance.setText('Balance')
        self.balance.setFont(font)

        self.amount = QtWidgets.QLabel()
        self.amount.setText('Amount Due')
        self.amount.setFont(font)

        # create lineEdit
        self.id_lineEdit = QtWidgets.QLineEdit()
        self.id_lineEdit.setFont(font)

        self.name_edit = QtWidgets.QLineEdit()
        self.name_edit.setFont(font)

        self.status_edit = QtWidgets.QLineEdit()
        self.status_edit.setFont(font)

        self.balance_edit = QtWidgets.QLineEdit()
        self.balance_edit.setFont(font)

        self.amount_edit = QtWidgets.QLineEdit()
        self.amount_edit.setFont(font)


        # adding button
        self.add_btn = QtWidgets.QPushButton()
        self.add_btn.setText('Add')
        self.add_btn.setFont(font)
        self.add_btn.clicked.connect(self.add_func)

        self.cancel_btn = QtWidgets.QPushButton()
        self.cancel_btn.setText('Cancel')
        self.cancel_btn.setFont(font)
        self.cancel_btn.clicked.connect(self.cancel_func)

        # adding widget to formlayout
        form_layout.addRow(self.id, self.id_lineEdit)
        form_layout.addRow(self.name, self.name_edit)
        form_layout.addRow(self.status, self.status_edit)
        form_layout.addRow(self.balance, self.balance_edit)
        form_layout.addRow(self.amount, self.amount_edit)

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.add_btn)
        main_layout.addWidget(self.cancel_btn)
        self.setLayout(main_layout)

    # button event for cancel button
    def cancel_func(self):
        self.close()

    # button event for add button
    def add_func(self):
        font = QtGui.QFont()
        font.setPointSize(15)
        id_no = self.id_lineEdit.text()
        name = self.name_edit.text()
        status = self.status_edit.text()
        balance = self.balance_edit.text()
        amount = self.amount_edit.text()
        try:
            self.conn = sqlite3.connect('kinder1_database.db')
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO record (id,name,status,balance,amount_due) VALUES (?,?,?,?,?)",(id_no,name,status,balance,amount))
            self.conn.commit()
            self.c.close()
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)
            message_box.setWindowTitle('Successful')
            message_box.setText('Student is added successfully to the database.')
            message_box.setFont(font)
            message_box.exec()
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add record to the database.')

# Seearch class
class Search(QDialog):
    
    def __init__(self):
        super(Search,self).__init__()
        self.setWindowIcon(QIcon('logo/sacred_logo.png'))
        self.setWindowTitle('Search Record')
        self.setFixedHeight(90)
        self.setFixedWidth(600)
        self.ui()

    def ui(self):
        # font
        font = QtGui.QFont()
        font.setPointSize(12)

        # setting a layout
        main_layout = QHBoxLayout()
        form_layout = QFormLayout()

        # QlineEdit
        self.search_lineEdit = QtWidgets.QLineEdit()
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setPlaceholderText('Type a Name')

        # search button
        self.search_btn = QtWidgets.QPushButton()
        self.search_btn.setText('Search')
        self.search_btn.setFont(font)
        self.search_btn.clicked.connect(self.search_func)

        # cancel button
        self.cancel_btn = QtWidgets.QPushButton()
        self.cancel_btn.setText('Cancel')
        self.cancel_btn.setFont(font)
        self.cancel_btn.clicked.connect(self.cancel_func)

        form_layout.addRow(self.search_lineEdit)

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.search_btn)
        main_layout.addWidget(self.cancel_btn)
        self.setLayout(main_layout)

    def search_func(self):
        # setting the font
        font = QtGui.QFont()
        font.setPointSize(15)

        search_for = self.search_lineEdit.text()
        try:
            self.conn = sqlite3.connect("kinder1_database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from record WHERE name=?",[search_for])
            row = result.fetchone()
            searchResult = "ID# : "+str(row[0])+'\n'+"Name : "+str(row[1])+'\n'+"Status : "+str(row[2])+'\n'+"Balance : "+str(row[3])+'\n'+"Amount Due : "+str(row[4])
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)
            message_box.setText(searchResult)
            message_box.setWindowTitle('Message Box')
            message_box.setFont(font)
            message_box.exec()

            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(f'Could not find {search_for} from database')
            msgBox.setWindowTitle("Message Box")
            msgBox.setFont(font)
            msgBox.exec()

    def cancel_func(self):
        self.close()

 # Delete class
class Delete(QDialog):
    
    def __init__(self):
        super(Delete,self).__init__()
        self.setWindowIcon(QIcon('logo/sacred_logo.png'))
        self.setWindowTitle('Delete')
        self.setFixedHeight(60)
        self.setFixedWidth(600)
        self.ui()

    def ui(self):
        # font
        font = QtGui.QFont()
        font.setPointSize(12)

        # setting a layout
        main_layout = QHBoxLayout()
        form_layout = QFormLayout()

        # QlineEdit
        self.delete_edit = QtWidgets.QLineEdit()
        self.delete_edit.setFont(font)
        self.delete_edit.setPlaceholderText('Type a Name')

        # search button
        self.delete_btn = QtWidgets.QPushButton()
        self.delete_btn.setText('Delete')
        self.delete_btn.setFont(font)
        self.delete_btn.clicked.connect(self.delete_func)

        # cancel button
        self.cancel_btn = QtWidgets.QPushButton()
        self.cancel_btn.setText('Cancel')
        self.cancel_btn.setFont(font)
        self.cancel_btn.clicked.connect(self.cancel_func)

        form_layout.addRow(self.delete_edit)

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.delete_btn)
        main_layout.addWidget(self.cancel_btn)
        self.setLayout(main_layout)

    def delete_func(self):
        # setting the font
        font = QtGui.QFont()
        font.setPointSize(15)
        delete_record = self.delete_edit.text()
        try:
            self.conn = sqlite3.connect('kinder1_database.db')
            self.c  = self.conn.cursor()
            self.c.execute("DELETE from record WHERE name=?",[delete_record])
            self.conn.commit()
            self.c.close()
            self.conn.close()
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)
            message_box.setText(f'{delete_record} Deleted From Record Table Successful')
            message_box.setFont(font)
            message_box.exec()
            self.close()
        except Exception:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText(f'Could not Delete {delete_record} from the database.')
            message_box.setFont(font)
            message_box.exec()

    def cancel_func(self):
        self.close()