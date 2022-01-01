# Quiz) tkinter 를 이용한 메모장 프로그램을 ㅁ나드시오

# [GUI 조건]
# 1. title : 제목 없음 - Windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 status 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기

from tkinter import *
import tkinter.messagebox as msgbox


root = Tk()
root.title("Windows 메모장")
root.geometry("640x480") # 가로 * 세로

def open_file():
    print("open file") # 파일을 열 수 있는 창을 띄움 

def save_file():
    print("save file") # 파일을 저장 할 수 창을 띄움 

def exit_file():
    response = msgbox.askyesnocancel(title=None, message="파일이 저장되지 않았었을 수도 있습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답:", response) # True, False, None -> 예 1, 아니오 0, 그 외
    if response == 1: # return save_file() 열어서 다시 저장하게끔 하기
        print("예")
        save_file()
    elif response == 0: # 아니오 
        print("아니오")
        root.quit() # 프로그램 닫기
    else:
        print("취소")

menu= Menu(root)


# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="파일 메뉴", state="disable")
menu_file.add_separator()
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=exit_file)
menu.add_cascade(label="파일", menu=menu_file)


# 편집 메뉴
menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="편집 메뉴", state="disable")
menu.add_cascade(label="편집", menu=menu_edit)

# 서식 메뉴
menu_form = Menu(menu, tearoff=0)
menu_form.add_command(label="서식 메뉴", state="disable")
menu.add_cascade(label="서식", menu=menu_form)

# 보기 메뉴
menu_option = Menu(menu, tearoff=0)
menu_option.add_command(label="보기 메뉴", state="disable")
menu.add_cascade(label="보기", menu=menu_option)

# 도움말 메뉴
menu_help = Menu(menu, tearoff=0)
menu_help.add_command(label="도움말 메뉴", state="disable")
menu.add_cascade(label="도움말", menu=menu_help)

root.config(menu=menu)
root.mainloop()