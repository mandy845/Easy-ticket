from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
root = Tk()
root.title("Easy Ticket")
root.geometry('500x500')


class Tickets:
#Initializing  window
    myresult = StringVar()
    def __init__(self, window):

        self.lblnumber =Label (window, text="Enter CellNumber:")
        self.lblnumber.place(x=50,y=50)
        self.txtcellno= Entry(window)
        self.txtcellno.place(x=200,y=50)
        self.lblcategory = Label (window, text="Select Ticket Category:")
        self.lblcategory.place(x=50, y=100)
        self.lblticket_no = Label (window, text="Number of Tickets Bought:")
        self.lblticket_no.place(x=50, y=150)
        self.txtticket_no =Entry(window)
        self.txtticket_no.place(x=250, y=150)
#Combobox Creation
        self.Combobox = Combobox(root, values=['Soccer', 'Movie', 'Theatre'])
        self.Combobox.place(x=250, y=100, width=180)
#Button
        self.btncal = Button (window, text="Calculate Ticket", borderwidth="10", command=self.cost)
        self.btncal.place(x=50, y=250)
        self.btnclear = Button (window, text="Clear Entries", borderwidth="10")
        self.btnclear.place(x=350, y=250)
#Display
        self.res_lab = Label(window, text=" ", width="50", wraplength=245, textvariable=self.myresult)
        self.res_lab.place(x=50, y=350)


    def cost(self):
#Getting the input
        cellnumber = (self.txtcellno.get())
        category = self.Combobox.get()
        tickets = float(self.txtticket_no.get())
#Calculating the prices

        if category == "Soccer":
            AmountPayable = float(tickets * 40.00 + (14/100))
            Amountline = "The amount payable is: " + str(AmountPayable)
            Reserved = "Reservation for: " + category
            Value = "for: " + str(tickets) + "\n"
            Numbers = "Was done by: " + str(cellnumber)

        elif category == "Movie":
            AmountPayable = float(tickets * 75.00 + (14/100))
            Amountline = "The amount payable is: " + "R" + str(AmountPayable)
            Reserved = "Reservation for: " + category
            Value = "for: " + str(tickets) + "\n"
            Numbers = "Was done by: " + str(cellnumber)


        elif category == "Theatre":
            AmountPayable = float(tickets * 100 + (14/100))
            Amountline = "The amount payable is: " + str (AmountPayable)
            Reserved = "Reservation for: " + category
            Value = "for: " + str(tickets) + "\n"
            Numbers= "Was done by: " + str(cellnumber)
#self.myresult.set("The area is" + str (answer))
        self.myresult.set(Amountline+ "\n"+ Reserved + "\n " + Value + Numbers)



obj_total_cost =Tickets(root)

root.mainloop()

