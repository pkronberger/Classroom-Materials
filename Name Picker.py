import os
import random
import tkinter as tk



##rawFiles = os.listdir()
##classes = list()
##print(rawFiles)
##for fileName in rawFiles:
##    extension = fileName.split(".")[-1]
##    print (extension)
##    if extension == "txt":
##        classes.append(fileName)
##print (classes)
##
##with open(classes[0], 'r') as f:
##    data = f.read()
##print(data)
##
##names = data.split('\n')
##
##print(names)
##
##def getName():
##    return names[random.randrange(0,len(names))]

#while True:
#    print(getName())
#    input()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.chooseClass()
        
    def chooseClass(self):
        rawFiles = os.listdir()
        self.classes = list()
        #print(rawFiles)
        for fileName in rawFiles:
            extension = fileName.split(".")[-1]
            #print (extension)
            if extension == "txt":
                self.classes.append(fileName)
        #print (self.classes)
        self.listBox = tk.Listbox(self.master, selectmode="SINGLE")
        
        i=0
        for roster in self.classes:
            self.listBox.insert(i, roster)
            i+=1
        self.listBox.activate(1)
        self.listBox.pack()
        self.choose = tk.Button(self)
        self.choose["text"] = "Choose a class\n(click me)"
        self.choose["command"] = self.RandomNames
        self.choose.pack(side="top")

    
    def changeMenu(self):
        self.attend.destroy()
        self.rosterList = tk.Listbox(self.master, selectmode="multiple")
        self.rosterList.pack()
        i = 0
        for name in self.names:
            self.rosterList.insert(i, name)
            i += 1
        self.confirm = tk.Button(self)
        self.confirm["text"] = "Confirm Attendance\nConfirm"
        self.confirm["command"] = self.changeRoster
        self.confirm.pack(side = "top")

    def changeRoster(self):
        self.attend = tk.Button(self)
        self.attend["text"] = "Absent?\n(click me)"
        self.attend["command"] = self.changeMenu
        self.attend.pack()
        self.confirm.destroy()
        present = self.rosterList.curselection()
        self.presentRoster = list()
        for i in range(len(self.names)):
            if i not in present:
                self.presentRoster.append(self.names[i])
                #print(self.names[i])
        self.rosterList.destroy()

    def RandomNames(self):
        self.hi_there = tk.Button(self)
        self.hi_there["font"] = ("Comic Sans MS", 20)
        self.hi_there["text"] = "Generate a name\n(click me)"
        self.attend = tk.Button(self)
        self.attend["text"] = "Absent?\n(click me)"
        course = self.listBox.curselection()
    
        self.listBox.destroy()
        self.choose.destroy()
        with open(self.classes[course[0]], 'r') as f:
            data = f.read()
        #print(data)
        self.names = data.split('\n')
        self.presentRoster = self.names
        #print(self.names)

        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.attend["command"] = self.changeMenu
        self.attend.pack(side = "bottom")



    def getName(self):
        return self.presentRoster[random.randrange(0,len(self.presentRoster))]

    def say_hi(self):
        nm = self.getName()
        #print(nm)
        colors = ["pink", "blue", "teal", "cyan", "green", "purple",
                  "lightcoral", "deeppink", "cornflowerblue", "lightskyblue",
                  "mediumorchid","springgreen","tomato","thistle"]
        self.hi_there.configure(bg = colors[random.randrange(0,len(colors))])
        self.hi_there["text"] = "Generate a name\n" + nm

    

root = tk.Tk()
root.title("Name Generator")
root.attributes("-topmost", True)
app = Application(master=root)
app.mainloop()
