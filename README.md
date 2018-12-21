# 记录自己用Python重写《图解设计模式》这本书的示例程序的全部过程
本书上传的所有代码都是可以运行的，在此附上本书源码地址： [http://www.ituring.com.cn/book/1811](http://www.ituring.com.cn/book/1811)<br/>
在此向本书作者和译者表示感谢<br/>
本书采用的是Java版本，笔者采用的**Python语言实现**所有设计模式，如果大家要参考Java版本的设计模式，可以链接到以下地址：
[https://github.com/Relph1119/GraphicDesignPattern](https://github.com/Relph1119/GraphicDesignPattern)

## 运行环境 ##
Python 版本：3.7.2<br/>
PyCharm 版本：PyCharm 2017.3.3 (Professional Edition)

## 代码结构 ##
![](https://i.imgur.com/4SCI2J5.png)
<pre>
src
+---abstractFactory------------------------抽象工厂模式
+---adapter--------------------------------适配器模式
+---bridge---------------------------------桥接模式
+---builder--------------------------------建造者模式
+---chainOfResponsibility------------------职责链模式
+---command--------------------------------命令模式
+---composite------------------------------组合模式
+---decorator------------------------------装饰者模式
+---facade---------------------------------外观模式
+---factoryMethod--------------------------工厂模式
+---flyweight------------------------------享元模式
+---interpreter----------------------------解释器模式
+---iterator-------------------------------迭代模式
+---mediator-------------------------------中介者模式
+---memento--------------------------------备忘录模式
+---observer-------------------------------观察者模式
+---prototype------------------------------原型模式
+---proxy----------------------------------代理模式
+---singleton------------------------------单例模式
+---state----------------------------------状态转换模式
+---strategy-------------------------------策略模式
+---templateMethod-------------------------模版模式
+---visitor--------------------------------访问者模式
images-------------------------------------运行结果截图
</pre>

## 运行结果 ##
### 第一章-Iterator（迭代器）模式 ###
示例
![](https://i.imgur.com/zD4kRhU.png)
### 第二章-Adapter（适配器）模式 ###
示例
![](https://i.imgur.com/dF2y6rk.png)
### 第三章-Template Method（模版）模式 ###
示例
![](https://i.imgur.com/UTQKMNc.png)
### 第四章-Factory Method（工厂）模式 ###
示例
![](https://i.imgur.com/KbSt5if.png)
### 第五章-Singleton（单例）模式 ###
示例
![](https://i.imgur.com/p8sZ4Qn.png)
### 第六章-Prototype（原型）模式 ###
示例
![](https://i.imgur.com/WzfpEdi.png)
### 第七章-Builder（建造者）模式 ###
示例
![](https://i.imgur.com/BglmzM5.png)
![](https://i.imgur.com/TV2Kywn.png)
### 第八章-Abstract Factory（抽象工厂）模式 ###
示例
![](https://i.imgur.com/L082wOr.png)
![](https://i.imgur.com/0L6Bqi7.png)
![](https://i.imgur.com/1TmCJK1.png)
![](https://i.imgur.com/PSUrCvs.png)
### 第九章-Bridge（桥接）模式 ###
示例
![](https://i.imgur.com/H5HZeWl.png)
### 第十章-Strategy（策略）模式 ###
示例
![](https://i.imgur.com/chGkcvK.png)
### 第十一章-Composite（组合）模式 ###
示例
![](https://i.imgur.com/BYFLesj.png)
### 第十二章-Decorator（装饰者）模式 ###
示例
![](https://i.imgur.com/9C9zuXN.png)
### 第十三-Visitor（访问者）模式 ###
示例
![](https://i.imgur.com/KEnQDwl.png)
### 第十四章-Chain of Responsibility（职责链）模式 ###
示例
![](https://i.imgur.com/1C6nFrf.png)
### 第十五章-Facade（外观）模式 ###
示例
![](https://i.imgur.com/duTJUn9.png)
![](https://i.imgur.com/OAfFHVN.png)
### 第十六章-Mediator（中介者）模式 ###
示例
![](https://i.imgur.com/cTiG6Gl.png)
![](https://i.imgur.com/JTuO39p.png)
### 第十七章-Observer（观察者）模式 ###
示例
![](https://i.imgur.com/QuFj9X3.png)
### 第十八章-Memento（备忘录）模式 ###
示例
![](https://i.imgur.com/S1wkyTW.png)
### 第十九章-State（状态转换）模式 ###
示例
![](https://i.imgur.com/Elukzyp.png)
### 第二十章-Flyweight（享元）模式 ###
示例
![](https://i.imgur.com/IfMmait.png)
### 第二十一章-Proxy（代理）模式 ###
示例
![](https://i.imgur.com/9WXOXnS.png)
### 第二十二章-Command（命令）模式 ###
示例
![](https://i.imgur.com/vs0LBIg.png)
### 第二十三章-Interpreter（解释器）模式 ###
示例
![](https://i.imgur.com/kI7kowE.png)

## 总结 ##
1. 前后用了2天多的时间用Python重写了一遍《图解设计模式》中的示例代码，对于Python语言的使用更加熟练了。
2. 上面23个设计模式，只有Mediator模式的重写还没有完成，程序总是报错，可能不支持tkinter的控件继承，该模式的Main.py是整合好的程序，可以运行。
3. 对于Facade模式中的读取maildata.txt文件，由于Python没有Java Properties的类，笔者参照网上的方法，自己实现了一个。
4. 对于Interpreter模式中词分处理，由于没有Java StringTokenizer类，笔者直接在Context中实现了该类的方法。
5. 其中的几个GUI编程，采用的是Python自带的tkinter包，目前已经熟练使用Text, Button, Canvas, Label, Entry等控件。
6. 2018年12月5日 按照Effective Python中的进行代码优化。
7. 2018年12月21日 按照PEP8 进行代码优化。

## 编程时的Tips ##
1. 对于Python的循环继承的处理，可以所用到的方法内声明导入类。
2. 针对Python的动态读取类信息，并生成类的实例可采用以下代码实现<pre>
    @staticmethod
    def get_factory(module_name, class_name):
        module = importlib.import_module(module_name)
        aclass = getattr(module, class_name)
        factory = aclass()
        return factory
</pre>
3. Python中并没有接口类的概念，由于可以多重继承，可采用以下代码实现<pre>
    class Print(object):
        @classmethod
        def print_weak(cls):
            pass
        @classmethod
        def print_strong(cls):
            pass
</pre>
4. 在主程序内开启子线程，退出主程序之后，子线程依然会执行，可以采用标志位判断之后break，退出子线程，可参考State模式的示例代码。<br/>
以下内容引用Python开发手册中关于杀死线程的警告：<pre>
不要试图用强制方法杀掉一个python线程，这从服务设计上就存在不合理性。 
多线程本用来任务的协作并发，如果你使用强制手段干掉线程，那么很大几率出现意想不到的bug。
</pre>