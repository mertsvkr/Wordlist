from PyQt5.QtWidgets import QVBoxLayout

class ElementWrapper(QVBoxLayout):
    """
    This class is a wrapper for GUI elements to set margins easily
    """

    def __init__(self, element):
        """
        :param element: element to be wrapped
        :type element: any QtWidgets type (button, widget, lineedit etc...)
        """
        super().__init__()
        self.element = element
        self.addWidget(self.element)
