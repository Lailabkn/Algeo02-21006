import tkinter as tk
from PIL import ImageTk, Image

main = tk.Tk()

main.geometry("1000x600")
main.title("Face Recognition")

img = tk.PhotoImage(file=".\src\GUI\Frame.png", master=main)
img_label = tk.Label(main, image=img)
img_label.place(x=0, y=0)

button1 = tk.Button(main, text="Choose File", font=("Arial", 12))
button1.place(x=45, y=238, relx=0.01, rely=0.01)

button2 = tk.Button(main, text="Choose File", font=("Arial", 12))
button2.place(x=45, y=350, relx=0.01, rely=0.01)

main.mainloop()