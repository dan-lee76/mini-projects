#This is a comment
import re,itertools
import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
root = tk.Tk()
cov={"J":11,"Q":12,"K":13}
con={0:"C", 1:"D", 2:"S", 3:"H"}
rankd={9:"Straight Flush",8:"Four of a Kind",7:"Full House",6:"Flush",5:"Straight",4:"Three of a kind",3:"Two Pair",2:"Pair",1:"High Card"}
ranky={9:"Large Straight",8:"Four of a Kind",7:"Full House",4:"Three of a kind",1:"Chance",-2:"Yahtzee",-3:"Small Straight"}
print("♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠\n\tWELCOME TO POKER SOLVER 30018\n♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠\n")
print("""
✓1. Straight Flush  | J 10 9 8 7  Same Suit
✓2. Four of a kind  | 5 5 5 5 2
✓3. Full house      | 6 6 6 K K
✓4. Flush           | J 9 8 4 3   Same Suit
✓5. Straight        | 10 J 8 7 6
✓6. Three of a kind | Q Q Q 9 2
✓7. Two Pair        | J J 3 3 2
✓8. One Pair        | 10 10 8 7 4
✓9. High Card       | K Q 7 4 3
""")
def replace(num,rep):
    if num in rep.keys():
        return rep[num]
    else:
        return int(num)
def cardChecker(deck,numList,charList):
    global yahtzee
    sflush,quad,fullhouse,flush,straight,triple,dpair,pair,highcard,paira,five=False,False,False,False,False,False,False,False,False,0,False
    for x in range(14):
        if numList.count(x) == 2:
            paira += 1
            pair = True
        if numList.count(x) == 3:
            triple = True
        if numList.count(x) == 4:
            quad = True
        if numList.count(x) == 5:
            five = True
    if yahtzee == True:
        if len(set(charList)) ==1 and sorted(numList) == list(range(min(numList), max(numList)+1)):
            rank=9
            sflush=True
        elif five == True:
            rank=-2
        elif quad == True:
            rank=8
        elif pair == True and triple == True:
            fullhouse=True
            rank=7
        elif triple == True:
            rank=4
        else:
            highcard=True
            rank = 1
    else:
        if len(set(charList)) ==1 and sorted(numList) == list(range(min(numList), max(numList)+1)):
            rank=9
            sflush=True
        elif five == True:
            rank=-2
        elif quad == True:
            rank=8
        elif pair == True and triple == True:
            fullhouse=True
            rank=7
        elif len(set(charList)) ==1:
            rank=6
            flush=True
        elif sorted(numList) == list(range(min(numList), max(numList)+1)):
            rank=5
            straight=True
        elif triple == True:
            rank=4
        elif paira == 2:
            dpair=True
            rank = 3
        elif pair == True:
            rank=2
        else:
            highcard=True
            rank = 1
    return rank
def cardSelector():
    global d,cards,head,menuFrame,topFrame,cardFrame
    root.geometry("1225x665")
    menuFrame.grid_forget()
    d,cards,count={},[],0
    fname=list(itertools.product(['C','D','S','H'],range(1,14)))
    topFrame=tk.Frame(root)
    cardFrame=tk.Canvas(root)
    head=tk.Label(topFrame, text="Select 5 Cards for Deck One",font=("",24))
    for i in range(4):
        for x in range(13):
            photo=tk.PhotoImage(file="images/png/poker/"+str(fname[count][1])+fname[count][0]+".png")
            d["grid_location_" + str(i) + "_" + str(x)] = tk.Button(cardFrame,image=photo, command=lambda r=i, c=x: boxClicked(r,c),border=1.5,relief="solid",bg="white")
            d["grid_location_" + str(i) + "_" + str(x)].grid(row=i, column=x,pady=1,padx=1)
            d["grid_location_" + str(i) + "_" + str(x)].image = photo
            count+=1
    nxt=tk.Button(topFrame, text="Submit",command=lambda:submit(),font=("", 14),border=1.5,relief="solid",width=50)
    reset=tk.Button(topFrame,text="Reset",command=lambda:refreshPoker(),font=("", 14),border=1.5,relief="solid")
    menu=tk.Button(topFrame,text="Menu",command=lambda:backToMain(),font=("", 14),border=1.5,relief="solid")
    head.grid(row=0,column=1)
    nxt.grid(row=1,column=0,columnspan=4)
    reset.grid(row=0,column=0)
    menu.grid(row=0,column=2)
    topFrame.grid()
    cardFrame.grid()
