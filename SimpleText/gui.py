#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

class SimpleText(QWidget):

    CONFIG = {
        "AutoName": False,
        "Crypt": True
    }

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setFixedSize(800, 500)
        self.setWindowTitle("CryptoDiary")

        new = QPushButton("New", self)
        new.setFont(QFont("SansSerif", 10))
        new.clicked.connect(self.new)
        new.resize(new.sizeHint())
        new.move(528,10)

        del new

        save = QPushButton("Save", self)
        save.setFont(QFont("SansSerif", 10))
        save.clicked.connect(self.save)
        save.resize(save.sizeHint())
        save.move(700,10)

        del save

        load = QPushButton("Load", self)
        load.setFont(QFont("SansSerif", 10))
        load.clicked.connect(self.load)
        load.resize(load.sizeHint())
        load.move(614, 10)

        del load

        self.filename = QLineEdit(self)
        self.filename.setGeometry(10, 10, 515, 28)

        self.text = QPlainTextEdit(self)
        self.text.resize(QSize(780, 445))
        self.text.move(10, 45)

        self.show()

    def new(self):
        self.filename.setText("New.st")
        self.text.clear()

    def save(self):
        filename = self.filename.text()
        path = QFileDialog.getSaveFileName(self, "Save File", filename, '.st, .txt')[0]

        if path == "":
            return

        with open(path, "w") as writeFile:
            text = self.text.toPlainText()
            writeFile.write(text)

    def load(self):
        path = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        filename = path.split("/")[-1]

        if path == "":
            return

        self.filename.setText(filename)
        with open(path, "r") as readFile:
            text = readFile.read()
            self.text.setPlainText(text)

        del filename, path
