import tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title('ConsumoDatos')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#fff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.60, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=10)
entry.place(rely=0.15, relwidth=0.65, relheight=0.7)

button = tk.Button(frame, text='Consultar', font=10)
button.place(relx=0.7, rely=0.12, relwidth=0.3, relheight=0.7)

lower_frame = tk.Frame(root, bg='#fff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.6, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
