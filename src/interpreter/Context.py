from interpreter.PraseException import PraseException


class Context:
    currentIndex = 0
    __currentToken = None

    def __init__(self, text):
        self.context = text.split(" ")
        self.nextToken()

    def nextToken(self):
        if self.currentIndex < len(self.context):
            self.__currentToken = self.context[self.currentIndex]
            self.currentIndex += 1
        else:
            self.currentToken = None

    def currentToken(self):
        return self.__currentToken

    def skipToken(self, token):
        if token != self.__currentToken:
            raise PraseException("Warning: {0} is expected, but {1} is found.".format(token, self.__currentToken))
        self.nextToken()
