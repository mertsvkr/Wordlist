from PyQt5.QtWidgets import QPushButton
from Styles.buttons import nextButtonStyle


class NextButton(QPushButton):
    def __init__(self, app):
        super().__init__("Next >")
        self.parentApp = app
        self.nextPages = list()
        self.clicked.connect(self.clickSlot)
        self.setStyleSheet(nextButtonStyle)
        self.setFixedHeight(50)
        self.setFixedWidth(100)

    def setNext(self):
        self.nextPages.append(self.parentApp.gui.currentPage)
        self.parentApp.gui.currentPage.hide()

    def clickSlot(self):
        if len(self.nextPages) != 0:
            self.parentApp.gui.leftPart.previousButton.element.setPrevious()
            self.parentApp.gui.currentPage = self.nextPages.pop(-1)
            self.parentApp.gui.currentPage.show()