def refreshPoker():
    global deckOne,deckTwo,cards,firstSet,cardFrame,topFrame
    topFrame.grid_forget()
    cardFrame.grid_forget()
    deckOne,deckTwo,cards,firstSet=[],[],[],True
    cardSelector()
def backToMain():
    global topFrame,cardFrame
    topFrame.grid_forget()
    cardFrame.grid_forget()
    menu()
def refreshYah():
    global deckOne,deckTwo,cards,firstSet,yahFrame,yahBigFrame
    yahFrame.grid_forget()
    yahBigFrame.grid_forget()
    deckOne,deckTwo,cards,firstSet=[],[],[],True
    yahtzeeSelector()
def backToMainYah():
    global deckOne,deckTwo,cards,firstSet,yahFrame,yahBigFrame
    yahFrame.grid_forget()
    yahBigFrame.grid_forget()
    deckOne,deckTwo,cards,firstSet=[],[],[],True
    menu()
def yahtzeeSelector():
    global d,cards,count,q,yahBigFrame,menuFrame,firstSet,head,yahtzee,yahFrame
    menuFrame.grid_forget()
    d,q,count,cards,firstSet,yahtzee={},{},0,[],True,True
    yahFrame=tk.Frame(root)
    yahBigFrame=tk.Frame(yahFrame,width=622)
    yahFrame.grid(row=2)
    yahBigFrame.grid(row=5,columnspan=1000)
    head=tk.Label(yahFrame, text="Select 5 Dice for hand One",font=("",24))
    head.grid(row=1,columnspan=1000)
    reset=tk.Button(yahFrame,text="Reset",command=lambda:refreshYah(),font=("", 14),border=1.5,relief="solid")
    menu=tk.Button(yahFrame,text="Menu",command=lambda:backToMainYah(),font=("", 14),border=1.5,relief="solid")
    reset.grid(row=0,column=0)
    menu.grid(row=0,column=1)
    for x in range(5):
        photo=tk.PhotoImage(file="images/png/yahtzee/"+str(x+1)+".png")
        d["grid_location_" + str(x)] = tk.Button(yahFrame,image=photo, command=lambda c=x, : boxClickedYah(c),border=1.5,relief="solid",bg="white",width=50,height=50)
        d["grid_location_" + str(x)].grid(row=3, column=x,pady=1,padx=1)
        d["grid_location_" + str(x)].image = photo
def boxClickedYah(c):
    global d,cards,firstSet,deckOne,head,count,q,yahBigFrame,count
    if firstSet== True:
        photo=tk.PhotoImage(file="images/default/yahtzee/"+str(c+1)+".png")
        q["grid_location_"+str(count)]=tk.Label(yahBigFrame,image=photo)
        q["grid_location_"+str(count)].grid(row=1,column=count)
        q["grid_location_"+str(count)].image = photo
    else:
        photo=tk.PhotoImage(file="images/default/yahtzee/"+str(c+1)+".png")
        q["grid_location_"+str(count)]=tk.Label(yahBigFrame,image=photo)
        q["grid_location_"+str(count)].grid(row=2,column=count)
        q["grid_location_"+str(count)].image = photo
    cards.append(c+1)
    count+=1
    if count == 5:
        submitYah()
def submit():
    global cards,head,firstSet,deckOne,deckTwo
    if len(cards) != 5:
        head.config(text="5 Cards not Selected")
    else:
        if firstSet==True:
            deckOne=cards
            cards=[]
            firstSet=False
            head.config(text="Select 5 Cards for Deck Two")
        else:
            deckTwo=cards
            convert()
def submitYah():
    global cards,head,firstSet,deckOne,deckTwo,count
    count=0
    if firstSet==True:
        deckOne=cards
        cards=[]
        firstSet=False
        head.config(text="Select 5 Dice to compare")
    else:
        deckTwo=cards
        for x in range(5):
            d["grid_location_" + str(x)].grid_forget()
        convertYah()
