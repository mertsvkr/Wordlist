from PyQt5.QtWidgets import QPushButton
from Styles.buttons import previousButtonStyle


class PreviousButton(QPushButton):
    def __init__(self, app):
        super().__init__("< Prev")
        self.parentApp = app
        self.previousPages = list()
        self.setStyleSheet(previousButtonStyle)
        self.clicked.connect(self.clickSlot)
        self.setFixedHeight(50)
        self.setFixedWidth(100)

    def setPrevious(self):
        if self.parentApp.gui.currentPage != None:
            self.previousPages.append(self.parentApp.gui.currentPage)

            self.parentApp.gui.currentPage.hide()

    def clickSlot(self):
        if len(self.previousPages) != 0:
            self.parentApp.gui.leftPart.nextButton.element.setNext()
            self.parentApp.gui.currentPage = self.previousPages.pop(-1)
            self.parentApp.gui.currentPage.show()
