from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout
from GUI.LeftPart.index import LeftPart
from GUI.RightPart.index import RightPart


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWid = QWidget()
        self.setCentralWidget(self.centralWid)
        self.parentApp = None
        self.leftPart = None
        self.rightPart = None
        self.currentPage = None
        self.centralWid.setStyleSheet("background-color: #383838;")
    #def closeEvent(self, *args, **kwargs):
        #print("kapandim")

    def setCurrentPage(self, page):
        self.currentPage = page

    def setSizeOfMainWindow(self, width, height):
        """
        :param Width: demanding width of main window
        :type Width: integer

        :param Height: demanding height of main window
        :type Height: integer
        """
        self.setGeometry(0, 0, width, height)

    def centralizeTheMainWindow(self, app):
        #  get the width and height of screen
        screenSizes = app.desktop().screenGeometry()
        screenWidth, screenHeight = screenSizes.width(), screenSizes.height()

        #  move the main window to center of screen
        self.move((screenWidth - self.width()) / 2, (screenHeight - self.height()) / 2)

    def setApp(self, app):
        """
        sets app which Gui belongs to , to reach other attributes of Application
        object of this Class will be instatiate in parentApp and this function also will be called there
        not in __init__.
        :param app: app which Gui belongs to
        """
        self.parentApp = app
        self.setSizeOfMainWindow(1000, 600)
        self.centralizeTheMainWindow(app)

    def setWindowParts(self):
        """
        main window is made of 2 parts, this function sets these two part
        this function won't be called from __init__ because it will send parentApp as argument.
        """
        centralLayout = QHBoxLayout()
        self.centralWid.setLayout(centralLayout)
        self.leftPart = LeftPart(self.parentApp)
        centralLayout.addLayout(self.leftPart)
        self.rightPart = RightPart(self.parentApp)
        centralLayout.addLayout(self.rightPart)

