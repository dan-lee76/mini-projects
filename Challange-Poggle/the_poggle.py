##                                                                                                               bbbbbbbb                                  
##PPPPPPPPPPPPPPPPP                                                          lllllll                             b::::::b                                  
##P::::::::::::::::P                                                         l:::::l                             b::::::b                                  
##P::::::PPPPPP:::::P                                                        l:::::l                             b::::::b                                  
##PP:::::P     P:::::P                                                       l:::::l                              b:::::b                                  
##  P::::P     P:::::P  ooooooooooo      ggggggggg   ggggg   ggggggggg   gggggl::::l     eeeeeeeeeeee             b:::::bbbbbbbbb yyyyyyy           yyyyyyy
##  P::::P     P:::::Poo:::::::::::oo   g:::::::::ggg::::g  g:::::::::ggg::::gl::::l   ee::::::::::::ee           b::::::::::::::bby:::::y         y:::::y 
##  P::::PPPPPP:::::Po:::::::::::::::o g:::::::::::::::::g g:::::::::::::::::gl::::l  e::::::eeeee:::::ee         b::::::::::::::::by:::::y       y:::::y  
##  P:::::::::::::PP o:::::ooooo:::::og::::::ggggg::::::ggg::::::ggggg::::::ggl::::l e::::::e     e:::::e         b:::::bbbbb:::::::by:::::y     y:::::y   
##  P::::PPPPPPPPP   o::::o     o::::og:::::g     g:::::g g:::::g     g:::::g l::::l e:::::::eeeee::::::e         b:::::b    b::::::b y:::::y   y:::::y    
##  P::::P           o::::o     o::::og:::::g     g:::::g g:::::g     g:::::g l::::l e:::::::::::::::::e          b:::::b     b:::::b  y:::::y y:::::y     
##  P::::P           o::::o     o::::og:::::g     g:::::g g:::::g     g:::::g l::::l e::::::eeeeeeeeeee           b:::::b     b:::::b   y:::::y:::::y      
##  P::::P           o::::o     o::::og::::::g    g:::::g g::::::g    g:::::g l::::l e:::::::e                    b:::::b     b:::::b    y:::::::::y       
##PP::::::PP         o:::::ooooo:::::og:::::::ggggg:::::g g:::::::ggggg:::::gl::::::le::::::::e                   b:::::bbbbbb::::::b     y:::::::y        
##P::::::::P         o:::::::::::::::o g::::::::::::::::g  g::::::::::::::::gl::::::l e::::::::eeeeeeee   ......  b::::::::::::::::b       y:::::y         
##P::::::::P          oo:::::::::::oo   gg::::::::::::::g   gg::::::::::::::gl::::::l  ee:::::::::::::e   .::::.  b:::::::::::::::b       y:::::y          
##PPPPPPPPPP            ooooooooooo       gggggggg::::::g     gggggggg::::::gllllllll    eeeeeeeeeeeeee   ......  bbbbbbbbbbbbbbbb       y:::::y           
##                                                g:::::g             g:::::g                                                           y:::::y            
##                                    gggggg      g:::::g gggggg      g:::::g                                                          y:::::y             
##                                    g:::::gg   gg:::::g g:::::gg   gg:::::g                                                         y:::::y              
##                                     g::::::ggg:::::::g  g::::::ggg:::::::g                                                        y:::::y               
##                                      gg:::::::::::::g    gg:::::::::::::g                                                        yyyyyyy                
##                                        ggg::::::ggg        ggg::::::ggg                                                                                 
##                                           gggggg              gggggg                                                                                    
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import random,urllib.request,os,threading
class Timer(tk.Tk):#Thanks Stackoverflow
    def __init__(self):
        self.label=tk.Label(rinfoFrame, text="", font=("Arial Black", 18))
        self.label.grid(row=0,column=0)
        self.remaining=0
        self.countdown(180)
        
    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= 0:
            self.label.configure(text="STOP")
            checker()
        else:
            self.label.configure(text="Time Remaining:\n %d seconds" % self.remaining)
            self.remaining = self.remaining - 1
            root.after(1000, self.countdown)

