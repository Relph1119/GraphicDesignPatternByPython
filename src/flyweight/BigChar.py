class BigChar():
    def __init__(self, charname):
        self.charname = charname
        self.fontdata = ""
        file = open("big{0}.txt".format(self.charname), "r")
        for line in file:
            self.fontdata += line

    def print(self):
        print(self.fontdata)