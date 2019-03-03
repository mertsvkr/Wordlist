from PyQt5.QtWidgets import QScrollArea, QFrame, QVBoxLayout
from GUI.RightPart.ResultPage.MeaningsPage.Meaning import Meaning


class MeaningsPage(QScrollArea):
    def __init__(self, type, resultPage):
        super().__init__()
        self.resultPage = resultPage

        self.setWidgetResizable(True)
        self.frame = QFrame()
        self.setWidget(self.frame)
        self.meaningsPageLayout = QVBoxLayout()
        self.frame.setLayout(self.meaningsPageLayout)
        self.setStyleSheet("background-color: white")
        self.meanings = list()
        self.setMeanings(type, resultPage)

    def setMeanings(self, type, resultPage):
        for meaning in type.mainMeanings:
            meaningLayout = Meaning(meaning, resultPage)
            self.meanings.append(meaningLayout)
            self.meaningsPageLayout.addLayout(self.meanings[-1])
