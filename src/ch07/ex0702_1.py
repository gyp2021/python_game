import tkinter

def click_btn():
    text.insert(tkinter.END, "몬스터가 나타났다.")

root = tkinter.Tk()
root.title("멀티라인 텍스트 입력 필드")
root.geometry("400x200")

button = tkinter.Button(text="메시지", command=click_btn)
button.pack()

text = tkinter.Text()
text.pack()

root.mainloop()
