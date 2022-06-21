from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter

SUSPECTS = ("Green", "Mustard", "Peacock", "Plum", "Scarlet", "White")
WEAPONS = ("Candlestick", "Knife", "Pipe", "Revolver", "Rope", "Wrench")
ROOMS = ("Ballroom", "Billiard Room", "Conservatory", "Dining Room",
         "Hall", "Kitchen", "Library", "Lounge", "Study")

suspects = ["Green", "Mustard", "Peacock", "Plum", "Scarlet", "White"]
weapons = ["Candlestick", "Knife", "Pipe", "Revolver", "Rope", "Wrench"]
rooms = ["Ballroom", "Billiard Room", "Conservatory", "Dining Room",
         "Hall", "Kitchen", "Library", "Lounge", "Study"]


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.intro = Label(self, text="Welcome to Clue Helper!")
        self.intro.grid()
        suspectsString = ""
        for x in suspects:
            suspectsString += " " + x
        self.susListLabel = Label(self, text=suspectsString)
        self.susListLabel.grid()
        weaponsString = ""
        for x in weapons:
            weaponsString += " " + x
        self.weaListLabel = Label(self, text=weaponsString)
        self.weaListLabel.grid()
        roomsString = ""
        for x in rooms:
            roomsString += " " + x
        self.rooListLabel = Label(self, text=roomsString)
        self.rooListLabel.grid()
        self.per = Label(self, text="Person:")
        self.per.grid()
        self.testSus = ttk.Combobox(self, values=suspects)
        self.testSus.grid()
        self.wea = Label(self, text="Weapon:")
        self.wea.grid()
        self.testWea = ttk.Combobox(self, values=weapons)
        self.testWea.grid()
        self.roo = Label(self, text="Room:")
        self.roo.grid()
        self.testRoo = ttk.Combobox(self, values=rooms)
        self.testRoo.grid()
        self.bt = Button(self, text="Confirm", command=self.readUpdateValues)
        self.bt.grid()
        if (len(suspects) == 1):
            self.susListLabel = Label(
                "Congrats, you have found the suspect. They are: " + suspects[0])

    def readUpdateValues(self):
        self.susActions()
        self.weaActions()
        self.rooActions()

    def susActions(self):
        if (len(suspects) > 1):
            current_sus = self.testSus.get()
            if current_sus != None:
                suspects.remove(current_sus)
            self.testSus["values"] = suspects
            suspectsString = ""
            for x in suspects:
                suspectsString += " " + x
            self.susListLabel.configure(text=suspectsString)
        if (len(suspects) == 1):
            self.susListLabel.configure(
                text="Congrats, you have found the suspect. They are: " + suspects[0])

    def weaActions(self):
        if (len(weapons) > 1):
            current_wea = self.testWea.get()
            if current_wea != None:
                weapons.remove(current_wea)
            self.testWea["values"] = weapons
            weaponsString = ""
            for x in weapons:
                weaponsString += " " + x
            self.weaListLabel.configure(text=weaponsString)
        if (len(weapons) == 1):
            self.weaListLabel.configure(
                text="Congrats, you have found the murder weapon. It is: " + weapons[0])

    def rooActions(self):
        if (len(rooms) > 1):
            current_roo = self.testRoo.get()
            if current_roo != None:
                rooms.remove(current_roo)
            self.testRoo["values"] = rooms
            roomsString = ""
            for x in rooms:
                roomsString += " " + x
            self.rooListLabel.configure(text=roomsString)
        if (len(rooms) == 1):
            self.rooListLabel.configure(
                text="Congrats, you have found the room where the murder happened. It is: " + rooms[0])


root = Tk()
root.title("Clue Helper")
root.geometry("600x400")
Application(root)
root.mainloop()
