from Tkinter import *
from tkFileDialog import *
import threading
import tkMessageBox
class MainGui():


    def __init__(self):

        self.root = Tk()
        self.root.wm_title("Remote Snap Server")
        self.mainframe = Frame(self.root, relief='flat', borderwidth=20)
        self.running = False
        self.dir = NONE
        main = self.mainframe
        main.grid(row=1)
        #hello = Label(main,text='Remote Snap Python')
        #hello.grid(row=1)



        path = Entry(main)
        path.grid(row=2, padx=5, pady=5)
        self.path = path;
        choosbtn = Button(main,text='choose',command=self.chooseDir)
        choosbtn.grid(row=2,column=1)


        runbtn = Button(main,text="Start",command=self.runServer)
        runbtn.grid(row=3,columnspan=1)
        self.runbtn=runbtn;

        self.dir_opt = options = {}
        options['initialdir'] = '~'
        options['mustexist'] = False
        options['parent'] = self.root
        options['title'] = 'This is a title'




    def start(self):
        self.root.mainloop()


    def chooseDir(self):
        myPath =askdirectory(**self.dir_opt)
        self.dir = myPath
        self.path.insert(1,myPath)

    def runServer(self):


        if self.dir is not NONE:

            self.running = not self.running


            if self.running:
                self.runbtn.config(text='stop')
                self.runningLbl= Label(self.mainframe,text="running")
                self.runningLbl.grid(row=0,columnspan=1)

            else:
                self.runbtn.config(text='start')
                self.runningLbl.grid_forget()

            print self.running;
        else:
            tkMessageBox.showwarning(
            "Open file",
            "Choose a directory"
            )
        return

gui = MainGui()

gui.start()