from tkinter import*
from googletrans import Translator

win=Tk()
win.title('Translator')
win.geometry('600x120')


def translator():
    snt_ce=entry.get()
    lang=var.get()
    translator = Translator()
    translation = translator.translate(snt_ce, dest=lang)
    label2= Label(win,text=f'Translated text: {translation.text}',font=('arial' ,12,'bold'))
    label2.grid(row=1,column=1,pady=10)
    

label=Label(win,text='ENTer here to translate: ',font=('arial' ,10,'bold'))
label.grid(row=0,column=0)
entry=Entry(win,width=40)
entry.grid(row=0,column=1)
var=StringVar(win)
var.set('choose')
dropdown=OptionMenu(win,var,'SPANISH','ENGLISH','HINDI','ARABIC','FRENCH','ITALIAN','PUNJABI','GERMAN','ROMANIA','NEPALI','TELUGU','SINDHI','MAORI','BENGALI','JAPANESE')
dropdown.grid(padx=5,row=0,column=2)
button=Button(win,text='Translate',command=translator)
button.grid(pady=5,row=1,column=0)

win.mainloop()