def menu():
    global menFrame, htpFrame,gameFrame
    htpFrame.pack_forget()
    gameFrame.pack_forget()
    title=tk.Label(menFrame, text="Poggle.by", font=("Arial Black", 86))
    play=tk.Button(menFrame, text="Play", font=("Arial ", 24), relief="solid", borderwidth=4, command=lambda: game() )
    htpBtn=tk.Button(menFrame, text="How To Play", font=("Arial ", 24), relief="solid", borderwidth=4, command=lambda: howToPlay() )
    mulBtn=tk.Button(menFrame, text="LAN Mode", font=("Arial ", 24), relief="solid", borderwidth=4, command=lambda: multiName() )
    wcred=tk.Label(menFrame, text="\nA Dan Lee© Creation", font=("Calibre", 8))
    title.grid(row=0,column=0)
    play.grid(row=1,column=0)
    htpBtn.grid(row=2,pady=10)
    mulBtn.grid(row=3)
    wcred.grid(row=100)
    menFrame.pack()
def howToPlay():
    global menFrame, htpFrame
    menFrame.pack_forget()
    htpTitle=tk.Label(htpFrame, text="How to Play:", font=("Arial Black", 28))
    htp=tk.Label(htpFrame, text="Create English words longer than 3 charachters using the grid\nThe Letters must be connecting to one another(adjacent and diagonal)\nScore points by having long words\nYou get 3 minutes\n\nYou can use 'Return' to submit answers and 'Backspace' to clear the", font=("Arial", 16))
    menBtn=tk.Button(htpFrame, text="Menu", font=("Arial ", 24), relief="solid", borderwidth=4, command=lambda: menu())
    htpTitle.grid(row=2)
    htp.grid(row=3)
    menBtn.grid(row=0,column=0)
    htpFrame.pack()
def multiName():
    global menFrame, mnFrame,fLabel
    menFrame.pack_forget()
    fTitle=tk.Label(mnFrame, text="Username", font=("Arial Black", 32))
    fLabel=tk.Entry(mnFrame,relief="solid", bg="#f0f0ed",borderwidth=4,font=("Arial ", 12))
    fSubmit=tk.Button(mnFrame,text="Submit",font=("Arial ", 18),relief="solid", borderwidth=4,command=lambda:multiSelect())
    fTitle.grid(row=0)
    fLabel.grid(row=1,pady=10)
    fSubmit.grid(row=2)
    mnFrame.pack()
def multiSelect():
    global mnFrame, msFrame, username,fLabel
    username=fLabel.get()
    mnFrame.pack_forget()
    mTitle=tk.Label(msFrame, text="Multiplayer", font=("Arial Black", 28))
    mhBtn=tk.Button(msFrame, text="Host", font=("Arial ", 24), relief="solid", borderwidth=4, command=lambda: multiHost())
    mjBtn=tk.Button(msFrame, text="Join", font=("Arial ", 24), relief="solid", borderwidth=4, command=lambda: multiJoin())
    mTitle.grid(row=0,columnspan=2)
    mhBtn.grid(row=1,column=0)
    mjBtn.grid(row=1,column=1)
    msFrame.pack()

