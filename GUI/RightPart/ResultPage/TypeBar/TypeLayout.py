from PyQt5.QtWidgets import QHBoxLayout
from GUI.Utils.ElementWrapper import ElementWrapper
from GUI.RightPart.ResultPage.TypeBar.TypeButton import TypeButton
from GUI.RightPart.ResultPage.DownloadButtons import DownloadType


class TypeLayout(QHBoxLayout):
    def __init__(self, type, resultPage):
        super().__init__()
        self.resultPage = resultPage

        self.downloadButton = ElementWrapper(DownloadType(self, resultPage))
        self.addLayout(self.downloadButton)

        self.typeButton = ElementWrapper(TypeButton(type, resultPage))
        self.addLayout(self.typeButton)
