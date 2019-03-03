from PyQt5.QtWidgets import QHBoxLayout, QLabel
from GUI.Utils.ElementWrapper import ElementWrapper
from GUI.RightPart.ResultPage.DownloadButtons import DownloadWord

class ResultHeader(QHBoxLayout):
    def __init__(self, result, resultPage):
        super().__init__()
        self.resultPage = resultPage

        self.downloadButton = ElementWrapper(DownloadWord(result, resultPage))
        self.addLayout(self.downloadButton)

        self.label = ElementWrapper(QLabel(str(result.word.word)))
        self.label.element.setStyleSheet("color:white; font-weight: bold; font-size: 30; text-transform: uppercase;")

        self.addLayout(self.label)