#                                           ###################
#                                           #   Game Section  #
#                                           ###################
def game():
    global menFrame, sW_Display, cW_Display, cW_Display, rinfoFrame, gameFrame, linfoFrame,multiplayer,boggleLetter,multiWords
    menFrame.pack_forget()
    mhFrame.pack_forget()
    mjFrame.pack_forget()
    gridFrame=tk.Frame(gameFrame,bg="#f0f0ed")
    rinfoFrame=tk.Frame(gameFrame,bg="#f0f0ed")
    binfoFrame=tk.Frame(gameFrame,bg="#f0f0ed")
    
    #Grid
    c=0
    for i in range(4):#Generates grid area
        for x in range(4):
            if multiplayer != True:
                a=random.choice(boggleLetter)
                letter=random.choice(random.choice(a))#Randomly chooses a letter from 2d array
                d["grid_location_" + str(i) + "_" + str(x)] = tk.Button(gridFrame, relief="solid", text=letter, font=("", 20), bg="#f0f0ed", border=1.5, command=lambda r=i, c=x, l=letter: boxClicked(r,c,l) )
                d["grid_location_" + str(i) + "_" + str(x)].grid(row=i, column=x,pady=5,padx=5)
                d["grid_location_" + str(i) + "_" + str(x)].config(width=5, height=2)
                boggleLetter.remove(a)
            else:
                letter=multiWords[c]
                d["grid_location_" + str(i) + "_" + str(x)] = tk.Button(gridFrame, relief="solid", text=letter, font=("", 20), bg="#f0f0ed", border=1.5, command=lambda r=i, c=x, l=letter: boxClicked(r,c,l) )
                d["grid_location_" + str(i) + "_" + str(x)].grid(row=i, column=x,pady=5,padx=5)
                d["grid_location_" + str(i) + "_" + str(x)].config(width=5, height=2)
                c +=1
            
    #RInfo
            
    cWord=tk.Label(rinfoFrame, text="Current Word",font=("Arial Black", 20))
    cW_Display=tk.Label(rinfoFrame, text="",font=("Arial", 16))
    sWord=tk.Label(rinfoFrame, text="Submitted Words",font=("Arial Black", 20))
    sW_Display=ScrolledText(rinfoFrame,relief="solid",state="disabled",bg="#f0f0ed",width=15,height=10,wrap=tk.WORD, borderwidth=0, font=("Arial", 14))
    cWord.grid(row=1)
    cW_Display.grid(row=2)
    sWord.grid(row=3,column=0)
    sW_Display.grid(row=4)
    sW_Display.grid_propagate(False)
    
    #BInfo
            
    menuBtn=tk.Button(binfoFrame, text="End Game", font=("Arial ", 12), relief="solid", borderwidth=4, command=lambda: checker())
    submitBtn=tk.Button(binfoFrame, text="Submit",font=("Arial ", 12), relief="solid", borderwidth=4, command=lambda: wordSubmit())
    clearBtn=tk.Button(binfoFrame, text="Clear",font=("Arial ", 12), relief="solid", borderwidth=4, command=lambda: clear())
    submitBtn.grid(row=1,column=0,padx=3)
    clearBtn.grid(row=1,column=2,padx=3)
    menuBtn.grid(row=1,column=3,padx=3)
    
    #Frame Placement
    
    gameFrame.pack()
    rinfoFrame.grid(row=0,column=1)
    binfoFrame.grid(row=1,column=0)
    gridFrame.grid(row=0,column=0)
    
    #Binding
    
    root.bind("<Return>",wordSubmit)
    root.bind("<BackSpace>",clear)
    Timer()
def boxClicked(r,c,l):
    global currentWord, cW_Display, firstLetter,pPosRow,pPosCol
    dictKey = "grid_location_" + str(r) + "_" + str(c)
    if firstLetter == True:
        d[dictKey].config(disabledforeground="#FFFFFF", bg="#FF0000", state="disabled")
        currentWord.append(l)
        pPosRow,pPosCol=r,c
        firstLetter = False
    else:
        if (r+1 == pPosRow or r-1 == pPosRow or r == pPosRow) and (c+1 == pPosCol or c-1 == pPosCol or c == pPosCol):
            d[dictKey].config(disabledforeground="#FFFFFF", bg="#FF0000", state="disabled")
            currentWord.append(l)
            pPosRow,pPosCol=r,c
        else:
            d[dictKey].config(disabledforeground="#FFFFFF", bg="#f0f0ed", state="normal")
    #print(pPosRow,pPosCol)    
    cW_Display.config(text=currentWord)
def wordSubmit(event=None):
    global currentWord, sW_Display, cW_Display, firstLetter
    firstLetter = True
    if len(currentWord) <3:
        cW_Display.config(text="Too Short")
    elif "".join(currentWord) in wordList:
        cW_Display.config(text="Already in list")
    else:
        wordList.append("".join(currentWord))
        wDisplay=wordList[::-1]
        sW_Display.config(state="normal")
        sW_Display.delete("1.0",tk.END)#Removes everything from the box
        for i in wDisplay:#Adds the list to the box, makes it scrollable
            sW_Display.insert(tk.END,i+"\n")
        sW_Display.config(state="disabled")
    clear()
    #print(wordList)
