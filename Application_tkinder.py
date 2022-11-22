
import tkinter
from tkinter import *



proba = "98%"
predit = 0

if predit==1:
    commentaire = "vous avez un risque de décéder"
else:
    commentaire = "vous avez des chances d'être secouru"



#SCREEN
tuto = tkinter.Tk()
tuto.geometry("700x250")
tuto.title("Chance de survie")

x=95
#Label
l3 = Label(text="Notre application estime votre probabilité de décès à : ", font="Arial")
l3.place(x=10,y=100)

l3 = Label(text=proba, font="Arial")
l3.place(x=400,y=100)




l1 = Label(text=" En cas de problèmes, selon notre application :", font="Arial")
l1.place(x=10,y=50)

l2 = Label(text=commentaire, font="Arial")
l2.place(x=400,y=50)


#lOOP
tuto.mainloop()
