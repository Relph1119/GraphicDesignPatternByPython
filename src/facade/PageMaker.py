from facade.HtmlWriter import HtmlWriter
from facade.Database import Database
import time

class PageMaker():

    @staticmethod
    def makeWelcomePage(mailaddr, filename):
        mailprop = Database.getProperties("maildata")
        username = mailprop.get(mailaddr)
        file = open(filename, 'w', encoding='gbk')
        writer = HtmlWriter(file)
        writer.title("Welcome to " + username + "'s page!")
        writer.paragraph("欢迎来到" + username + " 的主页。")

        now = int(time.time())
        timeStruct = time.localtime(now)
        strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
        writer.paragraph(" 当前创建时间：" + strTime)
        writer.paragraph(" 等着你的邮件哦！ ")
        writer.mailto(mailaddr, username)
        writer.close()
        print(filename + " is created for " + mailaddr + " ( " + username + ")")
