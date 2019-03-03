from PyQt5.QtWidgets import QVBoxLayout, QLabel
from GUI.Utils.ElementWrapper import ElementWrapper
from GUI.RightPart.ResultPage.DownloadButtons import DownloadMeaning


class Meaning(QVBoxLayout):
    def __init__(self, meaning, resultPage):
        super().__init__()
        self.resultPage = resultPage

        self.downloadButton = ElementWrapper(DownloadMeaning(meaning, resultPage))
        self.addLayout(self.downloadButton)

        self.mainMeaning = ElementWrapper(QLabel())
        self.mainMeaning.element.setWordWrap(True)
        self.mainMeaning.element.setText(str(meaning.mainMeaningNumber)
                                         + ".  "
                                         + str(meaning.mainMeaning))
        self.addLayout(self.mainMeaning)
        self.mainMeaning.element.setStyleSheet("font-weight: bold; font-size: 15px")
        self.exampleLayout = MainMeaningExampleLayout(meaning)
        self.addLayout(self.exampleLayout)


class MainMeaningExampleLayout(QVBoxLayout):
    def __init__(self, meaning):
        super().__init__()
        if meaning.examples:
            for example in meaning.examples:
                label = QLabel()
                label.setWordWrap(True)
                label.setStyleSheet("background-color: white")
                label.setText(str(example))
                self.addWidget(label)
        self.setContentsMargins(50, 0, 0, 0)
