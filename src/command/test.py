from  tkinter import *

top=Tk()
top.title("简单绘画")
top.geometry("400x300+300+200")

# width,height:设置画布的宽高，bg:设置背景色
can=Canvas(top,width=400,height=300,bg="orange")
# 绘制一条线，起点--终点，线宽
can.create_line((0,0),(200,200),width=4)
# 绘制文字，前两个参数为字的位置
can.create_text(300,30,text="绘制")
# 布局方式
can.pack()

top.mainloop()