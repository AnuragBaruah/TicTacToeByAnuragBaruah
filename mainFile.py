#creating the screen
from tkinter import *
from Fncs import *

gridValue = {'A1':'', 'A2':'', 'A3':'', 'B1':'', 'B2':'', 'B3':'', 'C1':'', 'C2':'', 'C3':''}
allPossible = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
moveSeq = []

screen = Tk()
screen.geometry('500x500')
screen.title('TIC TAC TOE BY BHS')
canvas = Canvas(screen, width = 500, height = 500)
canvas.pack()

hl = PhotoImage(file = 'hBar.gif')#picture of a horizontal line
vl = PhotoImage(file = 'vBar.gif')#pic of vertical line
X = PhotoImage(file = 'X.gif')#pic of X
O = PhotoImage(file = 'O.gif')#pic of O
B = PhotoImage(file = 'butn.gif')#blank picture (this will be the face value of the buttons)
cpic = PhotoImage(file = 'Computer.gif')
ppic = PhotoImage(file = 'Player.gif')
dpic = PhotoImage(file = 'Draw.gif')
qpic = PhotoImage(file = 'quitImage.gif')
npic = PhotoImage(file = 'newGameImage.gif')

Pics(cpic, ppic, dpic, qpic, npic, O)
NewGame(screen, canvas, hl, vl,B, X, gridValue, moveSeq)
screen.mainloop()
















