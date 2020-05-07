from tkinter import *
from tkinter import messagebox

from Matrix import Matrix
from Vector import Vector
from Solver import Solver

root = Tk()
root.geometry("700x500")

root.title('System of linear equations solver')

# Max number of variables
maxSize = 7

n = 3

def changeSize():
    global n
    n = int(sizeBox.get())

    for i in range(maxSize):
        labelsEq[i].grid_forget()
        freeCoefs[i].grid_forget()
        for j in range(maxSize):
            labelsValue[i][j].grid_forget()
            coefs[i][j].grid_forget()
            if j != maxSize - 1:
                labelsSign[i][j].grid_forget() 

    for i in range(n):
        for j in range(n):
            coefs[i][j].grid(row=i, column=3*j)
            labelsValue[i][j].grid(row=i, column=3*j+1)
            if j != n - 1:
                labelsSign[i][j].grid(row=i, column=3*j+2)
            else:
                labelsEq[i].grid(row=i, column=3*j+2)

        
    for i in range(n):
        freeCoefs[i].grid(row=i, column=3*n)

headFrame = Frame(root)
centerFrame = Frame(root)
bottomFrame = Frame(root)

Label(headFrame, text='Number of variables: ')\
    .grid(row=0, column=0, columnspan=5, padx=(20), pady=(0,10), sticky=N+S)

sizeBox = Spinbox(headFrame, command=changeSize,
    textvariable=IntVar(value=3), width=4, from_=1, to=maxSize)
n = int(sizeBox.get())
sizeBox.grid(row=0, column=5, pady=(0,10), sticky=N+S)

coefs = [[Entry(centerFrame, width=4, textvariable=DoubleVar(value=0)) \
    for i in range(maxSize)] for j in range(maxSize)]

freeCoefs = [Entry(centerFrame, width=4, textvariable=DoubleVar(value=0)) \
    for i in range(maxSize)]

labelsValue = [[Label(centerFrame, text=" * x" + str(j+1)) \
    for j in range(maxSize)] for i in range(maxSize)]
labelsSign = [[Label(centerFrame, text=" + ") \
    for j in range(maxSize - 1)] for i in range(maxSize)]
labelsEq = [Label(centerFrame, text=" = ") \
    for i in range(maxSize)]

changeSize()

def solve(event):
    global n
    m = Matrix(n)
    for i in range(n):
        for j in range(n):
            m.matrix[i][j] = float(coefs[i][j].get())

    v = Vector(n)
    for i in range(n):
        v.vec[i] = float(freeCoefs[i].get())

    s = Solver(m, v)

    try:
        print(s.solve())
    except ValueError as e:
        messagebox.showwarning("Warning", str(e))

solveButton = Button(headFrame, text="Solve")
solveButton.grid(row=0, column=6, pady=(0, 10), padx=(30, 0), sticky=N+S)
solveButton.bind('<Button-1>', solve)

headFrame.place(anchor="c", relx=.5, rely=.3)
centerFrame.place(anchor="c", relx=.5, rely=.5)
bottomFrame.place(anchor="c", relx=.5, rely=.8)
root.mainloop()