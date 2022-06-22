from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter

SUSPECTS = ("Green", "Mustard", "Peacock", "Plum", "Scarlet", "White")
WEAPONS = ("Candlestick", "Knife", "Pipe", "Revolver", "Rope", "Wrench")
ROOMS = ("Ballroom", "BilliardRoom", "Conservatory", "DiningRoom",
         "Hall", "Kitchen", "Library", "Lounge", "Study")
ALL = SUSPECTS + WEAPONS + ROOMS


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.suspects = list(SUSPECTS)
        self.weapons = list(WEAPONS)
        self.rooms = list(ROOMS)
        self.grid()
        self.begin_setup()

    def begin_setup(self):
        validcount = (3, 4, 5, 6)
        self.intro = Label(
            self, text="Welcome to Clue Helper! How many people are playing today?")
        self.intro.grid()
        self.playnum = ttk.Combobox(self, values=validcount)
        self.playnum.grid()
        self.sbt = Button(self, text="Confirm", command=self.setup_names)
        self.sbt.grid()

    def setup_names(self):
        if not self.playnum.get():
            tkinter.messagebox.showinfo(
                title="Error", message="Please choose a player count!")
            return
        self.playercount = int(self.playnum.get())
        self.intro.grid_remove()
        self.playnum.grid_remove()
        self.sbt.grid_remove()
        self.intro = Label(self, text="What are the players names?")
        self.intro.grid()
        self.players = ["You"]
        self.otrplayervar = []
        self.play2lbl = Label(text="Player 2 name:")
        self.play2lbl.grid(row=1)
        self.play2ent = Entry()
        self.play2ent.grid(row=2)
        self.otrplayervar.append(self.play2ent)
        self.play3lbl = Label(text="Player 3 name:")
        self.play3lbl.grid(row=3)
        self.play3ent = Entry()
        self.play3ent.grid(row=4)
        self.otrplayervar.append(self.play3ent)
        if self.playercount > 3:
            self.play4lbl = Label(text="Player 4 name:")
            self.play4lbl.grid(row=5)
            self.play4ent = Entry()
            self.play4ent.grid(row=6)
            self.otrplayervar.append(self.play4ent)
        if self.playercount > 4:
            self.play5lbl = Label(text="Player 5 name:")
            self.play5lbl.grid(row=7)
            self.play5ent = Entry()
            self.play5ent.grid(row=8)
            self.otrplayervar.append(self.play5ent)
        if self.playercount > 5:
            self.play6lbl = Label(text="Player 6")
            self.play6lbl.grid(row=9)
            self.play6ent = Entry()
            self.play6ent.grid(row=10)
            self.otrplayervar.append(self.play6ent)
        self.nbt = Button(self, text="Confirm", command=self.finish_setup)
        self.nbt.grid()

        print(self.players)

    def finish_setup(self):
        for x in self.otrplayervar:
            if not x.get():
                tkinter.messagebox.showinfo(
                    title="Error", message="Please give players names!")
                return
            else:
                self.players.append(x.get())
        self.intro.grid_remove()
        self.nbt.grid_remove()
        self.play2ent.grid_remove()
        self.play2lbl.grid_remove()
        self.play3ent.grid_remove()
        self.play3lbl.grid_remove()
        if self.playercount > 3:
            self.play4ent.grid_remove()
            self.play4lbl.grid_remove()
        if self.playercount > 4:
            self.play5ent.grid_remove()
            self.play5lbl.grid_remove()
        if self.playercount > 5:
            self.play6ent.grid_remove()
            self.play6lbl.grid_remove()
        self.main_function()

    def main_function(self):
        self.peg = Label(self, text="Please enter current guess:")
        self.peg.grid()
        self.per = Label(self, text="Person:")
        self.per.grid()
        self.testSus = ttk.Combobox(self, values=SUSPECTS)
        self.testSus.grid()
        self.wea = Label(self, text="Weapon:")
        self.wea.grid()
        self.testWea = ttk.Combobox(self, values=WEAPONS)
        self.testWea.grid()
        self.roo = Label(self, text="Room:")
        self.roo.grid()
        self.testRoo = ttk.Combobox(self, values=ROOMS)
        self.testRoo.grid()
        self.wcs = Label(self, text="Who couldn't show?")
        self.wcs.grid()
        self.boolist = []
        self.cannot2 = BooleanVar()
        self.boolist.append(self.cannot2)
        self.cant2 = Checkbutton(
            self, text=self.players[1], variable=self.cannot2)
        self.cant2.grid()
        self.could2 = list(ALL).copy()
        self.cannot3 = BooleanVar()
        self.boolist.append(self.cannot3)
        self.cant3 = Checkbutton(
            self, text=self.players[2], variable=self.cannot3)
        self.cant3.grid()
        self.could2 = list(ALL).copy()
        if self.playercount > 3:
            self.cannot4 = BooleanVar()
            self.boolist.append(self.cannot4)
            self.cant4 = Checkbutton(
                self, text=self.players[3], variable=self.cannot4)
            self.cant4.grid()
            self.could4 = list(ALL).copy()
        if self.playercount > 4:
            self.cannot5 = BooleanVar()
            self.boolist.append(self.cannot5)
            self.cant5 = Checkbutton(
                self, text=self.players[4], variable=self.cannot5)
            self.cant5.grid()
            self.could5 = list(ALL).copy()
        if self.playercount > 5:
            self.cannot6 = BooleanVar()
            self.boolist.append(self.cannot6)
            self.cant6 = Checkbutton(
                self, text=self.players[5], variable=self.cannot6)
            self.cant6.grid()
            self.could6 = list(ALL).copy()
        # change create_widgets to load_info when method is completes
        self.ibt = Button(self, text="Confirm", command=self.create_widgets)
        self.ibt.grid()

    # def load_info(self):
        # for x in self.boolist:
        # if x:

        # for x in self.playercount:

    def create_widgets(self):
        self.sus = Label(self, text=self.suspects)
        self.sus.grid()
        self.wea = Label(self, text=self.weapons)
        self.wea.grid()
        self.roo = Label(self, text=self.rooms)
        self.roo.grid()
        self.alltext = Label(self, text="Known:")
        self.alltext.grid()
        self.all = ttk.Combobox(
            self, values=self.suspects + self.weapons + self.rooms)
        self.all.grid()
        self.bt = Button(self, text="Confirm", command=self.read_values)
        self.bt.grid()

    def read_values(self):
        current_all = self.all.get()
        if current_all in self.suspects:
            if len(self.suspects) > 1:
                self.suspects.remove(current_all)
                self.update_values()
                if len(self.suspects) == 1:
                    tkinter.messagebox.showinfo(
                        title="Mystery Solved!", message="The killer was " + self.suspects[0] + "!")
        elif current_all in self.weapons:
            if len(self.weapons) > 1:
                self.weapons.remove(current_all)
                self.update_values()
                if len(self.weapons) == 1:
                    tkinter.messagebox.showinfo(
                        title="Mystery Solved!", message="They were killed with the " + self.weapons[0] + "!")
        elif current_all in self.rooms:
            if len(self.rooms) > 1:
                self.rooms.remove(current_all)
                self.update_values()
                if len(self.rooms) == 1:
                    tkinter.messagebox.showinfo(
                        title="Mystery Solved!", message="The murder was in " + self.rooms[0] + "!")

    def update_values(self):
        self.sus["text"] = self.suspects
        self.wea["text"] = self.weapons
        self.roo["text"] = self.rooms
        self.all["values"] = self.suspects + self.weapons + self.rooms


root = Tk()
root.title("Clue Helper")
root.geometry("400x400")
test = Application(root)
test.mainloop()
