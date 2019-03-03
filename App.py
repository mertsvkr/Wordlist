from PyQt5.QtWidgets import QApplication
from GUI.index import Gui
import sys




class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.downloadedWords = None
        self.gui = Gui()
        self.searchResults = list()

    def openningOperations(self):
        self.gui.leftPart.navigationButtons["home"].element.click()



