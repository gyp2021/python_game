import tkinter

def check():
    if cval.get() == True:
        print("체크 설정")
    else :
        print("체크 해제")

root = tkinter.Tk()
root.title("체크 버튼 상태 확인")
root.geometry("400x200")

cval = tkinter.BooleanVar()
cval.set(False)

cbtn = tkinter.Checkbutton(text="체크 버튼", variable=cval, command=check)
cbtn.pack()

root.mainloop()
