from PyQt5.QtWidgets import QPushButton
from Styles.buttons import typeButtonOpenStyle, typeButtonCloseStyle
from GUI.RightPart.ResultPage.MeaningsPage.index import MeaningsPage


class TypeButton(QPushButton):
    def __init__(self, type, resultPage):
        super().__init__()
        self.resultPage = resultPage
        self.isOpen = False
        self.setText(type.type)

        self.meaningsPage = None
        self.setMeaningsPageOfType(type, resultPage)

        self.setFixedHeight(30)
        self.setStyleSheet(typeButtonCloseStyle)

        self.clicked.connect(self.openPage)

    def openPage(self):
        for typeLayout in self.resultPage.typeBar.typeLayouts:
            type = self.resultPage.typeBar.typeLayouts.get(typeLayout)
            if self.text() != type.typeButton.element.text():
                type.typeButton.element.closePage()
        self.meaningsPage.show()
        self.setStyleSheet(typeButtonOpenStyle)
        self.isOpen = True

    def closePage(self):
        self.meaningsPage.hide()
        self.setStyleSheet(typeButtonCloseStyle)
        self.isOpen = False

    def setMeaningsPageOfType(self, type, resultPage):
        self.meaningsPage = MeaningsPage(type, resultPage)
        self.meaningsPage.hide()
