from GUI.Utils.ElementWrapper import ElementWrapper
from GUI.RightPart.ContentWrapper import ContentWrapper
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from GUI.RightPart.SearchButton import SearchButton
from GUI.RightPart.SearchLine import SearchLine


class RightPart(QVBoxLayout):
    def __init__(self, app):
        super().__init__()
        self.parentApp = app

        self.searchLayout = self.createSearchLayout()
        self.setSearchLayout()

        self.pageLayout = self.createPageLayout()
        self.setPageLayout()

        self.searchLine = ElementWrapper(self.createSearchLine())
        self.setSearchLine()

        self.searchButton = ElementWrapper(self.createSearchButton())
        self.setSearchButton()

        self.contentWrapper = ContentWrapper(self.parentApp)

    def setPageLayout(self):
        self.addLayout(self.pageLayout)

    def createSearchLayout(self):
        """
        this layout will take search line widget and search button
        :return: returns this layout
        """
        layout = QHBoxLayout()
        return layout

    def setSearchLayout(self):
        self.addLayout(self.searchLayout)

    def createPageLayout(self):
        """
        this layout will display every content
        :return: returns this layout
        """
        layout = QVBoxLayout()
        return layout

    def createSearchLine(self):
        """
        this line is to write any word or phrase to look up
        :return: returns lineEdit object
        """
        line = SearchLine(self.parentApp)
        return line

    def setSearchLine(self):
        self.searchLayout.addLayout(self.searchLine)

    def createSearchButton(self):
        """
        creates button which sends signal to search the text written in searchLine
        :return: returns this button
        """
        button = SearchButton(self.parentApp)
        return button

    def setSearchButton(self):
        self.searchLayout.addLayout(self.searchButton)

