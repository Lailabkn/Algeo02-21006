import tkinter as tk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
from InputGambar import *
import numpy as np
from eigen import *
import cv2
import timeit

# START GUI
main = tk.Tk()

# SET WINDOW SIZE
main.geometry("1000x600")
main.title("Face Recognition")

# SET BACKGROUND
img = tk.PhotoImage(file=".\src\Frame.png", master=main)
img_label = tk.Label(main, image=img)
img_label.place(x=0, y=0)

# SET BUTTON CHOOSE FOLDER
def choose_folder():
    global mean
    global eigenfaces
    global weight
    global S
    folder_selected = fd.askdirectory() # choose folder from file explorer
    if folder_selected:
        S = np.array(load_images_folder(folder_selected)) # load images from folder
        mean = np.mean(S, axis=0) # Calculate mean of images
        sel = np.array(abs(S - mean))# Calculate selisih matrix S dan mean
        trans = np.transpose(sel) # Transpose difference
        cov = np.array(np.matmul(sel, trans))# Calculate covariance of difference
        cov = cov/len(cov)
        eigenvector = np.array(eigVec(cov)) # Calculate eigen vector of covariance

        for i in range(len(eigenvector)): 
            norm = Normalize(eigenvector[i]) # Normalize eigen vector
            eigenvector[i] = eigenvector[i]/norm 

        eigenfaces = np.array(np.matmul(eigenvector.T, sel)) # Calculate eigen face
        weight = np.array(np.matmul(eigenfaces, sel.T)) # Calculate weight of eigen face
        showinfo("Folder Selected", folder_selected) # show folder selected

# SET BUTTON CHOOSE IMAGE
def choose_file():
    global mins
    global weighttest
    global TestFace
    # START TIMER
    global start
    start = timeit.default_timer() # start timer
    filetypes = (('image files', '*.jpg'), ('All files', '*.*')) # set file type
    filename = fd.askopenfilename( # choose file from file explorer
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if filename: # if file selected
        img = Image.open(filename) # open image 
        img = img.resize((256,256), Image.ANTIALIAS) # resize image ke 256 x 256
        img = ImageTk.PhotoImage(img) # convert image to tkinter image
        panel = tk.Label(main, image=img) 
        panel.image = img # set image to panel
        panel.place(x=338, y=220) # set panel position

        TestFace = np.array(load_images_file(filename)) # load image from file
        selisihface = np.array(abs(TestFace - mean)) # calculate selisih matrix test face dan mean
        selisihfaces = selisihface.reshape(65536, 1) # reshape selisih face 
        weighttest = np.array(np.matmul(eigenfaces, selisihfaces)) # calculate weight of test face
        a = np.array(np.square(weight - weighttest)) # calculate akar kuadrat weight test face dan weight eigen face
        b = np.sum(a, axis=0) # sum of akar kuadrat weight test face dan weight eigen face
        eucl = np.sqrt(b) # euclidean distance
        mins = min(eucl) # minimum euclidean distance
        percent_result = (mins/Normalize(weighttest))*100 # Calculate percentage of result
        res = tk.Label(main, text=percent_result) # show label
        res.place(x=135, y=423) # show label
        if (mins < 0.5): # if minimum euclidean distance < 0.5
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
                    panel.place(x=680, y=220) # show image result
                    result_time()  # show time result
        else:
            showinfo("Result", "Not Found")     #kondisi jika tidak ditemukan 

# SET RESULT TIME
def result_time(): 
    global hours
    global minutes
    global secs
    global text
    global milisec
    stop = timeit.default_timer() # stop timer
    total = stop - start # calculate total time
    minutes, secs = divmod(total, 60) 
    hours, minutes = divmod(minutes, 60)
    text = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(secs)) # set time format
    time = tk.Label(main, text=text) 
    time.place(x=570, y=520) # show time result


button1 = tk.Button(main, text="Choose Folder", font=("Arial", 12), command=choose_folder) # set button choose folder
button1.place(x=45, y=238, relx=0.01, rely=0.01) # set button choose folder position

button2 = tk.Button(main, text="Choose File", font=("Arial", 12), command=choose_file) # set button choose file
button2.place(x=45, y=350, relx=0.01, rely=0.01) # set button choose file position

main.mainloop() # run mainloop