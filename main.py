import sys
import sqlite3
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5 import uic


datap = 'coffee.sqlite3'
st = {0: 'молотый',
      1: 'в зёрнах'}
a = 3


class CoffeeMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.coffee_table: QTableWidget = self.coffee_table
        self.coffee_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.load_table()

    def load_table(self):
        self.coffee_table.setRowCount(0)
        if not os.path.isfile(datap):
            return
        con = sqlite3.connect(datap)
        cur = con.cursor()
        data = cur.execute('SELECT * FROM coffee').fetchall()
        self.coffee_table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j in range(len(row)):
                if j == a:
                    value = st[row[j]]
                else:
                    value = str(row[j])
                item = QTableWidgetItem(value)
                item.setFlags(Qt.ItemIsEnabled)
                self.coffee_table.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeMainWindow()
    window.show()
    sys.exit(app.exec())
