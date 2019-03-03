from PyQt5.QtWidgets import QHBoxLayout
from GUI.RightPart.ResultPage.TypeBar.TypeLayout import TypeLayout


class TypeBar(QHBoxLayout):
    def __init__(self, result, resultPage):
        super().__init__()
        self.resultPage = resultPage
        self.typeLayouts = dict()
        self.setTypeLayouts(result, resultPage)

    def setTypeLayouts(self, result, resultPage):
        for type in result.word.wordTypes:
            type = result.word.wordTypes.get(type)
            typeLayout = TypeLayout(type, resultPage)
            self.typeLayouts.update({type.type: typeLayout})
            self.addLayout(self.typeLayouts.get(type.type))
