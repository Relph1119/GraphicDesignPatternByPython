from Gamer import Gamer
import time

gamer = Gamer(100)
memento = gamer.createMemento()
for i in range(100):
    print("==== {0}".format(i))
    print("当前状态：{0}".format(gamer))

    gamer.bet()

    print("所持金钱为 {0} 元".format(gamer.getMoney()))

    if gamer.getMoney() > memento.getMoney():
        print("     (所持金钱增加了许多，因此保存游戏的当前的状态)")
        memento = gamer.createMemento()
    elif gamer.getMoney() < memento.getMoney() / 2:
        print("     (所持金钱减少了许多，因此将游戏恢复至以前的状态)")
        gamer.restoreMomento(memento)

    time.sleep(1)