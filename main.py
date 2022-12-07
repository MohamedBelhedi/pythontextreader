import pyttsx3
from tkinter import *
from PyPDF2 import PdfReader



####setUP pyttsx3#######
engine = pyttsx3.init()
# eine while True oder for ... schleife Text len === text len stop 
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-70)

#####end#######

def read():
    reader = PdfReader("sample.pdf")
    page = reader.pages[0]
    print(page.extract_text())
    # engine.say("hallo ich bin mimuk von pipi kakaland habe pipi gemacht,das wetter ist sehr schön ich gehe gleich zu schule habe pipi kacka gemacht in pipikakaland")
    engine.say(page.extract_text())
    engine.runAndWait()
######setUP TK###############

root=Tk()

root.geometry("400x400")
button1=Button(text="read",command=read)
button1.pack(side="bottom")


#######end#####################


root.mainloop()