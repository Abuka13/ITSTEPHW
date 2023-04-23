class MainClass:
    def __init__(self, tx):
        self.text = tx
    def replace(self, tx):
        if tx:
            self.text = self.text + tx
        else:
            self.text = ""
    def print_text(self):
        return self.text
class ChildClass(MainClass):
    def __init__(self, text, n):
        super().__init__(text)
        self.number = n
    def print_number(self):
        return self.number