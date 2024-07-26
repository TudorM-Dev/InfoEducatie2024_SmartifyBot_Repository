# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2

# Create an instance of TKinter Window or frame
win= Tk()

# Set the size of the window
win.geometry("1280x720")# Create a Label to capture the Video frames
label =Label(win)
label.grid(row=0, column=0)
cap= cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   label.after(20, show_frames)

    # Repeat after an interval to capture continiously

show_frames()
win.mainloop()