import sys
from abstractFactory.factory.Factory import Factory

def main():
    if len(sys.argv) != 3:
        usage()

    factory = Factory.get_factory(sys.argv[1], sys.argv[2])

    people = factory.create_link("人民日报", "http://www.people.com.cn/")
    gmw = factory.create_link("光明日报", "http://www.gmw.cn/")
    us_yahoo = factory.create_link("Yahoo!", "http://www.yahoo.com/")
    jp_yahoo = factory.create_link("Yahoo!Japan", "http://www.yahoo.co.jp/")
    excite = factory.create_link("Excite", "http://www.excite.com/")
    google = factory.create_link("Google", "http://www.google.com/")

    traynews = factory.create_tray("日报")
    traynews.add(people)
    traynews.add(gmw)

    trayyahoo = factory.create_tray("Yahoo!")
    trayyahoo.add(us_yahoo)
    trayyahoo.add(jp_yahoo)

    traysearch = factory.create_tray("检索引擎")
    traysearch.add(trayyahoo)
    traysearch.add(excite)
    traysearch.add(google)

    page = factory.create_page("LinkPage", "杨文轩")
    page.add(traynews)
    page.add(traysearch)
    page.output()

def usage():
    print("Usage: python {0} module.name class.name.of.ConcreteFactory".format(sys.argv[0]))
    print("Example 1: python Main.py abstractFactory.listfactory.ListFactory ListFactory")
    print("Example 1: python Main.py abstractFactory.tablefactory.TableFactory TableFactory")
    sys.exit(0)

main()

