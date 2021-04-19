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

root.mainloop()
