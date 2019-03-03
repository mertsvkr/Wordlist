from bs4 import BeautifulSoup
from WordStructure.WordType import WordType

class Word:
    def __init__(self, entryWrapper):
        self.word = self.setWord(entryWrapper)
        self.wordTypes = dict()
        self.setWordTypes(entryWrapper)
        self.isAdded = False

    def setWord(self,entryWrapper):
        """
        parses entry wrapper and takes word
        :param entryWrapper: html div class to hold all about the word
        :return: searching word
        """
        headWord = entryWrapper.findChildren("span", {"class": "hw"})
        return headWord[0].text

    def setWordTypes(self,entryWrapper):
        """
        parses entryWrapper and sets word types
        :param entryWrapper: html div class to hold all about the word
        """
        # gramb is wrapper for every word type in html code
        grambs = entryWrapper.findChildren("section", {"class": "gramb"})
        if grambs:
            for gramb in grambs:
                type = gramb.findAll("span", {"class": "pos"})
                type = type[0]
                self.wordTypes.update({type.text: WordType(self.word, gramb, type)})
