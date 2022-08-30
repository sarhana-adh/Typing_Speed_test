import tkinter as tk
import time 
import threading 
import random 

class TypeSpeedGUI:

    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600") # change this 
        self.frame=tk.Frame(self.root)
        self.running=False
        self.texts=open("Sample.txt","r").read().split("\n")


        self.sample_label= tk.Label(self.frame,text=random.choice(self.texts),font=("Helvetica",18))
        self.sample_label.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

        self.input=tk.Entry(self.frame,width=40,font=("Helvetica",24))
        self.input.grid(row=1,column=0,columnspan=2,padx=5,pady=10)
        self.input.bind("<KeyPress>",self.start)

        self.speed_label= tk.Label(self.frame,text="Speed:\n 0.00 CPS\n 0.00 CPM \n 0.00 WPS\n 0.00 WPM",font=("Helvetica",18))
        self.speed_label.grid(row=2,column=0,columnspan=2,padx=5,pady=10)

        self.reset_button=tk.Button(self.frame,text="Reset",command=self.reset)
        self.reset_button.grid(row=3,column=0,columnspan=2,padx=5,pady=10)

        self.frame.pack(expand=True)
        self.counter=0
        
        self.root.mainloop()

    def start(self,event):
        if not self.running:
            if not event.keycode in [16,17,18]:
                self.running=True
                t= threading.Thread(target=self.time_threading)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input.get()):
            self.input.config(fg="red")
        else: 
            self.input.config(fg="black")
        if self.input.get()==self.sample_label.cget('text'):
            self.running=False
            self.input.config(fg="green")


    def time_threading(self):
        while self.running:
            time.sleep(0.1)
            self.counter+=0.1
            cps= len(self.input.get())/self.counter
            cpm=cps*60
            wps= len(self.input.get().split(" "))/self.counter
            wpm=wps*60
            self.speed_label.config(text=f'Speed:\n {cps:.2f} CPS\n {cpm:.2f} CPM \n {wps:.2f} WPS\n {wpm:.2f} WPM')
    def reset(self):
        self.running=False
        self.counter=0
        self.speed_label.config(text="Speed:\n 0.00 CPS\n 0.00 CPM \n 0.00 WPS\n 0.00 WPM")
        self.sample_label.config(text=random.choice(self.texts))
        self.input.delete(0,tk.END)

TypeSpeedGUI()