def convertYah():
    global deckOne,deckTwo,head,loop,yahtzee
    noHigh,loop,pairN1,pairN2=0,False,[],[]
    num1=[deckOne[x]+1 for x in range(5)]
    num2=[deckTwo[x]+1 for x in range(5)]
    valueOne=cardChecker(deckOne,num1,['D', 'D', 'D', 'D', 'D'])
    valueTwo=cardChecker(deckTwo,num2,['D', 'D', 'D', 'D', 'D'])
    if valueOne > valueTwo:
        t = replace(valueOne,ranky)+" vs "+replace(valueTwo,ranky)+"\nDeck one is better"
        head.config(text=t)
    elif valueTwo > valueOne:
        t = replace(valueOne,ranky)+" vs "+replace(valueTwo,ranky)+"\nDeck two is better"
        head.config(text=t)
    else:
        if valueOne == 9 :
            t = replace(valueOne,ranky)+" vs "+replace(valueTwo,ranky)+"\nIts a draw!"
            head.config(text=t)
        elif valueOne == 8:
            for x in range(14):
                if num1.count(x) == 4:
                    ran1=x
                if num2.count(x) == 4:
                    ran2=x
            outputYah(ran1,ran2,valueOne,valueTwo)
        elif valueOne == 7:
            t = replace(valueOne,rankd)+" vs "+replace(valueTwo,rankd)+"\nIts a draw!"
            head.config(text=t)
        elif valueOne==1:
            ans=outputYah(sum(num1),sum(num2),valueOne,valueTwo)
            if ans == 0:
                ans=outputPoker(pairN1[0],pairN2[0],valueOne,valueTwo)
                if ans == 0:
                    ans=outputPoker((sum(num1)-sum(pairN1*2)),(sum(num2)-sum(pairN2*2)),valueOne,valueTwo)
                    if ans == 0:
                        t = replace(valueOne,rankd)+" vs "+replace(valueTwo,rankd)+"\nIts a draw!"
                        head.config(text=t)
        elif valueOne == -2:
            t = replace(valueOne,ranky)+" vs "+replace(valueTwo,ranky)+"\nIts a draw!"
            head.config(text=t) 
            
        elif valueOne == 4:
            for x in range(14):
                if num1.count(x) == 3:
                    ran1=x
                if num2.count(x) == 3:
                    ran2=x
            outputYah(ran1,ran2,valueOne,valueTwo)
def convert():
 #0C 1D 2S 3H
    global deckOne,deckTwo,head,loop,yahtzee
    noHigh,loop,pairN1,pairN2=0,False,[],[]
    if yahtzee == True:
        num1=[deckOne[x]+1 for x in range(6)]
        num2=[deckTwo[x]+1 for x in range(6)]
        valueOne=cardChecker(deckOne,num1,['D', 'D', 'D', 'D', 'D'])
        valueTwo=cardChecker(deckTwo,num2,['D', 'D', 'D', 'D', 'D'])
    else:
        suit1=[replace(deckOne[x][0],con) for x in range(5)]
        num1=[deckOne[x][1]+1 for x in range(5)]
        valueOne=cardChecker(deckOne,num1,suit1)
        suit2=[replace(deckTwo[x][0],con) for x in range(5)]
        num2=[deckTwo[x][1]+1 for x in range(5)]
        valueTwo=cardChecker(deckTwo,num2,suit2)
    if valueOne > valueTwo:
        t = replace(valueOne,rankd)+" vs "+replace(valueTwo,rankd)+"\nDeck one is better"
        head.config(text=t)
    elif valueOne < valueTwo:
        t = replace(valueOne,rankd)+" vs "+replace(valueTwo,rankd)+"\nDeck two is better"
        head.config(text=t)
    else:
        if valueOne == 9 or valueOne == 5:
            outputPoker(sum(num1),sum(num2),valueOne,valueTwo)
        elif valueOne == 8:
            for x in range(14):
                if num1.count(x) == 4:
                    ran1=x
                if num2.count(x) == 4:
                    ran2=x
            outputPoker(ran1,ran2,valueOne,valueTwo)
        elif valueOne == 7:
            for x in range(14):
                if num1.count(x) == 3:
                    ran1=x
                if num2.count(x) == 3:
                    ran2=x
                if num1.count(x) == 2:
                    ran3=x
                if num2.count(x) == 2:
                    ran4=x
            outputPoker((ran1+ran3),(ran2+ran4),valueOne,valueTwo)
        elif valueOne == 6 or valueOne==1:
            loop = True
            for i in range(6):
                ans=outputPoker(num1[i],num2[i],valueOne,valueTwo)
                if ans == 1:
                    break
                if ans == 0:
                    noHigh += 1
                    if noHigh ==5:
                        t = replace(valueOne,rankd)+" vs "+replace(valueTwo,rankd)+"\nIts a draw!"
                        head.config(text=t)
        elif valueOne == 3:
            loop=True
            for x in range(14):
                if num1.count(x) == 2:
                    pairN1.append(x)
                if num2.count(x) == 2:
                    pairN2.append(x)
            ans=outputPoker(pairN1[1],pairN2[1],valueOne,valueTwo)
            if ans == 0:
                ans=outputPoker(pairN1[0],pairN2[0],valueOne,valueTwo)
                if ans == 0:
                    ans=outputPoker((sum(num1)-sum(pairN1*2)),(sum(num2)-sum(pairN2*2)),valueOne,valueTwo)
                    if ans == 0:
                        t = replace(valueOne,rankd)+" vs "+replace(valueTwo,rankd)+"\nIts a draw!"
                        head.config(text=t)
        elif valueOne == 2:
            for x in range(14):
                if num1.count(x) == 2:
                    ran1=x
                if num2.count(x) == 2:
                    ran2=x
            outputPoker(ran1,ran2,valueOne,valueTwo)  
            
        elif valueOne == 4:
            for x in range(14):
                if num1.count(x) == 3:
                    ran1=x
                if num2.count(x) == 3:
                    ran2=x
            outputPoker(ran1,ran2,valueOne,valueTwo)
