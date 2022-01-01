from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로


# 여러 라인의 텍스트를 필요로 할 때
txt = Text(root, width=30, height=5) # 텍스트 위젯 만들기
txt.pack()
txt.insert(END, "글자를 입력하세요")

# 한 줄의 텍스트만 필요로 할 때
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요") # 현재는 값이 비어 있으므로 END 를 써도 동일함

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1.0(1 : 첫번째 라인, 0: 0번째 column 위치) 에서 END 까지
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END) # insert 에서의 0 부터 끝(END)까지

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()