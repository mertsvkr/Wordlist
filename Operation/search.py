import requests
from bs4 import BeautifulSoup
from WordStructure.Word import Word

class Searcher:
    def __init__(self, word):
        self.word = word
        req = requests.get(self.editLink(word))
        self.soup = BeautifulSoup(req.text,"html.parser")

        if not self.isWordNotFound():
            self.takeEntryWrapper()
            self.word = Word(self.entryWrapper[0])

    def editLink(self, word):
        """

        takes word and adds it to link
        :param word: word or phrases searching for
        :return: returns edited link
        """
        link = "https://en.oxforddictionaries.com/definition/"
        word.replace(" ", "_")
        link = link + word
        return link

    def takeEntryWrapper(self):
        """
        takes entryWrapper from html code
        """
        self.entryWrapper = self.soup.findAll("div", {"class":"entryWrapper"})

    def isWordNotFound(self):
        """
        if not found any result, notFound variable will be empty list
        :return: if notFound is empty list, there is no result
        """
        notFound = self.soup.findAll("div", {"class": "no-exact-matches"})
        return notFound