def clear(event=None):
    global currentWord, firstLetter
    firstLetter=True
    for i in range(4):
            for x in range(4):
                d["grid_location_" + str(i) + "_" + str(x)].config(bg="#f0f0ed", state="normal")
    currentWord=[]
def checker():
    global score, correctWords,words
    score = 0
    correctWords=[wordList[i] for i in range(len(wordList)) if wordList[i].lower() in words]
    score=sum([+len(correctWords[i])for i in range(len(correctWords))])
    gameOver()
def gameOver():
    global gameFrame, score, correctWords, overFrame, words, multiplayer,username,fopen,threads
    gameFrame.pack_forget()
    overFrame=tk.Frame(root)
    gOver=tk.Label(overFrame, text="Game Over",font=("Arial Black", 52)).pack()
    gScoreTitle=tk.Label(overFrame, text="Your Score",font=("Arial", 36)).pack()
    gScore=tk.Label(overFrame, text=score ,font=("Arial Black", 32)).pack()
    cWords=tk.Label(overFrame, text=correctWords ,font=("Arial Black", 12)).pack()
    rButton=tk.Button(overFrame, text="Restart", font=("Arial Black", 24), relief="solid", borderwidth=5, command=lambda: reset()).pack()
    overFrame.pack()
    if multiplayer == True:
        fopen.write(str("USER_DONE,"+username+","+str(score)+"\n"))
        t = threading.Thread(target=multiGameover)
        threads.append(t)
        t.start()


#                                           ###################
#                                           #    Multiplayer  #
#                                           ###################
def multiHost():#Menu For host
    global msFrame, mhFrame, fLabel, stop,fSubmit
    stop = False
    msFrame.pack_forget()
    fTitle=tk.Label(mhFrame,text="Game Name", font=("Arial Black", 28))
    fLabel=tk.Entry(mhFrame,relief="solid", bg="#f0f0ed",borderwidth=4,font=("Arial ", 12))
    fSubmit=tk.Button(mhFrame,text="Submit",relief="solid", bg="#f0f0ed",borderwidth=4,font=("Arial ", 18),command=lambda:mHCreation())
    mhFrame.pack()
    fTitle.grid(row=0)
    fLabel.grid(row=1,pady=10)
    fSubmit.grid(row=2)
def multiJoin():#Menu for joining
    global msFrame, mjFrame,avagames
    msFrame.pack_forget()
    avagameList=[]
    avagames=tk.Listbox(mjFrame,relief="solid", bg="#f0f0ed",borderwidth=4,font=("Arial ", 12))
    avagames.bind("<<ListboxSelect>>", onselect)
    for file in os.listdir("./"):
        if file.endswith(".by"):
            filename=os.path.join(file[:-3])
            print(filename)
            avagameList.append(filename)
            avagames.insert(tk.END,filename)
    avagames.grid(row=0)
    mjFrame.pack()
def onselect(evt):
    global avagames, mjFrame, threads,fopen,wait,stop
    avagames.grid_forget()
    w,stop = evt.widget,0
    value = w.get(int(w.curselection()[0]))#Gets the value of the selected game | int(bit) gets the index location
    fopen=open(value+".by", "a+")
    fopen.write("PLAYER_WAITING\n")
    wait=tk.Label(mjFrame, text="Waiting...", font=("Arial Black", 86))
    wait.grid(row=2)
    t = threading.Thread(target=mJConnectionEngine)
    threads.append(t)
    t.start()
def mJConnectionEngine():
    global fopen,wait,stop,multiWords,multiplayer
    while stop != True:
        content=fopen.read().splitlines()
        for i in range(len(content)):
            if content[i] == "GAME_START":
                wamount="Starting"
                wait.configure(text=wamount)
                root.update()
                lines=[line for line in content]
                multiWords=list(lines[0])
                print(multiWords)
                print(multiWords[2])
                multiplayer,stop = True,True
                game()
