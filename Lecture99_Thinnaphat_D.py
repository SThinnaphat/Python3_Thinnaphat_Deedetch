from tkinter import *
import math

def CalculateData(event):
    print(float(textbox2.get())/math.pow(float(textbox.get())/100,2))
    labelShowValue.configure(text = (float(textbox2.get())/math.pow(float(textbox.get())/100,2)))
    if (float(textbox2.get())/math.pow(float(textbox.get())/100,2)) >= 30 :
        labelShowResult.configure(text = "Obese")
    elif (float(textbox2.get())/math.pow(float(textbox.get())/100,2)) > 25 and (float(textbox2.get())/math.pow(float(textbox.get())/100,2)) < 30 :
        labelShowResult.configure(text = "Fat")
    elif (float(textbox2.get())/math.pow(float(textbox.get())/100,2)) > 23 and (float(textbox2.get())/math.pow(float(textbox.get())/100,2)) < 25 :
        labelShowResult.configure(text = "Overweight")
    elif (float(textbox2.get())/math.pow(float(textbox.get())/100,2)) > 18.6 and (float(textbox2.get())/math.pow(float(textbox.get())/100,2)) < 23 :
        labelShowResult.configure(text = "NormalWeight")
    elif (float(textbox2.get())/math.pow(float(textbox.get())/100,2)) < 18.5 :
        labelShowResult.configure(text = "UnderWeight")


mainWindow = Tk()
labelIntro = Label(mainWindow,text = "BMI Calculation",fg = "blue",font = ("Tahoma",20))
labelIntro.grid(row=0,column=0)
labelHeight = Label(mainWindow,text = "height",font = ("Tahoma",14))
labelHeight.grid(row=1,column=0)
textbox = Entry(mainWindow)
textbox.grid(row=1,column=1)
labelHeightUnit = Label(mainWindow,text = "cm",font = ("Tahoma",14))
labelHeightUnit.grid(row=1,column=4)
labelWeight = Label(mainWindow,text = "weight(kg)",font = ("Tahoma",14))
labelWeight.grid(row=2,column=0)
textbox2 = Entry(mainWindow)
textbox2.grid(row=2,column=1)
labelWeightUnit = Label(mainWindow,text = "kg",font = ("Tahoma",14))
labelWeightUnit.grid(row=2,column=4)
CalculateButton = Button(mainWindow,text="Calculate",bg = "light blue",fg = "white",font = ("Tahoma",14))
CalculateButton.bind('<Button-1>',CalculateData)
CalculateButton.grid(row=3,column=1)
labelValue = Label(mainWindow,text = "Value",font = ("Tahoma",14))
labelValue.grid(row=4,column=0)
labelShowValue = Label(mainWindow,text = "-",font = ("Tahoma",14))
labelShowValue.grid(row=4,column=1)
labelResult = Label(mainWindow,text = "Result",font = ("Tahoma",14))
labelResult.grid(row=5,column=0)
labelShowResult = Label(mainWindow,text = "-",font = ("Tahoma",14))
labelShowResult.grid(row=5,column=1)

mainWindow.mainloop()