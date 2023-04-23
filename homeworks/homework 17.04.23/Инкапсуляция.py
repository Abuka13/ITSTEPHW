class MainClass:
    def __init__(self, tx):
        self.text = tx
    def replace(self, text):
        if text:
            self.text_field = text
        else:
            self.text_field = ""
class ChildClass(MainClass):
    def __init__(self, text, n):
        super().__init__(text)
        self.number = n
