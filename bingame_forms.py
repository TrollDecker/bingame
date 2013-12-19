# Number-to-binary game
# Copyright (C) 2013  Jonathan Humphreys

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import random, Tkinter
from bingame_maths import get_remainder, half_number
from bingame_grading import grade

# Class to store data relevant to this form.
# error_count will need to be accessible from outside this form, though.
class GameMain():
	def __init__(self, forms, apps):
		self.forms = forms                              # Need to carry the whole dictionary across every damn class.
		self.apps = apps
		self.parent = self.forms["root"]                # root is the parent of all widgets created in this class.
		
		self.number = random.randint(1, 2048)			# Randomly generated, between 1 and 2048. The player must gradually find the binary value of this number.
		self.progress = self.number						# The current number that must be divided by 2 to continue. Initially the same as "number".
		self.answer = 0									# The player's answer.
		self.remainder = 0								# The remainder from their answer. Can only ever be 1 or 0.
		self.answer_chain = []							# Stores each answer and its remainder and is recited with each step.
		self.error_count = 0							# Counts the number of errors a player makes in the process of a conversion.
		
		self.init_ui()
		
	# Configures the window to the appropriate paramaters.
	def init_ui(self):
		self.parent.title("Convert to Binary")          # Sets the window title.
		self.parent.geometry("200x300+400+150")         # Sets the window size (200x300), as well as its position (numbers preceded by plus signs).
		
		# Canvas upon which to output the answer chain.
		self.canAnswers = Tkinter.Canvas(self.parent, bg = "#EEEEEE")
		self.canAnswers.place(bordermode = "outside", x = 5, y = 5, width = 190, height = 190)
		
		# Label to visually idenitfy the error counter.
		self.lblErrorsTag = Tkinter.Label(self.parent, anchor = "w", text = "Errors:")
		self.lblErrorsTag.place(bordermode = "outside", x = 5, y = 200, width = 145, height = 25)
		
		# The error counter itself. It's a label, so requires a StringVar to be assigned to the widget's 'textvariable' property.
		# It's awkward like that.
		self.error_value = Tkinter.StringVar()
		self.error_value.set(str(self.error_count))
		self.lblErrors = Tkinter.Label(self.parent, anchor = "w", textvariable = self.error_value)
		self.lblErrors.place(bordermode = "outside", x = 155, y = 200, width = 40, height = 25)
		
		# Label to hold the last correct answer. Saves some confusion by having it right next to the answer entry boxes.
		self.last_answer_value = Tkinter.StringVar()
		self.last_answer_value.set(str(self.progress))
		self.lblLastAnswer = Tkinter.Label(self.parent, anchor = "w", textvariable = self.last_answer_value)
		self.lblLastAnswer.place(bordermode = "outside", x = 5, y = 230, width = 60, height = 25)

		# Entry box to accept the answer rounded down to the neared whole.
		self.entAnswer = Tkinter.Entry(self.parent, justify = "center")
		self.entAnswer.place(bordermode = "outside", x = 70, y = 230, width = 105, height = 25)

		# Entry box to accept the remainder left after working out the answer.
		self.entRemainder = Tkinter.Entry(self.parent, justify = "center")
		self.entRemainder.place(bordermode = "outside", x = 175, y = 230, width = 20, height = 25)

		# A big ol' button to submit the player's answer.
		self.btnSubmit = Tkinter.Button(self.parent, text = "Submit", command = self.submit_answer)
		self.btnSubmit.place(bordermode = "outside", x = 5, y = 260, width = 190, height = 35)
		
	def submit_answer(self):
		# Try to extract the answer and remainder from the entry boxes. If neither can be converted to an integer,
		# increase the error counter by 1.
		try:
			self.answer = int(self.entAnswer.get())
			self.remainder = int(self.entRemainder.get())
			
			# If both values are correct, add it to the answer chain.
			# Otherwise, an error for you, player.
			if self.answer == half_number(self.progress) and self.remainder == get_remainder(self.progress):
				self.remainder = get_remainder(self.progress)
				self.progress = half_number(self.progress)
				self.answer_chain.append(self.canAnswers.create_text(0,12 * len(self.answer_chain), anchor = "nw", text = str(self.progress) + " r" + str(self.remainder)))
			else:
				self.error_count += 1

		except ValueError:
			self.error_count += 1
		
		# Update the error counter and the current value to be dividing. Also clear the entry boxes.
		self.error_value.set(str(self.error_count))
		self.last_answer_value.set(str(self.progress))
		self.entAnswer.delete(0, "end")
		self.entRemainder.delete(0, "end")
		
		# If the player has reached 0, it's time to bring forth the binary entry form.
		if self.progress == 0:
			binary_entry(self.forms, self.apps)

