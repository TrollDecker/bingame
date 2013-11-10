import os

# Clears the screen and outputs the player's current progress, and their current error count.
def print_chain(answer_chain, number, error_count):
	# Clears the screen, using the operating system command "cls" in Windows and "clear" in Unix-likes.
	os.system("cls" if os.name == "nt" else "clear")
	print str(number)
	print "-----------"
	for answer in answer_chain:
		print str(answer[0]) + " r" + str(answer[1])
	print ""
	print "Errors: " + str(error_count)

# Provide an intro explaining how to play.
def intro():
	intro_text = ""
	intro_text += "How to play\n"
	intro_text += "===========\n"
	intro_text += "You are given a number, and must convert this number to its binary equivalent.\n"
	intro_text += "Impossible, you say? Well, no, there is a way.\n\n"
	intro_text += "Take the number you are given and divide it by two. If the result is a decimal\n"
	intro_text += "value then round it down (not up, regardless of the decimal) to the nearest\n"
	intro_text += "whole number and make a note of the remainder. The remainder in this case can\n"
	intro_text += "only be 1, if the result was a decimal, or 0 otherwise.\n\n"
	intro_text += "When you're done you will be asked to enter the binary value. Do this by\n"
	intro_text += "reciting all of the remainders in REVERSE order. When you get it right, you'll\n"
	intro_text += "be graded on the errors you've made along the way."
	
	print intro_text
	raw_input("Got that? Hit enter to begin.")
