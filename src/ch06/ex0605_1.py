import tkinter

root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

root.mainloop()
