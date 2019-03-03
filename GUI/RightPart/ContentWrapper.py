
class ContentWrapper:
    def __init__(self, app):
        self.parentApp = app

    def showContent(self, content):
        self.parentApp.gui.leftPart.previousButton.element.setPrevious()
        self.parentApp.gui.setCurrentPage(content)
        self.parentApp.gui.rightPart.pageLayout.addWidget(self.parentApp.gui.currentPage)

