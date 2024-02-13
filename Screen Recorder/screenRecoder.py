from tkinter import *
import pyscreenrec



root = Tk()
root.geometry("400x600")
root.title("Screnn Recorder")
root.config(bg="#345360")
root.resizable(False,False)

def start_rec():
    file = fileName.get()
    rec.start_recording(str(file+".mp4"),5)

def pause_rec():
   rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()




rec = pyscreenrec.ScreenRecorder()

image_icon = PhotoImage(file="png-clipart-logo-screen-recorder-blue-logo-thumbnail.png")
root.iconphoto(False,image_icon)

image1 = PhotoImage(file="background2.png")
Label(root,image=image1).place(width=400,height=600)

fileName = StringVar()
entry = Entry(root,textvariable=fileName,width=18,font="arial 15")
entry.place(x=70,y=395)
fileName.set("recording3")

start_btn = Button(root,text="Start",font="arial 20",bd=0,bg="#5361d0",border=10,command=start_rec)
start_btn.place(x=115,y=196)

pause_pic = PhotoImage(file="background4.png")
pause = Button(root,image=pause_pic,bd=0,border=5,command=pause_rec)
pause.place(x=50,y=450,width=80,height=80)

resume_pic = PhotoImage(file="background5.png")
resume = Button(root,image=resume_pic,bd=0,border=5,command=pause_rec)
resume.place(x=150,y=450,width=80,height=80)

stop_pic = PhotoImage(file="background6.png")
stop = Button(root,image=stop_pic,bd=0,border=5,command=stop_rec)
stop.place(x=250,y=450,width=80,height=80)

root.mainloop()