words=['Mango','Apple','Grapes','Door','Relation','Parents','Laptop','Television','Mother','Sister','School','college',
       'Air','wATER','BUNK','BLANKET','Pycharm','bedsheet']



def labelslider():
    global count,sliderwords
    text="Welcome to typing speed game"
    if count>=len(text):

        count=0
        sliderwords=''
    sliderwords+=text[count]
    count+=1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(150,labelslider)

def time():
    global timeleft,score,miss
    if(timeleft>=11):
        pass
    else:
        timerlabelcount.configure(fg='red')
    if(timeleft>0):
        timeleft-=1
        timerlabelcount.configure(text=timeleft)
        timerlabelcount.after(1000,time)
    else:
        gameplaydetaillabel.configure(text='Hit= {} | Miss={} | Total score={}'.format(score,miss,score-miss))
        rr=messagebox.askretrycancel('Notification','For playing again hit retry button ')
        if(rr==True):
            score=0
            timeleft=60
            miss=0
            timerlabelcount.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)


from tkinter import *
import random
from tkinter import messagebox
root=Tk()
root.geometry('800x600+400+100')
root.configure(bg='powder blue')
root.title('Typing speed game')

score=0
timeleft=60
count=0
sliderwords=''
miss=0


fontlabel=Label(root,text="",font=('aerial','25','italic bold'),bg='powder blue',fg='red',width=40)
fontlabel.place(x=10,y=10)
labelslider()
random.shuffle(words)

wordlabel=Label(root,text=words[0],font=('aerial','40','italic bold'),bg='powder blue')
wordlabel.place(x=350,y=200)

wordentry=Entry(root,font=('aerial','25','italic bold'),bd=10,justify='center')
wordentry.place(x=250,y=300)
wordentry.focus_set()

scorelabel=Label(root,text='Your Score:',font=('aerial','25','italic bold'),bg='powder blue')
scorelabel.place(x=10,y=100)

scorelabelcount=Label(root,text=score,font=('aerial','25','italic bold'),bg='powder blue',fg='blue')
scorelabelcount.place(x=80,y=180)

timerlabel=Label(root,text='Time left:',font=('aerial','25','italic bold'),bg='powder blue',)
timerlabel.place(x=500,y=100)

timerlabelcount=Label(root,text=timeleft,font=('aerial','25','italic bold'),bg='powder blue',fg='blue')
timerlabelcount.place(x=680,y=100)

gameplaydetaillabel=Label(root,text='Type word and hit Enter button',font=('aerial','30','italic bold'),bg='powder blue',fg='dark grey')
gameplaydetaillabel.place(x=120,y=450)

def startgame(event):
    global score,miss
    if(timeleft==60):
        time()

    gameplaydetaillabel.configure(text='')
    if(wordentry.get()==wordlabel['text']):
        score+=1
        scorelabelcount.configure(text=score)
    else:
        miss+=1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0,END)

root.bind('<Return>',startgame)
root.mainloop()

