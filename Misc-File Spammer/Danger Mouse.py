import uuid
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
root = Tk()
root.title("The File Spammer")
root.geometry("300x300")
root.resizable(False, False)
setloc=["N:\\Desktop\\", "N:\\Documents\\", "N:\\documents\\My Pictures\\", "N:\\documents\\My Music\\", ""]
spamloc = ""
ci = 0
random = True
def radioChanged():
    global random
    opt = v.get()
    if opt == 0:
        random= True
        lname.grid_remove()
        ename.grid_remove()
    elif opt == 1:
        random= False
        lname.grid()
        ename.grid()
def comboChanged():
    global spamloc, setloc
    loc = location.get()
    if loc == "Custom":
        spamloc = askdirectory()
        location.set(spamloc + "")
    elif loc == "Desktop":
        spamloc=setloc[0]
    elif loc == "Documents":
        spamloc=setloc[1]
    elif loc == "Pictures":
        spamloc=setloc[2]
    elif loc == "Music":
        spamloc=setloc[3]
    elif loc == "Default":
        spamloc=setloc[4]
def start():
    global random
    amount= int(eamount.get())+1 
    for i in range(1,int(amount)):
        if random == True:
            unique_filename = str(uuid.uuid4())
        elif random == False:
            unique_filename = str(ename.get())+str(i)
        f= open(spamloc+unique_filename+(efile.get()),"w+")
        bar(i, amount)
def bar(i, amount):
    if pbar["value"] >= 100:
        pass
    else:
        pbar["value"] = (i/(amount-1))*100
        interfaceFrame.update_idletasks()
v = IntVar()
v.set(0)
interfaceFrame=Frame(root)
interfaceFrame.pack()
lwelcome=Label(interfaceFrame, text="The File Spammer\n\n", font=("Courier", 14))
lwelcome.grid(row=0, column=0,columnspan=2)
lcred=Label(interfaceFrame, text="A Dan Lee© Creation", font=("Calibre", 8))
lcred.grid(row=11, column=0,columnspan=2)
lprog=Label(interfaceFrame, text="Progress:", font=("Calibre", 11))
lprog.grid(row=9, column=0,columnspan=2)
lamount=Label(interfaceFrame, text="Amount: ")
lamount.grid(row=2, column=0, sticky="w")
eamount=Entry(interfaceFrame, bd=2, width=25)
eamount.grid(row=2, column=1)
lfile=Label(interfaceFrame, text="File Type: ")
lfile.grid(row=3, column=0, pady=10, sticky="w")
efile=Entry(interfaceFrame, bd=2, width=25)
efile.grid(row=3, column=1)
llocation=Label(interfaceFrame, text="Location:")
llocation.grid(row=4, column=0, sticky="w")
location=ttk.Combobox(interfaceFrame, values=["Default", "Desktop", "Documents", "Photos", "Music", "Custom"], width=22)
location.set("Default")
location.grid(row=4, column=1)
lname=Label(interfaceFrame, text="File Name: ")
lname.grid(row=5, column=1)
ename=Entry(interfaceFrame, bd=2, width=20)
ename.grid(row=6, column=1)
lname.grid_remove()
ename.grid_remove()
eselect1=Radiobutton(interfaceFrame,text = "Random", variable = v, value = 0, command = radioChanged)
eselect2=Radiobutton(interfaceFrame,text = "Name", variable = v, value =1, command = radioChanged)
eselect1.grid(row=5,column=0, sticky="w")
eselect2.grid(row=6,column=0, sticky="w")
b1=Button(interfaceFrame, command=lambda: start(), bd=5, text="Enter", width=10)
b1.grid(row=8, column=0, columnspan=2)
pbar = ttk.Progressbar(interfaceFrame, orient = "horizontal", length = 300, mode = "determinate") 
pbar.grid(row=10, column=0,columnspan=2)
location.bind("<<ComboboxSelected>>",lambda event:comboChanged())
root.mainloop()
