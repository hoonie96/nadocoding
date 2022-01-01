from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")


label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="nadocoding/3_gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2 # Garbage Collection : 불필요한 메모리 공간 해제. global variable(전역 변수) 로 만들지 않으면 픽업해서 버림
    photo2 = PhotoImage(file="nadocoding/3_gui_basic/img2.png")
    label2.config(image=photo2) # 이미지가 사라졌지만 img2 가 적용이 안됨

btn = Button(root, text="클릭", command=change) # button 을 눌렀을 때 commmand 인 change 를 통해 "안녕하세요"를 "또 만나요" 로 변경
btn.pack()


root.mainloop()