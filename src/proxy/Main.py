from PrinterProxy import PrinterProxy

if __name__ == '__main__':
    p = PrinterProxy("Alice")
    print("现在的名字是{0}。".format(p.getPrinterName()))
    p.setPrinterName("Bob")
    print("现在的名字是{0}。".format(p.getPrinterName()))
    p.print("Hello, world.")