from Printable import Printable
import time

class Printer(Printable):
    def __init__(self, name=None):
        if name:
            self.name = name
            self.__heavyJob("正在生成Printer的实例({0})".format(self.name))
        else:
            self.__heavyJob("正在生成Printer的实例")

    def setPrinterName(self, name):
        self.name = name

    def getPrinterName(self):
        return self.name

    def print(self,string):
        print("=== {0} ===".format(self.name))
        print(string)

    def __heavyJob(self, msg):
        print(msg, end='')
        for i in range(5):
            time.sleep(1)
            print(".", end='')
        print("结束。")


