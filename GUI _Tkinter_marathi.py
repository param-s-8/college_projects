from tkinter import *

mWindow=Tk() #creating main window
mWindow.title("MARATHI KEYBOARD")
mWindow.resizable(0,0) #for restircting full screen usage.
                        #comment down that line of code, for full screen

def select(value):
    length=len(entry.get())
    if (value=='Erase'):
        entry.delete(length-1,length)
        length=length-1
    elif value=='Space':
        entry.insert(length,' ')
    else:
        entry.insert(length,value)

#widget creation
l1=Label(mWindow,text='MARATHI INPUT:',bg='black',fg='white').grid(row=2,column=0)
entry=Entry(mWindow,width=138,bd=6)
entry.grid(row=2,column=1,columnspan=13,sticky=E)
msg=Label(mWindow,text='<Welcome To Marathi Keyboard>',bg='black',fg='white').grid(row=0,column=6)


        
buttons=['(',')','१','२','३','४','५','६','७','८','९','0','Erase',
         'अ','आ','इ','ई','उ','ऊ','ए','ऐ','ओ','औ','ँ','ः',':',
         'ब','ह','ग','द','ज','ड','प','र','क','त','च','ट','न',
         'व','म','ल','स','य','भ','Space','घ','ध','झ','ढ','फ','ख',
         'थ','छ','ठ','ण','ळ','श','|','?','ौ','ै','ी','ा','ू',
         'ो','े','्','ि','ु','ं','ृ','ॉ','़','ँ',',',"'",'"']

#below code, for creating all the buttons
varRow=3
varColumn=2
for button in buttons:
    Button(mWindow,text=button,width=6,height=2,relief='raised',
           command=lambda x=button:select(x),bd=6).grid(row=varRow,column=varColumn)

    varColumn+=1
    if(varColumn>14 and varRow==3):
        varColumn=2
        varRow+=1
    if(varColumn>14 and varRow==4):
        varColumn=2
        varRow+=1
    if(varColumn>14 and varRow==5):
        varColumn=2
        varRow+=1
    if(varColumn>14 and varRow==6):
        varColumn=2
        varRow+=1
    if(varColumn>14 and varRow==7):
        varColumn=2
        varRow+=1


mWindow.mainloop() #for infinite loop of main window

