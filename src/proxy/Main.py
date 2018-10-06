from PrinterProxy import PrinterProxy

p = PrinterProxy("Alice")
print("现在的名字是{0}。".format(p.getPrinterName()))
p.setPrinterName("Bob")
print("现在的名字是{0}。".format(p.getPrinterName()))
p.print("Hello, world.")