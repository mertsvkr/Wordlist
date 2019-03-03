from PyQt5.QtWidgets import QPushButton
from Styles.buttons import addButtonStyle, removeButtonStyle


class DownloadWord(QPushButton):
    def __init__(self, result, resultPage):
        super().__init__()
        self.resultPage = resultPage
        self.isAdded = False
        self.setStyleSheet(addButtonStyle)
        self.setText("Download")
        self.clicked.connect(self.addRemove)
        self.setFixedHeight(30)
        self.setFixedWidth(70)

    def addRemove(self):
        if self.isAdded:
            self.remove()
        else:
            self.add()

    def add(self):

        for type in self.resultPage.typeBar.typeLayouts:
            type = self.resultPage.typeBar.typeLayouts.get(type)
            type.downloadButton.element.add()
        self.setStyleSheet(removeButtonStyle)

        self.isAdded = True

    def remove(self):
        for type in self.resultPage.typeBar.typeLayouts:
            type = self.resultPage.typeBar.typeLayouts.get(type)
            type.downloadButton.element.remove()
        self.setStyleSheet(addButtonStyle)
        self.isAdded = False


class DownloadMeaning(QPushButton):
    def __init__(self, meaning, resultPage):
        super().__init__()
        self.resultPage = resultPage
        self.meaning = meaning
        self.isAdded = False
        self.setStyleSheet(addButtonStyle)
        self.setFixedHeight(30)
        self.setFixedWidth(70)
        self.setText("Download")
        self.clicked.connect(self.addRemove)

    def addRemove(self):
        if self.isAdded:
            self.remove()
        else:
            self.add()

    def add(self):
        self.setStyleSheet(removeButtonStyle)

        self.isAdded = True

    def remove(self):
        type = self.resultPage.typeBar.typeLayouts.get(self.meaning.relatedWordType)
        type.downloadButton.element.isAdded = False
        type.downloadButton.element.setStyleSheet(addButtonStyle)

        self.resultPage.resultHeader.downloadButton.element.isAdded = False
        self.resultPage.resultHeader.downloadButton.element.setStyleSheet(addButtonStyle)

        self.setStyleSheet(addButtonStyle)

        self.isAdded = False


class DownloadType(QPushButton):
    def __init__(self, typeLayout, resultPage):
        super().__init__()
        self.resultPage = resultPage
        self.isAdded = False
        self.typeLayout = typeLayout
        self.setStyleSheet(addButtonStyle)
        self.setText("Download")
        self.clicked.connect(self.addRemove)
        self.setFixedHeight(30)
        self.setFixedWidth(70)

    def addRemove(self):
        if self.isAdded:
            self.remove()
        else:
            self.add()

    def add(self):

        for meaning in self.typeLayout.typeButton.element.meaningsPage.meanings:
            meaning.downloadButton.element.add()

        self.isAdded = True

        self.setStyleSheet(removeButtonStyle)

    def remove(self):
        for meaning in self.typeLayout.typeButton.element.meaningsPage.meanings:
            meaning.downloadButton.element.remove()
        self.setStyleSheet(addButtonStyle)
        self.resultPage.resultHeader.downloadButton.element.setStyleSheet(addButtonStyle)
        self.resultPage.resultHeader.downloadButton.element.isAdded = False

        self.isAdded = False
