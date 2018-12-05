from decorator.StringDisplay import StringDisplay
from decorator.SideBorder import SideBorder
from decorator.FullBorder import FullBorder

if __name__ == '__main__':
    b1 = StringDisplay("Hello, world.")
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)

    b1.show()
    b2.show()
    b3.show()

    b4 = SideBorder(FullBorder(FullBorder(SideBorder(FullBorder(StringDisplay("你好，世界。")), '*'))),'/')
    b4.show()