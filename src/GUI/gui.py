import tkinter as tk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo

main = tk.Tk()

main.geometry("1000x600")
main.title("Face Recognition")

img = tk.PhotoImage(file=".\src\GUI\Frame.png", master=main)
img_label = tk.Label(main, image=img)
img_label.place(x=0, y=0)

def display_image():
    filetypes = (('image files', '*.jpg'), ('All files', '*.*'))
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if filename:
        img = Image.open(filename)
        img = img.resize((256,256), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(main, image=img)
        panel.image = img
        panel.place(x=338, y=220)

def choose_folder():
    folder_selected = fd.askdirectory()
    if folder_selected:
        showinfo(title="Folder Selected", message=folder_selected)

button1 = tk.Button(main, text="Choose File", font=("Arial", 12), command=choose_folder)
button1.place(x=45, y=238, relx=0.01, rely=0.01)

button2 = tk.Button(main, text="Choose File", font=("Arial", 12), command=display_image)
button2.place(x=45, y=350, relx=0.01, rely=0.01)

label1 = tk.Label(main, text="result", font=("Arial", 15))
label1.place(x=135, y=423)

label2 = tk.Label(main, text="Time", font=("Arial", 15))
label2.place(x=570, y=520)

main.mainloop()