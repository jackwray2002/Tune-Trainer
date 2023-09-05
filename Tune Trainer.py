import tkinter as tk
from time import sleep
from random import randint
from winsound import Beep
from math import floor

#List representing note values
note_values = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

#Creates list of all note frequencies over octave interval from 3 to 6.
note_frequencies = [130.81]
for i in range(1,49):
    note_frequencies.insert(i, note_frequencies[i-1] * 1.059463)

#Class representing application.
class Application(tk.Frame):
    def __init__(self, parent):
        super().__init__(width=300, height=150)
        self.parent = parent
        self.pack()

        #Selects first note.
        self.pick_note()

        #Creates sound_button, binds with function play_sound to play current note.
        self.sound_button = tk.Button(self, text="Play")
        self.sound_button.place(relx=0, rely=.25, relwidth=.2, relheight=.75)
        self.sound_button.bind("<Button-1>", self.play_sound)

        #Creates piano keys, which are embedded into key_buttons[].
        self.key_buttons = []
        for i in range(0,12):
            self.key_buttons.insert(i, tk.Button(self))
            if i <= 4:
                if i % 2 == 0:
                    self.key_buttons[i].place(relx=.2+i*(.8/14), rely=.25,
                    relwidth=.8/7, relheight=.75)
                    self.key_buttons[i].lower()
                else:
                    self.key_buttons[i].place(relx=.2+i*(.8/14)+(.8/28), rely=.25,
                    relwidth=.8/14, relheight=.5)
                    self.key_buttons[i].config(bg="black")
                    
            else:
                if i % 2 == 0:
                    self.key_buttons[i].place(relx=.2+i*(.8/14)+(.8/28)*3, rely=.25,
                    relwidth=.8/14, relheight=.5)
                    self.key_buttons[i].config(bg="black")
                    
                else:
                    self.key_buttons[i].place(relx=.2+(.8/14)+i*(.8/14), rely=.25,
                    relwidth=.8/7, relheight=.75)
                    self.key_buttons[i].lower()
            #Binds all keys to key_press function.
            self.key_buttons[i].bind("<Button-1>", self.key_press)

        #Label which displays "What note is this?" and provides evaluation on input.
        self.feedback_label = tk.Label(self, text="What note is this?")
        self.feedback_label.place(relx=0, rely=0, relwidth=1, relheight=.25)
        self.feedback_label.lower()

    def pick_note(self):
        #Note_number represents random position on octave interval from 3 to 6.
        #Obtains frequency and value from note_number.
        self.note_number = randint(0, 48)
        self.note_frequency = note_frequencies[self.note_number]
        self.note_value = note_values[self.note_number % 12]

        #Obtains string with value and octave("C#0").        
        self.note_value_octave = (note_values[self.note_number % 12]+
        str(floor(self.note_number / 12)+3))

        #Plays new note
        self.play_sound(None, 600)

    #Plays note at note_frequency for length ms.    
    def play_sound(self, event, length=1000):
        Beep(round(self.note_frequency), length)

    #Evaluates piano key press, determines if correct key pressed, selects new note.
    def key_press(self, event):
        #Isolates button number from button name,
        #Subtracts 2 from button number to cooresponds with note_values[] equivalent.
        if note_values[int(event.widget._name[7::])-2] == self.note_value:
            #Feedback_label displays "Correct!..." if correct note chosen.
            self.feedback_label.config(text="Correct! The note was "+
            self.note_value_octave+".")
        
        else:
            #Feedback_label displays "Incorrect;..." if incorrect note chosen.
            self.feedback_label.config(text="Incorrect; the note was "+
            self.note_value_octave+".")
        #Picks new note.
        self.pick_note()

#Runs application.
if __name__ == "__main__":   
    root = tk.Tk()
    root.title("Tune Trainer")
    root.resizable(0, 0)
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
