import tkinter

def click_btn():
    button["text"] = "클릭했습니다"

root = tkinter.Tk()
root.title("첫 번째 버튼")
root.geometry("800x600")

button = tkinter.Button(root, text="버튼 문자열", font=("궁서", 24), command=click_btn)
button.place(x=200, y=100)

root.mainloop()
