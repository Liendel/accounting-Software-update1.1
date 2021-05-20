# Second Window
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
import kinder1Table

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

# Second Window
class Grade_Level(QDialog):
    def __init__(self):
        super(Grade_Level, self).__init__()
        self.setWindowIcon(QIcon('logo/sacred_logo.png'))
        self.setWindowTitle('Name of School or Company Name')
        self.ui()

    def ui(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        layout = QGridLayout()

        #Button Widget
        kinder1btn = QtWidgets.QPushButton()
        kinder1btn.setText('Kinder1')
        kinder1btn.setFont(font)
        kinder1btn.clicked.connect(self.kinder1_func)
        kinder2btn = QtWidgets.QPushButton()
        kinder2btn.setText('Kinder2')
        kinder2btn.setFont(font)
        kinder2btn.clicked.connect(self.kinder2_func)

        grade1xbtn = QtWidgets.QPushButton()
        grade1xbtn.setText('Grade 1x')
        grade1xbtn.setFont(font)
        grade1xbtn.clicked.connect(self.grade1x_func)
        grade1ybtn = QtWidgets.QPushButton()
        grade1ybtn.setText('Grade 1y')
        grade1ybtn.setFont(font)
        grade1ybtn.clicked.connect(self.grade1y_func)

        grade2xbtn = QtWidgets.QPushButton()
        grade2xbtn.setText('Grade 2x')
        grade2xbtn.clicked.connect(self.grade2x_func)
        grade2xbtn.setFont(font)
        grade2ybtn = QtWidgets.QPushButton()
        grade2ybtn.setText('Grade 2y')
        grade2ybtn.clicked.connect(self.g2y)
        grade2ybtn.setFont(font)

        grade3xbtn = QtWidgets.QPushButton()
        grade3xbtn.setText('Grade 3x')
        grade3xbtn.clicked.connect(self.g3x)
        grade3xbtn.setFont(font)
        grade3ybtn = QtWidgets.QPushButton()
        grade3ybtn.setText('Grade 3y')
        grade3ybtn.clicked.connect(self.g3y)
        grade3ybtn.setFont(font)

        grade4xbtn = QtWidgets.QPushButton()
        grade4xbtn.setText('Grade 4x')
        grade4xbtn.clicked.connect(self.g4x)
        grade4xbtn.setFont(font)
        grade4ybtn = QtWidgets.QPushButton()
        grade4ybtn.setText('Grade 4y')
        grade4ybtn.clicked.connect(self.g4y)
        grade4ybtn.setFont(font)

        grade5xbtn = QtWidgets.QPushButton()
        grade5xbtn.setText('Grade 5x')
        grade5xbtn.clicked.connect(self.g5x)
        grade5xbtn.setFont(font)
        grade5ybtn = QtWidgets.QPushButton()
        grade5ybtn.setText('Grade 5y')
        grade5ybtn.clicked.connect(self.g5y)
        grade5ybtn.setFont(font)

        grade6xbtn = QtWidgets.QPushButton()
        grade6xbtn.setText('Grade 6x')
        grade6xbtn.clicked.connect(self.g6x)
        grade6xbtn.setFont(font)
        grade6ybtn = QtWidgets.QPushButton()
        grade6ybtn.setText('Grade 6y')
        grade6ybtn.clicked.connect(self.g6y)
        grade6ybtn.setFont(font)

        grade7xbtn = QtWidgets.QPushButton()
        grade7xbtn.setText('Grade 7x')
        grade7xbtn.clicked.connect(self.g7x)
        grade7xbtn.setFont(font)
        grade7ybtn = QtWidgets.QPushButton()
        grade7ybtn.setText('Grade 7y')
        grade7ybtn.clicked.connect(self.g7y)
        grade7ybtn.setFont(font)

        grade8xbtn = QtWidgets.QPushButton()
        grade8xbtn.setText('Grade 8x')
        grade8xbtn.clicked.connect(self.g8x)
        grade8xbtn.setFont(font)
        grade8ybtn = QtWidgets.QPushButton()
        grade8ybtn.setText('Grade 8y')
        grade8ybtn.clicked.connect(self.g8y)
        grade8ybtn.setFont(font)

        grade9xbtn = QtWidgets.QPushButton()
        grade9xbtn.setText('Grade 9x')
        grade9xbtn.clicked.connect(self.g9x)
        grade9xbtn.setFont(font)
        grade9ybtn = QtWidgets.QPushButton()
        grade9ybtn.setText('Grade 9y')
        grade9ybtn.clicked.connect(self.g9y)
        grade9ybtn.setFont(font)

        grade10xbtn = QtWidgets.QPushButton()
        grade10xbtn.setText('Grade 10x')
        grade10xbtn.clicked.connect(self.g10x)
        grade10xbtn.setFont(font)
        grade10ybtn = QtWidgets.QPushButton()
        grade10ybtn.setText('Grade 10y')
        grade10ybtn.clicked.connect(self.g10y)
        grade10ybtn.setFont(font)

        grade11btn = QtWidgets.QPushButton()
        grade11btn.setText('Grade 11')
        grade11btn.clicked.connect(self.g11)
        grade11btn.setFont(font)

        grade12btn = QtWidgets.QPushButton()
        grade12btn.setText('Grade 12')
        grade12btn.clicked.connect(self.g12)
        grade12btn.setFont(font)

        # Add button widget to layout
        layout.addWidget(kinder1btn,0,0)
        layout.addWidget(kinder2btn,0,1)                
        
        layout.addWidget(grade1xbtn,0,2)
        layout.addWidget(grade1ybtn,0,3)
        
        layout.addWidget(grade2xbtn,1,0)
        layout.addWidget(grade2ybtn,1,1)

        layout.addWidget(grade3xbtn,1,2)
        layout.addWidget(grade3ybtn,1,3)

        layout.addWidget(grade4xbtn,2,0)
        layout.addWidget(grade4ybtn,2,1)

        layout.addWidget(grade5xbtn,2,2)
        layout.addWidget(grade5ybtn,2,3)

        layout.addWidget(grade6xbtn,3,0)
        layout.addWidget(grade6ybtn,3,1)

        layout.addWidget(grade7xbtn,3,2)
        layout.addWidget(grade7ybtn,3,3)

        layout.addWidget(grade8xbtn,4,0)
        layout.addWidget(grade8ybtn,4,1)

        layout.addWidget(grade9xbtn,4,2)
        layout.addWidget(grade9ybtn,4,3)

        layout.addWidget(grade10xbtn,5,0)
        layout.addWidget(grade10ybtn,5,1)

        layout.addWidget(grade11btn,5,2)
        layout.addWidget(grade12btn,5,3)
        
        self.setLayout(layout)

    def kinder1_func(self):
        from kinder1Table import Kinder1_table
        self.window = Kinder1_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def kinder2_func(self):
        from kinder2Table import Kinder2_table
        self.window = Kinder2_table()
        self.window.showMaximized()
        #self.window.load_data()
        self.close()

    def grade1x_func(self):
        from grade1x_table import Grade1x_table
        self.window = Grade1x_table()
        self.window.showMaximized()
        #self.window.load_data()
        self.close()

    def grade1y_func(self):
        self.window = Grade1y_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()
    
    def grade2x_func(self):
        self.window = Grade2x_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g2y(self):
        self.window = Grade2y_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g3x(self):
        self.window = Grade3x_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g3y(self):
        self.window = Grade3y_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g4x(self):
        self.window = Grade4x_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g4y(self):
        self.window = Grade4y_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g5x(self):
        self.window = Grade5x_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g5y(self):
        self.window = Grade5y_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g6x(self):
        self.window = Grade6x_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g6y(self):
        self.window = Grade6y_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g7x(self):
        self.window = Grade7x_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g7y(self):
        self.window = Grade7y_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g8x(self):
        self.window = Grade8x_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g8y(self):
        self.window = Grade8y_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g9x(self):
        self.window = Grade9x_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g9y(self):
        self.window = Grade9y_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g10x(self):
        self.window = Grade10x_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g10y(self):
        self.window = Grade10y_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g11(self):
        self.window = Grade11_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

    def g12(self):
        self.window = Grade12_table()
        self.window.showMaximized()
        self.window.load_data()
        self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Grade_Level()
	window.show()
	sys.exit(app.exec_())