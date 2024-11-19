from PySide6.QtWidgets import (QMainWindow, QTextEdit, QApplication,
                               QMenuBar, QMenu, QFileDialog)
from PySide6 import QtCore

import sys

class Editor(QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()

        self.setWindowTitle("Editor")
        self.setGeometry(200, 200, 550, 400)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.createMenuBar()

    def createMenuBar(self):
        self.menubar = QMenuBar(self)
        self.setMenuBar(self.menubar)

        filemenu = QMenu("File", self)
        self.menubar.addMenu(filemenu)

        filemenu.addAction("Open", self.action_clicked)
        filemenu.addAction("Save", self.action_clicked)

    @QtCore.Slot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Open":
            fname = QFileDialog.getOpenFileName(self,"Open Text File", "...\\Desktop",
                                                       "Text Files (*.txt)")[0]

            try:
                f = open(fname, "r")
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()
            except FileNotFoundError:
                print("No such file")

        elif action.text() == "Save":
            fname = QFileDialog.getSaveFileName(self,"Save Text File", "...\\Desktop",
                                                       "Text Files (*.txt)")[0]

            try:
                f = open(fname, "w")
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("No such file")

def application():
    app = QApplication(sys.argv)
    editor = Editor()

    editor.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()