def outputPoker(num1,num2,valueOne,valueTwo):
    global head,loop
    if num1 > num2:
        t = replace(valueOne,rankd)+"("+str(num1)+")"+" vs "+replace(valueTwo,rankd)+"("+str(num2)+")"+"\nDeck one is better"
        head.config(text=t)
        return 1
    elif num2 > num1:
        t = replace(valueOne,rankd)+"("+str(num1)+")"+" vs "+replace(valueTwo,rankd)+"("+str(num2)+")"+"\nDeck two is better"
        head.config(text=t)
        return 1
    else:
        if loop == True:
            return 0
        else:
            t = replace(valueOne,rankd)+"("+str(num1)+")"+" vs "+replace(valueTwo,rankd)+"("+str(num2)+")"+"\nIts a draw!"
            head.config(text=t)
def outputYah(num1,num2,valueOne,valueTwo):
    global head,loop
    if num1 > num2:
        t = replace(valueOne,ranky)+"("+str(num1)+")"+" vs "+replace(valueTwo,ranky)+"("+str(num2)+")"+"\nDeck one is better"
        head.config(text=t)
        return 1
    elif num2 > num1:
        t = replace(valueOne,ranky)+"("+str(num1)+")"+" vs "+replace(valueTwo,ranky)+"("+str(num2)+")"+"\nDeck two is better"
        head.config(text=t)
        return 1
    else:
        if loop == True:
            return 0
        else:
            t = replace(valueOne,ranky)+"("+str(num1)+")"+" vs "+replace(valueTwo,ranky)+"("+str(num2)+")"+"\nIts a draw!"
            head.config(text=t)
def boxClicked(r,c):
    global d,cards,firstSet,deckOne,head
    dictKey = "grid_location_" + str(r) + "_" + str(c)
    if firstSet==True:
        if (r,c) in cards:
            d[dictKey].config(bg="white")
            cards.remove((r,c))
        else: 
            d[dictKey].config(bg="blue")
            cards.append((r,c))
    else:
        if (r,c) in deckOne:
            head.config(text="Cards already selected")
        else:
            if (r,c) in cards:
                d[dictKey].config(bg="white")
                cards.remove((r,c))
            else:
                d[dictKey].config(bg="dark green")
                cards.append((r,c))
def menu():
    global yahtzee
    yahtzee = False
    root.geometry("612x408")
    global menuFrame
    menuFrame=tk.Frame(root)
    canvas = tk.Canvas(menuFrame, width = 612, height = 408)            
    img = tk.PhotoImage(file="images/background.png")      
    canvas.create_image(0,0, anchor=NW, image=img)
    canvas.image=img
    startPoker=tk.Button(canvas,text="Solve Poker",font=("", 20),border=1.5,relief="solid",command=lambda:cardSelector())
    startPoker_window = canvas.create_window(380, 204, anchor=NW, window=startPoker)
    startYah=tk.Button(canvas,text="Solve Yahtzee",font=("", 20),border=1.5,relief="solid",command=lambda:yahtzeeSelector())
    startYah_window = canvas.create_window(365, 275, anchor=NW, window=startYah)
    menuFrame.grid()
    canvas.pack()
firstSet=True
root.resizable(width=False, height=False)
root.title("Game Solver")
menu()
root.mainloop()
 
 
