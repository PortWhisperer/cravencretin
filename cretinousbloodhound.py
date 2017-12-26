# from Tkinter import Tk, Label, Button, Text
from Tkinter import *
import subprocess
import sys  #for reading of textfile to place in text widget

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Bloodhound")

        self.label = Label(master, text="Bloodhound")
        self.label.pack()

        self.goog_button = Button(master, text="1 - Open  Google", command=self.openURL_app1)
        self.goog_button.pack()
        master.bind('1', self.openURL_app1)

        self.bing_button = Button(master, text="2 - Open  Bing", command=self.openURL_app2)
        self.bing_button.pack()
        master.bind('2', self.openURL_app2)

        self.fb_button = Button(master, text="3 - Open  Facebook", command=self.openURL_app3)
        self.fb_button.pack()
        master.bind('3', self.openURL_app3)

        self.close_button = Button(master, text="Quit", command=master.quit)
        self.close_button.pack( )

#        #add in frame for display of text
#        configfile = Text(f3, wrap=WORD, width=45, height= 20)
        from Tkinter import *

        root = Tk()
        S = Scrollbar(master)
        T = Text(master, height=4, width=50)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = """HAMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummation
        Devoutly to be wished."""
        T.insert(END, quote)
        mainloop()


    def openURL_app1(self, event=None):                  #open target URL
        print("Launching Google")
        subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "google.com"])

    def openURL_app2(self, event=None):                  #open target URL
        print("Launching Bing")
        subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "bing.com"])

    def openURL_app3(self, event=None):                  #open target URL
        print("Launching Facebook")
        subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "facebook.com"])


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
