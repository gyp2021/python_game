import tkinter

root = tkinter.Tk()
root.title("첫 번째 버튼")

canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack()

gazou = tkinter.PhotoImage(file="d:\github\gyp2021\python_game\src\ch06\hyunju.png")
canvas.create_image(200, 300, image=gazou)

root.mainloop()
