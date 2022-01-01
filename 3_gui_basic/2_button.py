from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2222222222") # padding 을 Button 안에서 확보 (여백)
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4444444444") # Button 사이즈를 고정 (고정크기)
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg = foreground = 글자 색깔, bg = background = 배경 색깔
btn5.pack()

photo = PhotoImage(file="nado_coding/3_gui_basic/img.png")# 파일에 해당 하는 것을 불러와서 'photo' 로 저장해줌
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop()