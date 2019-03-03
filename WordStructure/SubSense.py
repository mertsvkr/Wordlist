from bs4 import BeautifulSoup

class SubSense:
    def __init__(self, relatedType, relatedMainMeaningNumber, subSenseNumber, subSense, subSenseWrapper):
        self.relatedType = relatedType
        self.relatedMainMeaningNumber = relatedMainMeaningNumber
        self.subSense = subSense
        self.subSenseNumber = subSenseNumber
        self.examples = list()
        self.setExamples(subSenseWrapper)
        self.isAdded = False
    def setExamples(self, subSenseWrapper):
        """
        parses mainMeaningWrapper and sets examples which belongs to main meaning
        :param mainMeaningWrapper: it holds main meaning, its examples; also  subsenses and subsenses' examples
        """
        # trg is inner wrapper for mainMeaningWrapper contents
        trg = subSenseWrapper.findChild("div", {"class": "trg"})

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