class EnterBinary():
	def __init__ (self, forms, apps):
		self.forms = forms
		self.apps = apps
		self.parent = forms["binary"]					# binary being the parent form for every widget here.
		self.apps["game"] = apps["game"]

		self.final_binary = bin(apps["game"].number)	# The final binary value representing the number.
		self.binary_answer = ""							# The player's attempt at entering the binary value.
		
		self.init_ui()
	
	def init_ui(self):
		self.parent.title("Enter binary")
		self.parent.geometry("300x35+400+150")
		
		# The entry box for the player's binary answer. The player needs to look back on their answers and enter all
		# of the remainders from the last one up to the first.
		self.entBinary = Tkinter.Entry(self.parent, justify = "center")
		self.entBinary.place(bordermode = "outside", x = 5, y = 5, width = 195, height = 25)
		
		# Button that does what it says on the tin: submits the answer.
		self.btnSubmit = Tkinter.Button(self.parent, text = "Submit", command = self.submit_answer)
		self.btnSubmit.place(bordermode = "outside", x = 205, y = 5, width = 90, height = 25)

	def submit_answer(self):
		# Take the player's answer from the entry box and precede it with "0b" so that it can be easily compared
		# with the correct answer.
		self.binary_answer = "0b" + self.entBinary.get()
		
		# If the answer's correct, call the scorecard window.
		# Otherwise, increase the error counter by 1 and update the main window accordingly.
		if self.binary_answer == self.final_binary:
			scorecard(self.forms,self.apps)
		else:
			self.apps["game"].error_count += 1
			self.apps["game"].error_value.set(str(self.apps["game"].error_count))

class FinalScore():
	def __init__ (self, forms, apps):
		self.forms = forms
		self.apps = apps
		self.parent = forms["scorecard"]				# scorecard is the parent for all widgets in this class.
		
		self.error_count = apps["game"].error_count		# Pass the error counter to one local to this window.
		self.grade = grade(self.error_count)			# Obtain a grade based on the number of errors made by the player.
		
		# Get rid of the root and binary forms. They are no longer needed.
		forms["root"].destroy()
		del(apps["game"])
		forms["binary"].destroy()
		del(apps["binary"])
		
		self.init_ui()
		
	def init_ui(self):
		self.parent.title("Scorecard")
		self.parent.geometry("300x100+400+150")
		
		# Label to show the player's error count, and the grade determined from that number.
		self.lblScore = Tkinter.Label(self.parent, anchor = "center", text = "Errors made:\n" + str(self.error_count) + "\nYour grade:\n" + self.grade)
		self.lblScore.place(bordermode = "outside", x = 5, y = 5, width = 290, height = 60)
		
		# Button to play again.
		self.btnPlayAgain = Tkinter.Button(self.parent, text = "Play again", command = self.play_again)
		self.btnPlayAgain.place(bordermode = "outside", x = 5, y = 70, width = 140, height = 25)
		
		# Button to quit.
		self.btnQuit = Tkinter.Button(self.parent, text = "Exit", command = self.quit_game)
		self.btnQuit.place(bordermode = "outside", x = 155, y = 70, width = 140, height = 25)
	
	# Destroys the window and deletes this object, effectively ending the program.
	def quit_game(self):
		self.parent.destroy()
		del(self)
	
	# Destroys this window and spawns a new game window.
	def play_again(self):
		self.parent.destroy()
		main()
		del(self)

def main():
	# Create dictionaries to store all the forms and widget classes. It's easier to pass a whole dict than it is to pass each individual form.
	# Cleaner too.
	forms = {}
	apps = {}
	forms["root"] = Tkinter.Tk()						# Create a new window and assign it to the entry 'root' in the dict.
	apps["game"] = GameMain(forms, apps)				# Create an object based on the GameMain class, which will create all the needed widgets and variables.
	forms["root"].mainloop()							# Commence the event-loop.

def binary_entry(forms, apps):
	forms["binary"] = Tkinter.Tk()
	apps["binary"] = EnterBinary(forms, apps)
	forms["binary"].mainloop()

def scorecard(forms, apps):
	forms["scorecard"] = Tkinter.Tk()
	apps["scorecard"] = FinalScore(forms, apps)
	forms["scorecard"].mainloop()
