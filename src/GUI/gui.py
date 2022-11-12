import tkinter as tk

main = tk.Tk()

main.geometry("1000x600")
main.title("Face Recognition")

label = tk.Label(main, text="Face Recognition", font=("Arial", 18), pady=30)
label.pack()

canvas = tk.Canvas(main, height=5, width=1000)
line = canvas.create_line(25, 5, 975, 5, fill="black")
canvas.pack()

frame1 = tk.Frame(main,width=318,height=450,cursor = "target")
frame1.place(x=20,  y=100,  relx=0.01,  rely=0.01)

frame2 = tk.Frame(main, width=316, height=450, cursor="target")
frame2.place(x=323,  y=100,  relx=0.01,  rely=0.01)

frame3 = tk.Frame(main, width=316, height=450, cursor="target")
frame3.place(x=639,  y=100,  relx=0.01,  rely=0.01)

label2 = tk.Label(frame1, text="Insert Your Dataset", font=("Arial", 12))
label2.pack(padx=(26,0))

button1 = tk.Button(frame1, text="Choose File", font=("Arial", 12))
button1.pack()

label3 = tk.Label(frame1, text="Insert Your Image", font=("Arial", 12))
label3.pack(padx=(26,0),pady=(40,0))

button2 = tk.Button(frame1, text="Choose File", font=("Arial", 12))
button2.pack()

label4 = tk.Label(frame1, text="Result", font=("Arial", 15))
label4.pack(anchor = "w",padx = (26,0), pady=(40,0))

label5 = tk.Label(frame2, text="Test Image", font=("Arial", 15))
label5.pack(anchor = "w")

imageframe1 = tk.LabelFrame(frame2, width=256, height=256)
imageframe1.pack()

label6 = tk.Label(frame3, text="Result", font=("Arial", 15))
label6.pack(anchor="w")

imageframe2 = tk.LabelFrame(frame3, width=256, height=256)
imageframe2.pack()

main.mainloop()