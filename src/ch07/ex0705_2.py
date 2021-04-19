import tkinter

root = tkinter.Tk()
root.title("고양이 지수 진단")
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

gazou = tkinter.PhotoImage(file="d:\github\gyp2021\python_game\src\ch07\mina.png")
canvas.create_image(400, 300, image=gazou)

button = tkinter.Button(text="진단하기", font=("Times New Roman", 32))
button.place(x=400, y=480)

text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

b_var = [None] * 7
c_btn = [None] * 7
ITEM = [
    "높은 곳이 좋다.",
    "공을 보면 굴리고 싶어진다.",
    "깜짝 놀라면 털이 곤두선다.",
    "쥐구멍이 마음에 든다.",
    "개에게 적대감을 느낀다.",
    "생선 뼈를 발라 먹고 싶다.",
    "밤, 기운이 난다."
]
for i in range(7):
    b_var[i] = tkinter.BooleanVar()
    b_var[i].set(False)
    c_btn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), variable=b_var[i], bg="#dfe")
    c_btn[i].place(x=400, y=160 + 40 * i)

root.mainloop()
