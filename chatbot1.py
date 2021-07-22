from tkinter import *

root=Tk()

def send():
    send="You : "+a.get()
    text.insert(END,"\n"+send)
    if(a.get()=='hi'):
        text.insert(END,"\n"+"Bot : hello")
    elif(a.get()=='hello'):
        text.insert(END,"\n"+"Bot: hi")
    elif(a.get()=='how are you'):
        text.insert(END,"\n"+"Bot: i am fine...and you sir")
    elif(a.get()=='i am fine'):
        text.insert(END,"\n"+"Bot: thats good sir...")
    elif(a.get()=='whats your name'):
        text.insert(END,"\n"+"Bot: i am a bot & your name sir")
    elif(a.get()=='my name is nikunj'):
        text.insert(END,"\n"+"Bot: so sweet name sir")
    elif(a.get()=='nice to meet you'):
        text.insert(END,"\n"+"Bot: thank you sir")
    elif(a.get()=='by dear bot'):
        text.insert(END,"\n"+"Bot: byy sir")
    else:
        text.insert(END,"\n"+"Bot: I did't get it sir")


text = Text(root,bg='white')
text.grid(row=0,column=0,columnspan=2)
a=Entry(root,width=80)
bsend=Button(root,text='Send',bg='green',width=20,command=send)
bsend.grid(row=1,column=1)
a.grid(row=1,column=0)
root.title('Simple ChatBot')
root.mainloop()