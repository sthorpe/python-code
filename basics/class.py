
class NameOfClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1)

noc = NameOfClass(param2 = 'dog', param1 = 'cat')
noc.some_method()
