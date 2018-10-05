import sys
from TextBuilder import TextBuilder
from HTMLBuilder import HTMLBuilder
from Director import Director

def main():
    if len(sys.argv) != 2:
        usage()

    if sys.argv[1] == "plain":
        textbuilder = TextBuilder()
        director = Director(textbuilder)
        director.construct()
        result = textbuilder.get_result()
        print(result)
    elif sys.argv[1] == "html":
        htmlbuilder = HTMLBuilder()
        director = Director(htmlbuilder)
        director.construct()
        filename = htmlbuilder.get_result()
        print("{0}文件编写完成。".format(filename))

def usage():
    print("Usage: python {0} plain 编写纯文本文档".format(sys.argv[0]))
    sys.exit(0)

main()