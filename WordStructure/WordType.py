from bs4 import BeautifulSoup
from WordStructure.MainMeaning import MainMeaning

class WordType:
    def __init__(self, word, gramb, type):
        self.relatedWord = word
        self.type = str(type.text)
        self.mainMeanings = list()
        self.setMainMeanings(gramb)
        self.isAdded = False
    def setMainMeanings(self, gramb):
        """
        :param gramb: gramb is wrapper for any word type in html code
        """
        mainMeaningWrapperList = gramb.findChildren("ul", {"class":"semb"})
        mainMeaningWrapperList = mainMeaningWrapperList[0]
        mainMeaningWrappers = mainMeaningWrapperList.findChildren("li", {"class":None})

        numberOfMainMeaning = 1
        for mainMeaningWrapper in mainMeaningWrappers:
            mainMeaning = mainMeaningWrapper.findChild("span", {"class": "ind"})
            if mainMeaning:
                mainMeaning = mainMeaning.text
                self.mainMeanings.append(MainMeaning(self.type, mainMeaning, mainMeaningWrapper, numberOfMainMeaning))
            else:
                mainMeaning = mainMeaningWrapper.findChild("div", {"class": "crossReference"})
                mainMeaning = mainMeaning.text
                if mainMeaning:
                    self.mainMeanings.append(
                        MainMeaning(self.type, mainMeaning, mainMeaningWrapper, numberOfMainMeaning)
                    )

            numberOfMainMeaning = numberOfMainMeaning + 1
