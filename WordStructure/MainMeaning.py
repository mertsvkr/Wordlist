from bs4 import BeautifulSoup
from WordStructure.SubSense import SubSense

class MainMeaning:
    def __init__(self, type, mainMeaning, mainMeaningWrapper, mainMeaningNumber):
        self.relatedWordType = type
        self.mainMeaning = mainMeaning
        self.mainMeaningNumber = mainMeaningNumber
        self.examples = list()
        self.subSenses = list()
        self.setExamples(mainMeaningWrapper)
        self.setSubSenses(mainMeaningWrapper)
        self.isAdded = False

    def setExamples(self, mainMeaningWrapper):
        """
        parses mainMeaningWrapper and sets examples which belongs to main meaning
        :param mainMeaningWrapper: it holds main meaning, its examples; also  subsenses and subsenses' examples
        """
        # trg is inner wrapper for mainMeaningWrapper contents
        trg = mainMeaningWrapper.findChild("div", {"class": "trg"})

        #class name for examples is "exg"
        exg = trg.findChild("div", {"class":"exg"})
        if exg:
            example = exg.findChild("div", {"class": "ex"})
            if example:
                self.examples.append(example.text)

            examples = exg.find_next_siblings("div", {"class": "exg"})
            if examples:
                for example in examples:
                    example = example.findChild("div", {"class": "ex"})
                    if example:
                        self.examples.append(example.text)

        #class name for wrapper which holds additional examples is "examples". So first we should go into the wrapper
        additionalExampleWrapper = trg.findChild("div", {"class": "examples"})
        if additionalExampleWrapper:
            examples = additionalExampleWrapper.findAll("li", {"class": "ex"})
            if examples:
                for example in examples:
                    self.examples.append(example.text)



    def setSubSenses(self, mainMeaningWrapper):
        """
        parses mainMeaningWrapper and adds subsenses into self.subSenses list
        :param mainMeaningWrapper: it holds main meaning, its examples; also  subsenses and subsenses' examples
        """
        subSensesWrapper = mainMeaningWrapper.findChild("ol", {"class": "subSenses"})
        if subSensesWrapper:
            subSenses = subSensesWrapper.findChildren("li", {"class": "subSense"})
            if subSenses:
                for subSense in subSenses:
                    #find subSenseNumber
                    iterationNumberWrapper = subSense.findChild("span", {"subsenseIteration"})
                    if iterationNumberWrapper:
                        iterationNumber = iterationNumberWrapper.text.split('.', 1)[1]
                    #find subSense's itself
                    subMeaning = subSense.findChild("span",{"class": "ind"})
                    if subMeaning:
                        subMeaning = subMeaning.text
                        self.subSenses.append(SubSense(self.relatedWordType, self.mainMeaningNumber, iterationNumber, subMeaning,subSense))
