from PyQt5.QtWidgets import QLineEdit
from Styles.input import searchLineStyle

class SearchLine(QLineEdit):
    def __init__(self, app):
        super().__init__()
        self.parentApp = app
        self.setStyleSheet(searchLineStyle)
        self.setFixedHeight(35)
        self.setPlaceholderText("search for a word or phrase...")
