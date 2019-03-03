from PyQt5.QtWidgets import QPushButton, QScrollArea
from Styles.buttons import navigationButtonStyle


class HomeButton(QPushButton):
    def __init__(self, app):
        super().__init__("Home")
        self.parentApp = app
        self.clicked.connect(self.prepareHomeButton)
        self.setStyleSheet(navigationButtonStyle)
        self.setFixedHeight(30)
        self.setFixedWidth(200)

    def prepareHomeButton(self):
        sc = QScrollArea()
        self.parentApp.gui.rightPart.contentWrapper.showContent(sc)
        sc.setStyleSheet("background-color: white")


class ListsButton(QPushButton):
    def __init__(self, app):
        super().__init__("All Lists")
        self.parentApp = app
        self.setStyleSheet(navigationButtonStyle)
        self.setFixedHeight(30)
        self.setFixedWidth(200)


class AllWordsButton(QPushButton):
    def __init__(self, app):
        super().__init__("All Words")
        self.parentApp = app
        self.setStyleSheet(navigationButtonStyle)
        self.setFixedHeight(30)
        self.setFixedWidth(200)


class TestsButton(QPushButton):
    def __init__(self, app):
        super().__init__("Tests")
        self.parentApp = app
        self.setStyleSheet(navigationButtonStyle)
        self.setFixedHeight(30)
        self.setFixedWidth(200)


class GamesButton(QPushButton):
    def __init__(self, app):
        super().__init__("Games")
        self.parentApp = app
        self.setStyleSheet(navigationButtonStyle)
        self.setFixedHeight(30)
        self.setFixedWidth(200)
