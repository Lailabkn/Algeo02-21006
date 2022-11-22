import tkinter as tk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
from InputGambar import *
import numpy as np
from eigen import *
import cv2
import timeit

main = tk.Tk()

main.geometry("1000x600")
main.title("Face Recognition")

img = tk.PhotoImage(file=".\src\Frame.png", master=main)
img_label = tk.Label(main, image=img)
img_label.place(x=0, y=0)

def choose_folder():
    global mean
    global eigenfaces
    global weight
    global S
    folder_selected = fd.askdirectory()
    if folder_selected:
        S = np.array(load_images_folder(".\dataset"))
        H = np.transpose(S)
        mean = np.mean(S, axis=0) # Calculate mean of images
        meanimage = mean.reshape(256, 256)
        sel = np.array(abs(S - mean))# Calculate difference between images and mean
        trans = np.transpose(sel)
        cov = np.array(np.matmul(sel, trans))# Calculate covariance of difference
        cov = cov/len(cov)
        eigenvector = np.array(eigVec(cov)) # Calculate eigen vector of covariance

        for i in range(len(eigenvector)):
            norm = Normalize(eigenvector[i])
            eigenvector[i] = eigenvector[i]/norm

        eigenfaces = np.array(np.matmul(eigenvector.T, sel)) # Calculate eigen face
        weight = np.array(np.matmul(eigenfaces, sel.T))
        showinfo("Folder Selected", folder_selected)


def choose_file():
    global mins
    global weighttest
    global TestFace
    # START TIMER
    global start
    start = timeit.default_timer()
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

        TestFace = np.array(load_images_file(filename))
        selisihface = np.array(abs(TestFace - mean))
        selisihfaces = selisihface.reshape(65536, 1)
        weighttest = np.array(np.matmul(eigenfaces, selisihfaces))
        a = np.array(np.square(weight - weighttest))
        b = np.sum(a, axis=0)
        eucl = np.sqrt(b) 
        mins = min(eucl)
        percent_result = (mins/Normalize(weighttest))*100 # Calculate percentage of result
        res = tk.Label(main, text=percent_result) # show label
        res.place(x=135, y=423) # show label
        if (mins < 0.5):
            for i in range (len(eucl)):
                if eucl[i] == mins:
                    hasil = i+1
            for i in range(len(S)):
                if i == hasil-1:
                    img = S[i].reshape(256,256)
                    img = Image.fromarray(img)
                    img = img.resize((256,256), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    panel = tk.Label(main, image=img)
                    panel.image = img
                    panel.place(x=680, y=220)
                    result_time()
        else:
            showinfo("Result", "Not Found")

def result_time():
    global hours
    global minutes
    global secs
    global text
    global milisec
    stop = timeit.default_timer()
    total = stop - start
    minutes, secs = divmod(total, 60)
    hours, minutes = divmod(minutes, 60)
    text = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(secs))
    time = tk.Label(main, text=text)
    time.place(x=570, y=520)


button1 = tk.Button(main, text="Choose Folder", font=("Arial", 12), command=choose_folder)
button1.place(x=45, y=238, relx=0.01, rely=0.01)

button2 = tk.Button(main, text="Choose File", font=("Arial", 12), command=choose_file)
button2.place(x=45, y=350, relx=0.01, rely=0.01)

main.mainloop()