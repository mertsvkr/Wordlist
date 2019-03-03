from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from GUI.Utils.ElementWrapper import ElementWrapper
from GUI.LeftPart.NavigationButtons import *
from GUI.LeftPart.NextButton import NextButton
from GUI.LeftPart.PreviousButton import PreviousButton


class LeftPart(QVBoxLayout):
    def __init__(self, app):
        super().__init__()
        self.parentApp = app

        self.previousNextButtonLayout = self.createPreviousNextButtonLayout()
        self.setPreviousNextButtonLayout()
        # self.previousNextButtonLayout.setContentsMargins(30,30,30,30)

        self.navigationButtonsLayout = self.createNavigationButtonsLayout()
        self.setNavigationButtonsLayout()

        self.newListLayout = self.createNewListLayout()
        self.setNewListLayout()

        self.navigationButtons = self.createNavigationButtons()
        self.setNavigationButtons()

        self.previousButton = ElementWrapper(self.createPreviousButton())
        self.setPreviousButton()
        # self.previousButton.setContentsMargins(10,10,10,10)
        self.nextButton = ElementWrapper(self.createNextButton())
        self.setNextButton()

    def createPreviousButton(self):
        button = PreviousButton(self.parentApp)
        return button

    def createNextButton(self):
        button = NextButton(self.parentApp)
        return button

    def setPreviousButton(self):
        self.previousNextButtonLayout.addLayout(self.previousButton)

    def setNextButton(self):
        self.previousNextButtonLayout.addLayout(self.nextButton)

    def setNewListLayout(self):
        self.addLayout(self.newListLayout)

    def createNewListLayout(self):
        layout = QVBoxLayout()
        return layout

    def setNavigationButtonsLayout(self):
        self.addLayout(self.navigationButtonsLayout)

    def createPreviousNextButtonLayout(self):
        layout = QHBoxLayout()
        return layout

    def setPreviousNextButtonLayout(self):
        self.addLayout(self.previousNextButtonLayout)

    def createNavigationButtonsLayout(self):
        layout = QVBoxLayout()
        return layout

    def createNavigationButtons(self):
        """
        create buttons to open some pages
        :return: dictionary type variable which holds all navigation  buttons
        """

        navigationButtons = dict()

        navigationButtons.update({"home": ElementWrapper(HomeButton(self.parentApp))})
        navigationButtons.update({"lists": ElementWrapper(ListsButton(self.parentApp))})
        navigationButtons.update({"allWords": ElementWrapper(AllWordsButton(self.parentApp))})
        navigationButtons.update({"tests": ElementWrapper(TestsButton(self.parentApp))})
        navigationButtons.update({"games": ElementWrapper(GamesButton(self.parentApp))})

        return navigationButtons

    def setNavigationButtons(self):
        """
        sets all buttons into navigationButtonLayout
        :return:
        """
        for button in self.navigationButtons:
            self.navigationButtonsLayout.addLayout(self.navigationButtons[button])
