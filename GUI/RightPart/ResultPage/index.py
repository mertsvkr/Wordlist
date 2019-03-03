from PyQt5.QtWidgets import QScrollArea, QVBoxLayout
from GUI.RightPart.ResultPage.ResultHeader import ResultHeader
from GUI.RightPart.ResultPage.TypeBar.index import TypeBar
from Styles.buttons import typeButtonOpenStyle


class ResultPage(QScrollArea):
    def __init__(self, searcher, app):
        super().__init__()
        self.parentApp = app
        self.searchResult = searcher

        self.resultPage = QVBoxLayout()
        self.setLayout(self.resultPage)

        self.resultHeader = ResultHeader(searcher, self)
        self.resultPage.addLayout(self.resultHeader)

        self.typeBar = TypeBar(searcher, self)
        self.resultPage.addLayout(self.typeBar)

        self.meaningsPageLayout = QVBoxLayout()
        self.resultPage.addLayout(self.meaningsPageLayout)

        k = 0
        for i in self.typeBar.typeLayouts:
            i = self.typeBar.typeLayouts.get(i)
            self.meaningsPageLayout.addWidget(i.typeButton.element.meaningsPage)
            if k == 0:
                i.typeButton.element.meaningsPage.show()
                i.typeButton.element.setStyleSheet(typeButtonOpenStyle)
                i.typeButton.element.isOpen = True
            k = k + 1

