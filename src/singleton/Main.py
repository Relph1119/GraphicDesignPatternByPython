import Singleton

print("Start.")
obj1 = Singleton.Singleton()
obj2 = Singleton.Singleton()

if obj1 == obj2:
    print("obj1与obj2是相同的实例")
else:
    print("obj1与obj2是不同的实例")

print("End.")


