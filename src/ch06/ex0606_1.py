import tkinter

root = tkinter.Tk()
root.title("캔버스 도형 그리기")
root.geometry("500x400")

canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

canvas.create_text(250, 25, text="문자열", fill="green", font=("Time New Roman", 24))

canvas.create_line(30, 30, 70, 80, fill="navy", width=5)

canvas.create_line(120, 20, 80, 50, 200, 80, 140, 120, fill="blue", smooth=True)

canvas.create_rectangle(40, 140, 160, 200, fill="lime")

canvas.create_rectangle(20, 240, 120, 369, fill="pink", outline="red")

canvas.create_oval(250 -40, 100 - 40, 250 + 40, 100 + 40, fill="silver", outline="purple")

canvas.create_oval(250 -80, 200 - 40, 250 + 80, 200 + 40, fill="cyan", width=0)

canvas.create_polygon(250, 250, 150, 350, 350, 350, fill="magenta", width=0)

canvas.create_arc(400 - 50, 100 - 50, 400 + 50, 100 + 50, fill="yellow", start=30, extent=300)

canvas.create_arc(400 - 50, 250 - 50, 400 + 50, 250 + 50, fill="gold", start=0, extent=120, style=tkinter.CHORD)

canvas.create_arc(400 - 50, 350 - 50, 400 + 50, 350 + 50, outline="orange", start=0, extent=120, style=tkinter.ARC)

root.mainloop()
