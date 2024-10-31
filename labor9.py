from tkinter import *

def belepes():
    pass


app = Tk()
app.title("Dolgozoi nyilvantartas")

menulista = Menu(app)

fajl = Menu(menulista)
fajl.add_command(label="belepes", command=belepes)

egyeb = Menu(menulista)

app.config(menu=menulista)
app.mainloop()