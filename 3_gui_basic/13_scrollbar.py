from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set) # yscrollcommand 없으면 다시 본래위치로 돌아가서 내용과 연결이 안됌
for i in range(1, 32): # 1 ~ 31 일
    listbox.insert(END, str(i) + "일") # 1일, 2일, ...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 매핑 해줌으로써 정상적으로 작동하게끔 함
# 스크롤의 위치는 업데이트가 되나 스크롤을 이용해서 위치를 바꾸지는 못함

root.mainloop()