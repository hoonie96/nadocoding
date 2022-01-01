import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # mode 왔다 갔다 반복 진행
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # mode 처음 부터 끝 까지 진행
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn1 = Button(root, text="중지", command=btncmd)
# btn1.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기
        
        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # UI 업데이트. 없으면 한꺼번에 업데이트 되서 보임 
        print(p_var2.get())

btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop()