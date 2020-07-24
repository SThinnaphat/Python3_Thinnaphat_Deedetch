from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
from PIL import Image, ImageTk




class Window1:
    def __init__(self,master): #master parameter for the parent widget
        self.master = master
        self.master.title("OnlineHospitalLoginSystem")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelLogin = Label(self.frame, text="Online Hospital Login System", fg="blue",bg="powder blue",
        font=("Tahoma", 20))
        self.LabelLogin.grid(row=0,column=0,columnspan=3,pady=40) #pady คือระยะเว้นจากขอบบน

        self.LoginFrame1 = LabelFrame(self.frame,width=1350,height=600,font=('Tahoma',15,'bold'),relief='ridge',
                                bg='cadet blue',bd=20)
        self.LoginFrame1.grid(row=1,column=0)
        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',
                                bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        #------------------------Label-----------------------------------------------------------

        self.LabelUsername = Label(self.LoginFrame1, text='Username', font=('Tahoma', 15, 'bold'))
        self.LabelUsername.grid(row=0, column=0)
        self.EnterUsername = Entry(self.LoginFrame1, font=('Tahoma', 15, 'bold'),textvariable=self.Username)
        self.EnterUsername.grid(row=0, column=1)

        self.LabelPassword = Label(self.LoginFrame1, text='Password', font=('Tahoma', 15, 'bold'))
        self.LabelPassword.grid(row=1, column=0)
        self.EnterPassword = Entry(self.LoginFrame1, font=('Tahoma', 15, 'bold'),show="*",textvariable=self.Password)
        self.EnterPassword.grid(row=1, column=1)

        #------------------------------------Buttons------------------------------------------------------------------

        self.Login = Button(self.LoginFrame2, text="Login", width=17,command = self.Login_System)
        self.Login.grid(row=3, column=0)
        self.Reset = Button(self.LoginFrame2, text="Reset", width=17,command = self.Reset)
        self.Reset.grid(row=3, column=1)
        self.Exit = Button(self.LoginFrame2, text="Exit", width=17,command = self.Exit)
        self.Exit.grid(row=3, column=2)

        self.canvas = Canvas(self.LoginFrame1,width=200,height=200,bg="cadet blue")
        self.canvas.grid(row=4,column=0)
        self.my_image = PhotoImage(file='C:\\Users\\HP\\PycharmProjects\\untitled1\\hospital.png')
        self.canvas.create_image(105,200,image=self.my_image)


        #--------------------ButtonsFunction----------------------------------------------------------------------
    def Login_System(self):
        u = (self.Username.get())
        p = (self.Password.get())
        if (u == "OnlineMed" and p == str(123456)):
            self.newWindow = Toplevel(self.master)
            self.app = Registration(self.newWindow)

        else:
            tkinter.messagebox.askyesno("Login System", "Invalid Login Detail")
            self.Username.set("")
            self.Password.set("")
            self.EnterUsername.focus()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.EnterUsername.focus()

    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to exit")
        if self.Exit > 0:
            self.master.destroy()
        else:
            command = self.Reset
            return


class Registration:
    def __init__(self,master):
        self.master = master
        self.master.title("Online Hospital Registration System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()

        self.Name = StringVar()
        self.Age = IntVar()
        self.LabelRegis = Label(self.frame, text="Online Hospital Registration System", fg="blue", bg="powder blue",
                                font=("Tahoma", 20))
        self.LabelRegis.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน

        self.RegisFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',
                                      bg='cadet blue', bd=20)
        self.RegisFrame1.grid(row=1, column=0)
        self.RegisFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',
                                      bg='cadet blue', bd=20)
        self.RegisFrame2.grid(row=2, column=0)

        # ------------------------Label-----------------------------------------------------------

        self.LabelName = Label(self.RegisFrame1, text='Name', font=('Tahoma', 15, 'bold'))
        self.LabelName.grid(row=0, column=0)
        self.EnterName = Entry(self.RegisFrame1, font=('Tahoma', 15, 'bold'), textvariable=self.Name)
        self.EnterName.grid(row=0, column=1)

        self.LabelAge = Label(self.RegisFrame1, text='Age', font=('Tahoma', 15, 'bold'))
        self.LabelAge.grid(row=1, column=0)
        self.EnterAge = Entry(self.RegisFrame1, font=('Tahoma', 15, 'bold'), textvariable=self.Age)
        self.EnterAge.grid(row=1, column=1)

        # ------------------------------------Buttons------------------------------------------------------------------

        self.btnSubmit = Button(self.RegisFrame2, text="Submit", width=17,command= self.SymptomsAnalysis_window)
        self.btnSubmit.grid(row=3, column=0)

        self.canvas = Canvas(self.RegisFrame1, width=200, height=200, bg="cadet blue")
        self.canvas.grid(row=4, column=0)
        self.my_image = PhotoImage(file='C:\\Users\\HP\\PycharmProjects\\untitled1\\hospital.png')
        self.canvas.create_image(105, 200, image=self.my_image)

        # --------------------ButtonsFunction----------------------------------------------------------------------
    def SymptomsAnalysis_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = SymptomsAnalysis(self.newWindow)


class SymptomsAnalysis:
    def __init__(self,master):
        self.master = master
        self.master.title("Online Hospital Symptoms Analysis System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()

        self.Symptoms = StringVar()
        self.Congenital = StringVar()
        self.Accident = StringVar()

        self.LabelSymp = Label(self.frame, text="Online Hospital Symptoms Analysis System", fg="blue", bg="powder blue",
                                font=("Tahoma", 20))
        self.LabelSymp.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน

        self.SympFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',
                                      bg='cadet blue', bd=20)
        self.SympFrame1.grid(row=1, column=0)
        self.SympFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',
                                      bg='cadet blue', bd=20)
        self.SympFrame2.grid(row=2, column=0)

        #-----------------------Label---------------------------------------------------------------------------

        self.LabelSymptoms = Label(self.SympFrame1, text='Symptoms', font=('Tahoma', 15, 'bold'))
        self.LabelSymptoms.grid(row=0, column=0)
        self.EnterSymptoms = Entry(self.SympFrame1, font=('Tahoma', 15, 'bold'), textvariable=self.Symptoms)
        self.EnterSymptoms.grid(row=0, column=1)

        self.LabelCongenital = Label(self.SympFrame1, text='Congenital Diseases', font=('Tahoma', 15, 'bold'))
        self.LabelCongenital.grid(row=1, column=0)
        self.EnterCongenital = Entry(self.SympFrame1, font=('Tahoma', 15, 'bold'), textvariable=self.Congenital)
        self.EnterCongenital.grid(row=1, column=1)

        self.LabelAccident = Label(self.SympFrame1, text='Accidental Event (Yes/No)', font=('Tahoma', 15, 'bold'))
        self.LabelAccident.grid(row=2, column=0)
        self.EnterAccident = Entry(self.SympFrame1, font=('Tahoma', 15, 'bold'), textvariable=self.Accident)
        self.EnterAccident.grid(row=2, column=1)


        #------------------------------------------Buttons--------------------------------------------

        self.btnSubmit = Button(self.SympFrame2, text="Submit", width=17, command=self.ChestPainTypes_Window)
        self.btnSubmit.grid(row=3, column=0)

        self.canvas = Canvas(self.SympFrame1, width=200, height=200, bg="cadet blue")
        self.canvas.grid(row=4, column=0)
        self.my_image = PhotoImage(file='C:\\Users\\HP\\PycharmProjects\\untitled1\\hospital.png')
        self.canvas.create_image(105, 200, image=self.my_image)

        # --------------------ButtonsFunction----------------------------------------------------------------------
    def ChestPainTypes_Window(self):
        s = (self.Symptoms.get())
        c = (self.Congenital.get())
        a = (self.Accident.get())
        if (s == 'chest pain' and a == 'no') or (c == 'heart disease'):
            self.newWindow = Toplevel(self.master)
            self.app = ChestPainTypes1(self.newWindow)
        elif (s == 'chest pain' and a == 'yes'):
            self.newWindow = Toplevel(self.master)
            self.app = ChestPainTypes2(self.newWindow)

class ChestPainTypes1:
    def __init__(self,master):

        self.master = master
        self.master.title("Online Hospital Heart Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.LabelChestPainTypes1 = Label(self.frame,text="Click the button that determine your type of chest pain", fg="red",bg="salmon1",font=("Tahoma", 20))
        self.LabelChestPainTypes1.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน
        self.ChestPainTypes1Frame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'),relief='ridge',bg='salmon1', bd=20)
        self.ChestPainTypes1Frame1.grid(row=1, column=0)
        self.ChestPainTypes1Frame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge',bg='salmon1', bd=20)
        self.ChestPainTypes1Frame2.grid(row=2, column=0)
        self.ChestPainTypes1Frame3 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.ChestPainTypes1Frame3.grid(row=3, column=0)

        #---------------------------------------------Buttons-----------------------------------------------------------------------------

        self.ChestDiscomfortPain = Button(self.ChestPainTypes1Frame1, text="1", width=17, command=self.ChestDiscomfort_window)
        self.ChestDiscomfortPain.grid(row=0, column=0)
        self.PinpointChestPain1 = Button(self.ChestPainTypes1Frame2, text="2", width=17, command=self.PinpointChestPain1_window)
        self.PinpointChestPain1.grid(row=0, column=0)
        self.SqueezingChestPain = Button(self.ChestPainTypes1Frame3, text="3", width=17,command=self.SqueezingChestPain_window)
        self.SqueezingChestPain.grid(row=0, column=0)

        #---------------------------------------------Label--------------------------------------------------------------------------------

        self.Label1ChestPainTypes1 = Label(self.ChestPainTypes1Frame1, text='Chest discomfort that gets better with exercise',font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.Label1ChestPainTypes1.grid(row=0, column=2)
        self.Label2ChestPainTypes1 = Label(self.ChestPainTypes1Frame2, text='Pinpoint chest discomfort that worsens with positional changes in breathing.', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.Label2ChestPainTypes1.grid(row=0, column=2)
        self.Label3ChestPainTypes1 = Label(self.ChestPainTypes1Frame3,text='Squeezing, pressure, heaviness, tightness or pain',font=('Tahoma', 15, 'bold'), bg='salmon1')
        self.Label3ChestPainTypes1.grid(row=0, column=2)


    def ChestDiscomfort_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = ChestDiscomfort(self.newWindow)

    def PinpointChestPain1_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = PinpointChestPain1(self.newWindow)

    def SqueezingChestPain_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = SqueezingChestPain(self.newWindow)

class ChestDiscomfort:
    def __init__(self,master):

        self.master = master
        self.master.title("Online Hospital Heart Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.LabelChestDiscomfort = Label(self.frame, text="Online Hospital Heart Center", fg="red", bg="salmon1",font=("Tahoma", 20))
        self.LabelChestDiscomfort.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน
        self.ChestDiscomfortFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',bg='salmon1', bd=20)
        self.ChestDiscomfortFrame1.grid(row=1, column=0)
        self.ChestDiscomfortFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',bg='salmon1', bd=20)
        self.ChestDiscomfortFrame2.grid(row=2, column=0)

        #---------------------------Information------------------------------------------------------------------------

        self.ChestDiscomfort1 = Label(self.ChestDiscomfortFrame1, text='You are having common symptoms of these diseases', font=('Tahoma', 20, 'bold'))
        self.ChestDiscomfort1.grid(row=0, column=0)
        self.ChestDiscomfort2 = Label(self.ChestDiscomfortFrame1, text='- Peptic ulcers', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.ChestDiscomfort2.grid(row=2, column=0)
        self.ChestDiscomfort3 = Label(self.ChestDiscomfortFrame1, text='- Gastroesophageal reflux disease (GERD)', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.ChestDiscomfort3.grid(row=3, column=0)
        self.ChestDiscomfort4 = Label(self.ChestDiscomfortFrame1, text='- Esophageal contraction disorders', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.ChestDiscomfort4.grid(row=4, column=0)
        self.ChestDiscomfort5 = Label(self.ChestDiscomfortFrame1, text='- Esophageal hypersensitivity', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.ChestDiscomfort5.grid(row=5, column=0)
        self.ChestDiscomfort6 = Label(self.ChestDiscomfortFrame1, text='- Hiatal hernia', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.ChestDiscomfort6.grid(row=6, column=0)
        self.ChestDiscomfort7 = Label(self.ChestDiscomfortFrame1, text='We have some screening questions for you to answer', font=('Tahoma', 20, 'bold'))
        self.ChestDiscomfort7.grid(row=8, column=0)

        #--------------------------------------------Buttons------------------------------------------------------------

        self.ChestDiscomfortScreeningCenter = Button(self.ChestDiscomfortFrame2, text="Next", width=17, command=self.ChestDiscomfortScreeningCenter_window)
        self.ChestDiscomfortScreeningCenter.grid(row=3, column=0)

    def ChestDiscomfortScreeningCenter_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = ChestDiscomfortScreeningCenter(self.newWindow)

class ChestDiscomfortScreeningCenter:
        def __init__(self, master):
            self.master = master
            self.master.title("Online Hospital Heart Screening Center System")
            self.master.geometry('1350x750+0+0')
            self.master.config(bg='salmon1')
            self.frame = Frame(self.master, bg='salmon1')
            self.frame.pack()

            self.LabelChestDiscomfortScreening = Label(self.frame,text="make the check sign in the box that determine your symptom(s)",fg="red", bg="salmon1", font=("Tahoma", 20))
            self.LabelChestDiscomfortScreening.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน
            self.ChestDiscomfortScreeningFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
            self.ChestDiscomfortScreeningFrame1.grid(row=1, column=0)
            self.ChestDiscomfortScreeningFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
            self.ChestDiscomfortScreeningFrame2.grid(row=2, column=0)
            self.ChestDiscomfortScreeningFrame3 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
            self.ChestDiscomfortScreeningFrame3.grid(row=3, column=0)

            # -------------------------------CheckBoxes----------------------------------------------------

            var1 = IntVar()
            self.ChestDiscomfortCheck1 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Smoking", variable=var1)
            self.ChestDiscomfortCheck1.grid(row=0, column=0, sticky=W)
            var2 = IntVar()
            self.ChestDiscomfortCheck2 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Drinking too much alcohol", variable=var2)
            self.ChestDiscomfortCheck2.grid(row=0, column=1, sticky=W)
            var3 = IntVar()
            self.ChestDiscomfortCheck3 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Changes in appetite", variable=var3)
            self.ChestDiscomfortCheck3.grid(row=1, column=0, sticky=W)
            var4 = IntVar()
            self.ChestDiscomfortCheck4 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Nausea", variable=var4)
            self.ChestDiscomfortCheck4.grid(row=1, column=1, sticky=W)
            var5 = IntVar()
            self.ChestDiscomfortCheck5 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Bloody or dark stools", variable=var5)
            self.ChestDiscomfortCheck5.grid(row=2, column=0, sticky=W)
            var6 = IntVar()
            self.ChestDiscomfortCheck6 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Unexplained weight loss", variable=var6)
            self.ChestDiscomfortCheck6.grid(row=2, column=1, sticky=W)
            var7 = IntVar()
            self.ChestDiscomfortCheck7 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Indigestion", variable=var7)
            self.ChestDiscomfortCheck7.grid(row=3, column=0, sticky=W)
            var8 = IntVar()
            self.ChestDiscomfortCheck8 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Vomiting", variable=var8)
            self.ChestDiscomfortCheck8.grid(row=3, column=1, sticky=W)
            var9 = IntVar()
            self.ChestDiscomfortCheck9 = Checkbutton(self.ChestDiscomfortScreeningFrame1,text="Retasting your food after eating", variable=var9)
            self.ChestDiscomfortCheck9.grid(row=4, column=0, sticky=W)
            var10 = IntVar()
            self.ChestDiscomfortCheck10 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Difficulty or pain when swallowing",variable=var10)
            self.ChestDiscomfortCheck10.grid(row=4, column=1, sticky=W)
            var11 = IntVar()
            self.ChestDiscomfortCheck11 = Checkbutton(self.ChestDiscomfortScreeningFrame1,text="Inflammation of the gums", variable=var11)
            self.ChestDiscomfortCheck11.grid(row=5, column=0, sticky=W)
            var12 = IntVar()
            self.ChestDiscomfortCheck12 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Laryngitis or hoarseness", variable=var12)
            self.ChestDiscomfortCheck12.grid(row=5, column=1, sticky=W)
            var13 = IntVar()
            self.ChestDiscomfortCheck13 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Chronic sore throat", variable=var13)
            self.ChestDiscomfortCheck13.grid(row=6, column=0, sticky=W)
            var14 = IntVar()
            self.ChestDiscomfortCheck14 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Sudden excess of saliva", variable=var14)
            self.ChestDiscomfortCheck14.grid(row=6, column=1, sticky=W)
            var15 = IntVar()
            self.ChestDiscomfortCheck15 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="Heartburn",variable=var15)
            self.ChestDiscomfortCheck15.grid(row=7, column=0, sticky=W)
            var16 = IntVar()
            self.ChestDiscomfortCheck16 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="A dry cough", variable=var16)
            self.ChestDiscomfortCheck16.grid(row=7, column=1, sticky=W)
            var17 = IntVar()
            self.ChestDiscomfortCheck17 = Checkbutton(self.ChestDiscomfortScreeningFrame1,
                                            text="Bad breath", variable=var17)
            self.ChestDiscomfortCheck17.grid(row=8, column=0, sticky=W)
            var18 = IntVar()
            self.ChestDiscomfortCheck18 = Checkbutton(self.ChestDiscomfortScreeningFrame1, text="The wearing away of your teeth", variable=var18)
            self.ChestDiscomfortCheck18.grid(row=8, column=1, sticky=W)

            #---------------------------------------------------Ending---------------------------------------------------------

            self.ChestDiscomfortScreening1 = Label(self.ChestDiscomfortScreeningFrame2,text='For more accurate diagnosis, please go to the hospital immediately if you found that you have many checked boxes',font=('Tahoma', 15, 'bold'))
            self.ChestDiscomfortScreening1.grid(row=0, column=0)
            self.ChestDiscomfortScreening2 = Label(self.ChestDiscomfortScreeningFrame2,text='We recommend you to capture this screen and show it to your doctor which may be helpful for your doctor',font=('Tahoma', 15, 'bold'))
            self.ChestDiscomfortScreening2.grid(row=2, column=0)
            self.ChestDiscomfortScreening3 = Label(self.ChestDiscomfortScreeningFrame3, text='Thank you for using our program',font=('Tahoma', 15, 'bold'))
            self.ChestDiscomfortScreening3.grid(row=4, column=0)

class PinpointChestPain1:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Hospital Heart Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.LabelPinpointChestPain1 = Label(self.frame, text="Online Hospital Heart Center", fg="red", bg="salmon1",font=("Tahoma", 20))
        self.LabelPinpointChestPain1.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน
        self.PinpointChestPain1Frame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.PinpointChestPain1Frame1.grid(row=1, column=0)
        self.PinpointChestPain1Frame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.PinpointChestPain1Frame2.grid(row=2, column=0)

        # ---------------------------Information------------------------------------------------------------------------

        self.PinpointChestPain11 = Label(self.PinpointChestPain1Frame1,text='You are having common symptoms of these diseases',font=('Tahoma', 20, 'bold'))
        self.PinpointChestPain11.grid(row=0, column=0)
        self.PinpointChestPain12 = Label(self.PinpointChestPain1Frame1, text='- Asthma', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.PinpointChestPain12.grid(row=2, column=0)
        self.PinpointChestPain13 = Label(self.PinpointChestPain1Frame1, text='- Pneumothorax',font=('Tahoma', 15, 'bold'), bg='salmon1')
        self.PinpointChestPain13.grid(row=3, column=0)
        self.PinpointChestPain14 = Label(self.PinpointChestPain1Frame1, text='- Tuberculosis',font=('Tahoma', 15, 'bold'), bg='salmon1')
        self.PinpointChestPain14.grid(row=4, column=0)
        self.PinpointChestPain15 = Label(self.PinpointChestPain1Frame1, text='- Pleurisy',font=('Tahoma', 15, 'bold'), bg='salmon1')
        self.PinpointChestPain15.grid(row=5, column=0)
        self.PinpointChestPain16 = Label(self.PinpointChestPain1Frame1, text='- Pneumonia', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.PinpointChestPain16.grid(row=6, column=0)
        self.PinpointChestPain17 = Label(self.PinpointChestPain1Frame1,text='We have some screening questions for you to answer',font=('Tahoma', 20, 'bold'))
        self.PinpointChestPain17.grid(row=8, column=0)

        # --------------------------------------------Buttons------------------------------------------------------------

        self.PinpointChestPain1ScreeningCenter = Button(self.PinpointChestPain1Frame2, text="Next", width=17,command=self.PinpointChestPain1ScreeningCenter_window)
        self.PinpointChestPain1ScreeningCenter.grid(row=3, column=0)

    def PinpointChestPain1ScreeningCenter_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = PinpointChestPain1ScreeningCenter(self.newWindow)


class PinpointChestPain1ScreeningCenter:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Hospital Heart Screening Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.LabelPinpointChestPain1Screening = Label(self.frame,text="make the check sign in the box that determine your symptom(s)",fg="red", bg="salmon1", font=("Tahoma", 20))
        self.LabelPinpointChestPain1Screening.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน
        self.PinpointChestPain1ScreeningFrame1 = LabelFrame(self.frame, width=1350, height=600,font=('Tahoma', 15, 'bold'), relief='ridge', bg='salmon1',bd=20)
        self.PinpointChestPain1ScreeningFrame1.grid(row=1, column=0)
        self.PinpointChestPain1ScreeningFrame2 = LabelFrame(self.frame, width=1000, height=600,font=('Tahoma', 15, 'bold'), relief='ridge', bg='salmon1',bd=20)
        self.PinpointChestPain1ScreeningFrame2.grid(row=2, column=0)
        self.PinpointChestPain1ScreeningFrame3 = LabelFrame(self.frame, width=1000, height=600,font=('Tahoma', 15, 'bold'), relief='ridge', bg='salmon1',bd=20)
        self.PinpointChestPain1ScreeningFrame3.grid(row=3, column=0)

        # -------------------------------CheckBoxes----------------------------------------------------

        var1 = IntVar()
        self.PinpointChestPain1Check1 = Checkbutton(self.PinpointChestPain1ScreeningFrame1, text="Wheezing", variable=var1)
        self.PinpointChestPain1Check1.grid(row=0, column=0, sticky=W)
        var2 = IntVar()
        self.PinpointChestPain1Check2 = Checkbutton(self.PinpointChestPain1ScreeningFrame1,text="Breathlessness", variable=var2)
        self.PinpointChestPain1Check2.grid(row=0, column=1, sticky=W)
        var3 = IntVar()
        self.PinpointChestPain1Check3 = Checkbutton(self.PinpointChestPain1ScreeningFrame1, text="Coughing",variable=var3)
        self.PinpointChestPain1Check3.grid(row=1, column=0, sticky=W)
        var4 = IntVar()
        self.PinpointChestPain1Check4 = Checkbutton(self.PinpointChestPain1ScreeningFrame1, text="A loss of appetite and weight", variable=var4)
        self.PinpointChestPain1Check4.grid(row=1, column=1, sticky=W)
        var5 = IntVar()
        self.PinpointChestPain1Check5 = Checkbutton(self.PinpointChestPain1ScreeningFrame1, text="A cough that produces phlegm",variable=var5)
        self.PinpointChestPain1Check5.grid(row=2, column=0, sticky=W)
        var6 = IntVar()
        self.PinpointChestPain1Check6 = Checkbutton(self.PinpointChestPain1ScreeningFrame1,text="Abdominal pain", variable=var6)
        self.PinpointChestPain1Check6.grid(row=2, column=1, sticky=W)
        var7 = IntVar()
        self.PinpointChestPain1Check7 = Checkbutton(self.PinpointChestPain1ScreeningFrame1, text="Fever",variable=var7)
        self.PinpointChestPain1Check7.grid(row=3, column=0, sticky=W)
        var8 = IntVar()
        self.PinpointChestPain1Check8 = Checkbutton(self.PinpointChestPain1ScreeningFrame1, text="Joint or bone pain",variable=var8)
        self.PinpointChestPain1Check8.grid(row=3, column=1, sticky=W)
        var9 = IntVar()
        self.PinpointChestPain1Check9 = Checkbutton(self.PinpointChestPain1ScreeningFrame1,text="A persistent headache", variable=var9)
        self.PinpointChestPain1Check9.grid(row=4, column=0, sticky=W)
        var10 = IntVar()
        self.PinpointChestPain1Check10 = Checkbutton(self.PinpointChestPain1ScreeningFrame1,text="Shortness of breath, or rapid, shallow breathing", variable=var10)
        self.PinpointChestPain1Check10.grid(row=4, column=1, sticky=W)
        var11 = IntVar()
        self.PinpointChestPain1Check11 = Checkbutton(self.PinpointChestPain1ScreeningFrame1,text="Unexplained weight loss", variable=var11)
        self.PinpointChestPain1Check11.grid(row=5, column=0, sticky=W)
        var12 = IntVar()
        self.PinpointChestPain1Check12 = Checkbutton(self.PinpointChestPain1ScreeningFrame1,text="Muscle aches", variable=var12)
        self.PinpointChestPain1Check12.grid(row=5, column=1, sticky=W)
        var13 = IntVar()
        self.PinpointChestPain1Check13 = Checkbutton(self.PinpointChestPain1ScreeningFrame1, text="Shaking chills",variable=var13)
        self.PinpointChestPain1Check13.grid(row=6, column=0, sticky=W)
        var14 = IntVar()
        self.PinpointChestPain1Check14 = Checkbutton(self.PinpointChestPain1ScreeningFrame1,text="Diarrhea", variable=var14)
        self.PinpointChestPain1Check14.grid(row=6, column=1, sticky=W)
        var15 = IntVar()
        self.PinpointChestPain1Check15 = Checkbutton(self.PinpointChestPain1ScreeningFrame1, text="Sweating",variable=var15)
        self.PinpointChestPain1Check15.grid(row=7, column=0, sticky=W)
        var16 = IntVar()
        self.PinpointChestPain1Check16 = Checkbutton(self.PinpointChestPain1ScreeningFrame1, text="Dusky or purplish skin color, or cyanosis",variable=var16)
        self.PinpointChestPain1Check16.grid(row=7, column=1, sticky=W)

        # ---------------------------------------------------Ending---------------------------------------------------------

        self.PinpointChestPain1Screening1 = Label(self.PinpointChestPain1ScreeningFrame2,text='For more accurate diagnosis, please go to the hospital immediately if you found that you have many checked boxes',font=('Tahoma', 15, 'bold'))
        self.PinpointChestPain1Screening1.grid(row=0, column=0)
        self.PinpointChestPain1Screening2 = Label(self.PinpointChestPain1ScreeningFrame2,text='We recommend you to capture this screen and show it to your doctor which may be helpful for your doctor',font=('Tahoma', 15, 'bold'))
        self.PinpointChestPain1Screening2.grid(row=2, column=0)
        self.PinpointChestPain1Screening3 = Label(self.PinpointChestPain1ScreeningFrame3,text='Thank you for using our program', font=('Tahoma', 15, 'bold'))
        self.PinpointChestPain1Screening3.grid(row=4, column=0)


class SqueezingChestPain:
    def __init__(self,master):

        self.master = master
        self.master.title("Online Hospital Heart Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.LabelHeart = Label(self.frame, text="Online Hospital Heart Center", fg="red", bg="salmon1",
                               font=("Tahoma", 20))
        self.LabelHeart.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน
        self.HeartFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',bg='salmon1', bd=20)
        self.HeartFrame1.grid(row=1, column=0)
        self.HeartFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',bg='salmon1', bd=20)
        self.HeartFrame2.grid(row=2, column=0)

        #---------------------------Information------------------------------------------------------------------------

        self.Heart1 = Label(self.HeartFrame1, text='You are having common symptoms of these diseases', font=('Tahoma', 20, 'bold'))
        self.Heart1.grid(row=0, column=0)
        self.Heart2 = Label(self.HeartFrame1, text='- Coronary Heart Disease', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.Heart2.grid(row=2, column=0)
        self.Heart3 = Label(self.HeartFrame1, text='- Heart Arrhythmia', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.Heart3.grid(row=3, column=0)
        self.Heart4 = Label(self.HeartFrame1, text='- Heart Valve Disease', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.Heart4.grid(row=4, column=0)
        self.Heart5 = Label(self.HeartFrame1, text='- Cardiomyopathy', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.Heart5.grid(row=5, column=0)
        self.Heart6 = Label(self.HeartFrame1, text='- Pericardial Effusion', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.Heart6.grid(row=6, column=0)
        self.Heart7 = Label(self.HeartFrame1, text='We have some screening questions for you to answer', font=('Tahoma', 20, 'bold'))
        self.Heart7.grid(row=8, column=0)

        #--------------------------------------------Buttons------------------------------------------------------------

        self.HeartScreeningCenter = Button(self.HeartFrame2, text="Next", width=17, command=self.HeartScreeningCenter_window)
        self.HeartScreeningCenter.grid(row=3, column=0)

    def HeartScreeningCenter_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = HeartScreeningCenter(self.newWindow)



class HeartScreeningCenter:
    def __init__(self,master):

        self.master = master
        self.master.title("Online Hospital Heart Screening Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.LabelHeartScreening = Label(self.frame, text="make the check sign in the box that determine your symptom(s)", fg="red", bg="salmon1",font=("Tahoma", 20))
        self.LabelHeartScreening.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน
        self.HeartScreeningFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',bg='salmon1', bd=20)
        self.HeartScreeningFrame1.grid(row=1, column=0)
        self.HeartScreeningFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'), relief='ridge',bg='salmon1', bd=20)
        self.HeartScreeningFrame2.grid(row=2, column=0)
        self.HeartScreeningFrame3 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge',bg='salmon1', bd=20)
        self.HeartScreeningFrame3.grid(row=3, column=0)


        #-------------------------------CheckBoxes----------------------------------------------------

        var1 = IntVar()
        self.HeartCheck1 = Checkbutton(self.HeartScreeningFrame1, text="High Blood Pressure", variable=var1)
        self.HeartCheck1.grid(row=0,column = 0, sticky=W)
        var2 = IntVar()
        self.HeartCheck2 = Checkbutton(self.HeartScreeningFrame1, text="High Blood Cholesterol", variable=var2)
        self.HeartCheck2.grid(row=0,column = 1, sticky=W)
        var3 = IntVar()
        self.HeartCheck3 = Checkbutton(self.HeartScreeningFrame1, text="Obesity", variable=var3)
        self.HeartCheck3.grid(row=1,column=0, sticky=W)
        var4 = IntVar()
        self.HeartCheck4 = Checkbutton(self.HeartScreeningFrame1, text="Diabetes", variable=var4)
        self.HeartCheck4.grid(row=1,column=1, sticky=W)
        var5 = IntVar()
        self.HeartCheck5 = Checkbutton(self.HeartScreeningFrame1, text="Chronic kidney disease", variable=var5)
        self.HeartCheck5.grid(row=2,column=0,sticky=W)
        var6 = IntVar()
        self.HeartCheck6 = Checkbutton(self.HeartScreeningFrame1, text="HIV/AIDS", variable=var6)
        self.HeartCheck6.grid(row=2,column=1, sticky=W)
        var7 = IntVar()
        self.HeartCheck7 = Checkbutton(self.HeartScreeningFrame1, text="Metabolic Syndrome", variable=var7)
        self.HeartCheck7.grid(row=3,column=0, sticky=W)
        var8 = IntVar()
        self.HeartCheck8 = Checkbutton(self.HeartScreeningFrame1, text="Sleep disorders", variable=var8)
        self.HeartCheck8.grid(row=3,column=1, sticky=W)
        var9 = IntVar()
        self.HeartCheck9 = Checkbutton(self.HeartScreeningFrame1, text="Work on the night shift which affect your sleep", variable=var9)
        self.HeartCheck9.grid(row=4,column=0 ,sticky=W)
        var10 = IntVar()
        self.HeartCheck10 = Checkbutton(self.HeartScreeningFrame1, text="Work more than 55 hours a week", variable=var10)
        self.HeartCheck10.grid(row=4,column=1, sticky=W)
        var11 = IntVar()
        self.HeartCheck11 = Checkbutton(self.HeartScreeningFrame1, text="Family historical record of having a heart disease", variable=var11)
        self.HeartCheck11.grid(row=5,column=0, sticky=W)
        var12 = IntVar()
        self.HeartCheck12 = Checkbutton(self.HeartScreeningFrame1, text="Cold sweats", variable=var12)
        self.HeartCheck12.grid(row=5,column=1, sticky=W)
        var13 = IntVar()
        self.HeartCheck13 = Checkbutton(self.HeartScreeningFrame1, text="Dizziness", variable=var13)
        self.HeartCheck13.grid(row=6,column=0, sticky=W)
        var14 = IntVar()
        self.HeartCheck14 = Checkbutton(self.HeartScreeningFrame1, text="Light-headedness", variable=var14)
        self.HeartCheck14.grid(row=6,column=1, sticky=W)
        var15 = IntVar()
        self.HeartCheck15 = Checkbutton(self.HeartScreeningFrame1, text="Nausea or a feeling of indigestion", variable=var15)
        self.HeartCheck15.grid(row=7,column=0, sticky=W)
        var16 = IntVar()
        self.HeartCheck16 = Checkbutton(self.HeartScreeningFrame1, text="neck pain", variable=var16)
        self.HeartCheck16.grid(row=7,column=1, sticky=W)
        var17 = IntVar()
        self.HeartCheck17 = Checkbutton(self.HeartScreeningFrame1, text="Shortness of breath, especially with activity", variable=var17)
        self.HeartCheck17.grid(row=8,column=0, sticky=W)
        var18 = IntVar()
        self.HeartCheck18 = Checkbutton(self.HeartScreeningFrame1, text="weakness", variable=var18)
        self.HeartCheck18.grid(row=8,column=1,sticky=W)

        self.HeartScreening1 = Label(self.HeartScreeningFrame2, text='For more accurate diagnosis, please go to the hospital immediately if you found that you have many checked boxes',font=('Tahoma', 15, 'bold'))
        self.HeartScreening1.grid(row=0, column=0)
        self.HeartScreening2 = Label(self.HeartScreeningFrame2,text='We recommend you to capture this screen and show it to your doctor which may be helpful for your doctor',font=('Tahoma', 15, 'bold'))
        self.HeartScreening2.grid(row=2, column=0)
        self.HeartScreening3 = Label(self.HeartScreeningFrame3,text='Thank you for using our program',font=('Tahoma', 15, 'bold'))
        self.HeartScreening3.grid(row=0, column=0)

class ChestPainTypes2:
    def __init__(self,master):

        self.master = master
        self.master.title("Online Hospital Heart Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.LabelChestPainTypes2 = Label(self.frame,text="Click the button that determine your type of chest pain", fg="red",bg="salmon1",font=("Tahoma", 20))
        self.LabelChestPainTypes2.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน
        self.ChestPainTypes2Frame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'),relief='ridge',bg='salmon1', bd=20)
        self.ChestPainTypes2Frame1.grid(row=1, column=0)
        self.ChestPainTypes2Frame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge',bg='salmon1', bd=20)
        self.ChestPainTypes2Frame2.grid(row=2, column=0)

        #---------------------------------------------Buttons-----------------------------------------------------------------------------

        self.LightningChestPain = Button(self.ChestPainTypes2Frame1, text="1", width=17, command=self.LightningChestPain_window)
        self.LightningChestPain.grid(row=0, column=0)
        self.PinpointChestPain = Button(self.ChestPainTypes2Frame2, text="2", width=17, command=self.PinpointChestPain2_window)
        self.PinpointChestPain.grid(row=0, column=1)

        #---------------------------------------------Label--------------------------------------------------------------------------------

        self.Label1ChestPainTypes2 = Label(self.ChestPainTypes2Frame1, text='Momentary chest discomfort, often characterized as a lightning bolt or electrical shock.',font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.Label1ChestPainTypes2.grid(row=0, column=2)
        self.Label2ChestPainTypes2 = Label(self.ChestPainTypes2Frame2, text='Pinpoint chest discomfort that worsens with positional changes in breathing.', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.Label2ChestPainTypes2.grid(row=0, column=2)

    def LightningChestPain_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = LightningChestPain(self.newWindow)

    def PinpointChestPain2_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = PinpointChestPain2(self.newWindow)

class LightningChestPain:
    def __init__(self,master):

        self.master = master
        self.master.title("Online Hospital Heart Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.LightningChestPainFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.LightningChestPainFrame1.grid(row=1, column=0)
        self.LightningChestPainFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.LightningChestPainFrame2.grid(row=2, column=0)

 # ---------------------------Information-----------------------------------------------------------------------------------

        self.LightningChestPain = Label(self.LightningChestPainFrame1, text='You are having common symptoms of these diseases',font=('Tahoma', 20, 'bold'))
        self.LightningChestPain.grid(row=0, column=0)
        self.LightningChestPain2 = Label(self.LightningChestPainFrame1, text='- Muscle strain', font=('Tahoma', 15, 'bold'),bg='salmon1')
        self.LightningChestPain2.grid(row=2, column=0)
        self.LightningChestPain3 = Label(self.LightningChestPainFrame1, text='- Injured ribs', font=('Tahoma', 15, 'bold'), bg='salmon1')
        self.LightningChestPain3.grid(row=3, column=0)
        self.LightningChestPain4 = Label(self.LightningChestPainFrame1, text='- Costochondritis', font=('Tahoma', 15, 'bold'), bg='salmon1')
        self.LightningChestPain4.grid(row=4, column=0)
        self.LightningChestPain5 = Label(self.LightningChestPainFrame1, text='We have some screening questions for you to answer',font=('Tahoma', 20, 'bold'))
        self.LightningChestPain5.grid(row=6, column=0)

        # --------------------------------------------Buttons------------------------------------------------------------

        self.LightningChestPainScreeningCenter = Button(self.LightningChestPainFrame2, text="Next", width=17,command=self.LightningChestPainScreeningCenter_window)
        self.LightningChestPainScreeningCenter.grid(row=3, column=0)

    def LightningChestPainScreeningCenter_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = LightningChestPainScreeningCenter(self.newWindow)

class LightningChestPainScreeningCenter:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Hospital Heart Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.LabelLightningChestPainScreening = Label(self.frame,text="make the check sign in the box that determine your symptom(s)", fg="red",bg="salmon1", font=("Tahoma", 20))
        self.LabelLightningChestPainScreening.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน
        self.LightningChestPainScreeningFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.LightningChestPainScreeningFrame1.grid(row=1, column=0)
        self.LightningChestPainScreeningFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.LightningChestPainScreeningFrame2.grid(row=2, column=0)
        self.LightningChestPainScreeningFrame3 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.LightningChestPainScreeningFrame3.grid(row=3, column=0)

        # -------------------------------CheckBoxes----------------------------------------------------

        var1 = IntVar()
        self.LightningChestPainCheck1 = Checkbutton(self.LightningChestPainScreeningFrame1, text="sharp upper back and rib pain", variable=var1)
        self.LightningChestPainCheck1.grid(row=0, column=0, sticky=W)
        var2 = IntVar()
        self.LightningChestPainCheck2 = Checkbutton(self.LightningChestPainScreeningFrame1, text="severe and sudden pain, particularly if caused by a blow to the chest or back", variable=var2)
        self.LightningChestPainCheck2.grid(row=0, column=1, sticky=W)
        var3 = IntVar()
        self.LightningChestPainCheck3 = Checkbutton(self.LightningChestPainScreeningFrame1, text="gradual worsening pain after repetitive movement, such as rowing, swimming, or other physical exercises", variable=var3)
        self.LightningChestPainCheck3.grid(row=1, column=0, sticky=W)
        var4 = IntVar()
        self.LightningChestPainCheck4 = Checkbutton(self.LightningChestPainScreeningFrame1, text="stiffness and tension in muscles, causing upper back pain", variable=var4)
        self.LightningChestPainCheck4.grid(row=1, column=1, sticky=W)
        var5 = IntVar()
        self.LightningChestPainCheck5 = Checkbutton(self.LightningChestPainScreeningFrame1, text="muscle rigidity when bending or twisting the upper body", variable=var5)
        self.LightningChestPainCheck5.grid(row=2, column=0, sticky=W)
        var6 = IntVar()
        self.LightningChestPainCheck6 = Checkbutton(self.LightningChestPainScreeningFrame1, text="worsening pain when coughing, sneezing, or breathing in deeply", variable=var6)
        self.LightningChestPainCheck6.grid(row=2, column=1, sticky=W)
        var7 = IntVar()
        self.LightningChestPainCheck7 = Checkbutton(self.LightningChestPainScreeningFrame1, text="spasms of the intercostal muscles", variable=var7)
        self.LightningChestPainCheck7.grid(row=3, column=0, sticky=W)
        var8 = IntVar()
        self.LightningChestPainCheck8 = Checkbutton(self.LightningChestPainScreeningFrame1, text="tenderness in the area between the ribs", variable=var8)
        self.LightningChestPainCheck8.grid(row=3, column=1, sticky=W)
        var9 = IntVar()
        self.LightningChestPainCheck9 = Checkbutton(self.LightningChestPainScreeningFrame1,text="feeling breathless", variable=var9)
        self.LightningChestPainCheck9.grid(row=4, column=0, sticky=W)
        var10 = IntVar()
        self.LightningChestPainCheck10 = Checkbutton(self.LightningChestPainScreeningFrame1, text="a protrusion or a sharp stabbing sensation in the rib area",variable=var10)
        self.LightningChestPainCheck10.grid(row=4, column=1, sticky=W)
        var11 = IntVar()
        self.LightningChestPainCheck11 = Checkbutton(self.LightningChestPainScreeningFrame1,text="an area around the ribs that is extremely tender to touch",variable=var11)
        self.LightningChestPainCheck11.grid(row=4, column=1, sticky=W)

        self.HeartScreening1 = Label(self.LightningChestPainScreeningFrame2,text='For more accurate diagnosis, please go to the hospital immediately if you found that you have many checked boxes',font=('Tahoma', 15, 'bold'))
        self.HeartScreening1.grid(row=0, column=0)
        self.HeartScreening2 = Label(self.LightningChestPainScreeningFrame2,text='We recommend you to capture this screen and show it to your doctor which may be helpful for your doctor',font=('Tahoma', 15, 'bold'))
        self.HeartScreening2.grid(row=2, column=0)
        self.HeartScreening3 = Label(self.LightningChestPainScreeningFrame3, text='Thank you for using our program',font=('Tahoma', 15, 'bold'))
        self.HeartScreening3.grid(row=0, column=0)

class PinpointChestPain2:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Hospital Heart Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.PinpointChestPain2Frame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.PinpointChestPain2Frame1.grid(row=1, column=0)
        self.PinpointChestPain2Frame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.PinpointChestPain2Frame2.grid(row=2, column=0)

        # ---------------------------Information-----------------------------------------------------------------------------------

        self.PinpointChestPain2 = Label(self.PinpointChestPain2Frame1,text='You are having common symptoms of these diseases',font=('Tahoma', 20, 'bold'))
        self.PinpointChestPain2.grid(row=0, column=0)
        self.PinpointChestPain22 = Label(self.PinpointChestPain2Frame1, text='- Traumatic pneumothorax',font=('Tahoma', 15, 'bold'), bg='salmon1')
        self.PinpointChestPain22.grid(row=2, column=0)
        self.PinpointChestPain23 = Label(self.PinpointChestPain2Frame1, text='- Pulmonary contusion',font=('Tahoma', 15, 'bold'), bg='salmon1')
        self.PinpointChestPain23.grid(row=3, column=0)
        self.PinpointChestPain24 = Label(self.PinpointChestPain2Frame1, text='- Costochondritis',font=('Tahoma', 15, 'bold'), bg='salmon1')
        self.PinpointChestPain24.grid(row=4, column=0)
        self.PinpointChestPain25 = Label(self.PinpointChestPain2Frame1,text='We have some screening questions for you to answer',font=('Tahoma', 20, 'bold'))
        self.PinpointChestPain25.grid(row=6, column=0)

        # --------------------------------------------Buttons------------------------------------------------------------

        self.PinpointChestPain2ScreeningCenter = Button(self.PinpointChestPain2Frame2, text="Next", width=17,command=self.PinpointChestPain2ScreeningCenter_window)
        self.PinpointChestPain2ScreeningCenter.grid(row=3, column=0)

    def PinpointChestPain2ScreeningCenter_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = PinpointChestPain2ScreeningCenter(self.newWindow)

class PinpointChestPain2ScreeningCenter:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Hospital Heart Center System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='salmon1')
        self.frame = Frame(self.master, bg='salmon1')
        self.frame.pack()

        self.PinpointChestPain2Screening = Label(self.frame,text="make the check sign in the box that determine your symptom(s)", fg="red",bg="salmon1", font=("Tahoma", 20))
        self.PinpointChestPain2Screening.grid(row=0, column=0, columnspan=3, pady=40)  # pady คือระยะเว้นจากขอบบน
        self.PinpointChestPain2ScreeningFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.PinpointChestPain2ScreeningFrame1.grid(row=1, column=0)
        self.PinpointChestPain2ScreeningFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.PinpointChestPain2ScreeningFrame2.grid(row=2, column=0)
        self.PinpointChestPain2ScreeningFrame3 = LabelFrame(self.frame, width=1000, height=600, font=('Tahoma', 15, 'bold'),relief='ridge', bg='salmon1', bd=20)
        self.PinpointChestPain2ScreeningFrame3.grid(row=3, column=0)

        # -------------------------------CheckBoxes----------------------------------------------------

        var1 = IntVar()
        self.PinpointChestPain2Check1 = Checkbutton(self.PinpointChestPain2ScreeningFrame1, text="shortness of breath", variable=var1)
        self.PinpointChestPain2Check1.grid(row=0, column=0, sticky=W)
        var2 = IntVar()
        self.PinpointChestPain2Check2 = Checkbutton(self.PinpointChestPain2ScreeningFrame1, text="Chest pain, which may be more severe on one side of the chest", variable=var2)
        self.PinpointChestPain2Check2.grid(row=0, column=1, sticky=W)
        var3 = IntVar()
        self.PinpointChestPain2Check3 = Checkbutton(self.PinpointChestPain2ScreeningFrame1, text="Sharp pain when inhaling", variable=var3)
        self.PinpointChestPain2Check3.grid(row=1, column=0, sticky=W)
        var4 = IntVar()
        self.PinpointChestPain2Check4 = Checkbutton(self.PinpointChestPain2ScreeningFrame1, text="Pressure in the chest that gets worse over time", variable=var4)
        self.PinpointChestPain2Check4.grid(row=1, column=1, sticky=W)
        var5 = IntVar()
        self.PinpointChestPain2Check5 = Checkbutton(self.PinpointChestPain2ScreeningFrame1, text="Blue discoloration of the skin or lips", variable=var5)
        self.PinpointChestPain2Check5.grid(row=2, column=0, sticky=W)
        var6 = IntVar()
        self.PinpointChestPain2Check6 = Checkbutton(self.PinpointChestPain2ScreeningFrame1, text="Rapid breathing", variable=var6)
        self.PinpointChestPain2Check6.grid(row=2, column=1, sticky=W)
        var7 = IntVar()
        self.PinpointChestPain2Check7 = Checkbutton(self.PinpointChestPain2ScreeningFrame1, text="Confusion or dizziness", variable=var7)
        self.PinpointChestPain2Check7.grid(row=3, column=0, sticky=W)
        var8 = IntVar()
        self.PinpointChestPain2Check8 = Checkbutton(self.PinpointChestPain2ScreeningFrame1, text="Wheezing and coughing", variable=var8)
        self.PinpointChestPain2Check8.grid(row=3, column=1, sticky=W)
        var9 = IntVar()
        self.PinpointChestPain2Check9 = Checkbutton(self.PinpointChestPain2ScreeningFrame1,text=" Coughing up blood or bloody sputum ", variable=var9)
        self.PinpointChestPain2Check9.grid(row=4, column=0, sticky=W)
        var10 = IntVar()
        self.PinpointChestPain2Check10 = Checkbutton(self.PinpointChestPain2ScreeningFrame1, text="Painful breathing or difficulty breathing",variable=var10)
        self.PinpointChestPain2Check10.grid(row=4, column=1, sticky=W)


        self.PinpointChestPain2Screening1 = Label(self.PinpointChestPain2ScreeningFrame2,text='For more accurate diagnosis, please go to the hospital immediately if you found that you have many checked boxes',font=('Tahoma', 15, 'bold'))
        self.PinpointChestPain2Screening1.grid(row=0, column=0)
        self.PinpointChestPain2Screening2 = Label(self.PinpointChestPain2ScreeningFrame2,text='We recommend you to capture this screen and show it to your doctor which may be helpful for your doctor',font=('Tahoma', 15, 'bold'))
        self.PinpointChestPain2Screening2.grid(row=2, column=0)
        self.PinpointChestPain2Screening3 = Label(self.PinpointChestPain2ScreeningFrame3, text='Thank you for using our program',font=('Tahoma', 15, 'bold'))
        self.PinpointChestPain2Screening3.grid(row=0, column=0)

if __name__ == '__main__':
    root = Tk()
    app = Window1(root)
    root.mainloop()

#----------------------------------Developed by Thinnaphat Deedetch---------------------------------------------------------------------------------------------------------------------