def mHCreation():
    global fLabel, mhFrame,stop,fopen,waiting,fopen,threads,fSubmit
    fSubmit.grid_forget()
    fname,c,stop = fLabel.get(),0,False
    fopen=open(fname+".by", "w+")#Needs to be a+ so it generates new file
    waiting=tk.Label(mhFrame, text="0 Waiting", font=("Arial ", 24))
    ready=tk.Button(mhFrame, text="Ready", font=("Arial ", 24), relief="solid", borderwidth=4, command=lambda:mHgameStart())
    waiting.grid(row=2)
    ready.grid(row=3)
    root.update()
    t = threading.Thread(target=mHCreationEngine)
    threads.append(t)
    t.start()
def mHCreationEngine():
    global fLabel, mhFrame,stop,fopen,waiting
    c=0
    while stop != True:
        content=fopen.read().splitlines()
        for i in range(len(content)):
            if content[i] == "PLAYER_WAITING":
                c+=1
                wamount=c,"Waiting"
                waiting.config(text=wamount)
                root.update()
        #root.after(3500)
def mHgameStart():
    global multiplayer,fopen, boggleLetters,multiWords,stop
    print("Yes")
    multiplayer,stop = True,True
    multiWords=[random.choice(random.choice(random.choice(boggleLetter))) for i in range(16)]
    fopen.write(str("".join(multiWords))+"\n")
    fopen.write("GAME_START\n")
    game()
def multiGameover():
    global overFrame,fopen,score,gameover
    highscore = score
    pWon=tk.Label(overFrame,text="You" ,font=("Arial Black", 12))
    pWon.pack()
    while gameover != True:
        content=fopen.read().splitlines()
        for i in range(len(content)):
            cUser=content[i].split(",")
            if cUser[0] == "USER_DONE":
                if int(cUser[2]) > highscore:
                    winner=cUser[1]+" | "+cUser[2]
                    pWon.config(text=winner)
                root.update()

#                                           ######################
#                                           #   Utility Section  #
#                                           ######################
def reset():
    global overFrame, gameover
    gameover = True
    overFrame.pack_forget()
    boot()
def loader():
    global words
    loadFrame=tk.Frame(root)
    lTitle=tk.Label(loadFrame, text="Poggle.by", font=("Arial Black", 86)).pack()
    loadFrame.pack()
    root.update()
    wurl="https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response=urllib.request.urlopen(wurl)
    longtxt = response.read().decode().lower()
    words= longtxt.splitlines()
    loadFrame.pack_forget()
    boot()
def boot():
    global boggleLetter,wordList,currentWord,correctWords,d,pPosRow,pPosCol,firstLetter,htpFrame,menFrame,gameFrame,msFrame,mhFrame,mjFrame,multiplayer,threads,mnFrame,gameover,stop
    boggleLetter=[["A","A","E","E","G","N"],["E","L","R","T","T","Y"],["A","O","O","T","T","W"],["A","B","B","J","O","O"],["E","H","R","T","V","W"],["C","I","M","O","T","U"],["D","I","S","T","T","Y"],["E","I","O","S","S","T"],["D","E","L","R","V","Y"],["A","C","H","O","P","S"],["H","I","M","N","Q","U"],["E","E","I","N","S","U"],["E","E","G","H","N","W"],["A","F","F","K","P","S"],["H","L","N","N","R","Z"],["D","E","I","L","R","X"]]
    wordList,currentWord,correctWords,threads=[],[],[],[]
    d={}
    pPosRow,pPosCol,multiplayer,stop,gameover = 0,0,False,False,False
    firstLetter=True
    htpFrame=tk.Frame(root)
    menFrame=tk.Frame(root)
    msFrame=tk.Frame(root)
    mnFrame=tk.Frame(root)
    mhFrame=tk.Frame(root)
    mjFrame=tk.Frame(root)
    gameFrame=tk.Frame(root,bg="#f0f0ed")
    menu()
#                                         #########################
#                                         #   Initialise Section  #
#                                         #########################
root=tk.Tk()
root.title("Poggle.by")
root.geometry("675x450")
root.resizable(width=False, height=False)
loader()
root.mainloop()

