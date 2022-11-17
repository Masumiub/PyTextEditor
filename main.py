import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import QSize

class PyTextEditior(QMainWindow):
    def __init__(self):
        super(PyTextEditior, self).__init__()
        self.editor = QTextEdit()
        self.setWindowTitle("PyTextEditor")
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(15)
        self.create_tool_bar()
        self.setStyleSheet("color: #000000; font-family:'Arial' ")
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = QMenuBar()

        file_menu = QMenu('File', self)
        menu_bar.addMenu(file_menu)


        edit_menu = QMenu('Edit', self)
        menu_bar.addMenu(edit_menu)

        view_menu = QMenu('View', self)
        menu_bar.addMenu(view_menu)

        self.setMenuBar(menu_bar)

    def create_tool_bar(self):
        tool_bar = QToolBar()
        #tool_bar.setStyleSheet("background-color: #000000")

        undo_action = QAction('Undo', self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)

        redo_action = QAction('Redo', self)
        redo_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo_action)

        cut_action = QAction('Cut', self)
        cut_action.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut_action)
        self.addToolBar(tool_bar)

        copy_action = QAction('Copy', self)
        copy_action.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy_action)
        self.addToolBar(tool_bar)

        paste_action = QAction('Paste', self)
        paste_action.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste_action)
        self.addToolBar(tool_bar)



app = QApplication(sys.argv)
window = PyTextEditior()
#window.setStyleSheet("background-color: #000000; color: #ffffff;")
window.resize(550,550)
window.show()
sys.exit(app.exec_())