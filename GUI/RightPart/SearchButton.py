from Styles.buttons import searchButtonStyle
from PyQt5.QtWidgets import QPushButton
from Operation.search import Searcher
from GUI.RightPart.ResultPage.index import ResultPage

class SearchButton(QPushButton):
    def __init__(self, app):
        super().__init__("search")
        self.parentApp = app
        self.clicked.connect(self.search)
        self.setStyleSheet(searchButtonStyle)
        self.setFixedHeight(35)
        self.setFixedWidth(80)

    def search(self):
        #        if len(self.parentApp.gui.rightPart.searchLine.element.text()) !=0:

        for i in self.parentApp.gui.rightPart.searchLine.element.text():
            if i != "" and i != " ":

                # searcher holds the result
                searcher = Searcher(
                    self.parentApp.gui.rightPart.searchLine.element.text())

                for previousResult in self.parentApp.searchResults:
                    if previousResult.searchResult.word.word == searcher.word.word:
                        self.parentApp.gui.rightPart.contentWrapper.showContent(previousResult)
                        previousResult.show()
                        return
                # createing of resultPage
                resultPage = ResultPage(searcher, self.parentApp)

                # showing of resultPage on Screen
                self.parentApp.gui.rightPart.contentWrapper.showContent(resultPage)
                # adding to previous results
                self.parentApp.searchResults.append(self.parentApp.gui.currentPage)

                break
