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

import random
from bingame_maths import get_remainder, half_number
from bingame_output import print_chain, intro
from bingame_grading import grade

number = 0                        # Randomly generated, between 1 and 1024. The player must gradually find the binary value of this number.
progress = 0                      # The current number that must be divided by 2 to continue. Initially the same as "number".
answer = 0                        # The player's answer.
remainder = 0                     # The remainder from their answer. Can only ever be 1 or 0.
answer_chain = []                 # Stores each answer and its remainder and is recited with each step.
final_binary = "0b0"              # The final binary value representing the number.
binary_answer = ""                # The player's attempt at entering the binary value.
error_count = 0                   # Counts the number of errors a player makes in the process of a conversion.

keep_playing = "y"                # When the player finishes, they are asked to go again. If they answer "n" the following loop ends and in turn the program.

intro()

while keep_playing != "n":
	number = random.randint(1, 1024)
	progress = number
	answer = 0
	remainder = 0
	answer_chain = []
	final_binary = bin(number)
	binary_answer = ""
	error_count = 0
	
	while progress > 0:
		while True:
			# Clear the screen and print the current progress.
			print_chain(answer_chain, number, error_count)
			# Try to ask the player for an answer and convert it to integer.
			try:
				answer = int(raw_input(str(progress) + " / 2 = "))
			# Did the player enter a string or leave it blank? (Both cases would cause this Error, since they can't be converted to integer.
			except ValueError:
				continue
			else:
				try:
					remainder = int(raw_input("remainder: "))
				except ValueError:
					continue
				else:
					# Exit the loop.
					break

        # If the player's answer and remainder are correct, then pass those answers to the answer chain.
        # Otherwise, increase the error counter by 1. 
		if answer == half_number(progress) and remainder == get_remainder(progress):
			remainder = get_remainder(progress)
			progress = half_number(progress)
			answer_chain.append([progress, remainder])
		else:
			error_count += 1

	while final_binary != binary_answer:
		print_chain(answer_chain, number, error_count)
		# Ask the player for the binary value (by reciting the remainders in REVERSE order) and add the binary prefix to it.
		binary_answer = "0b" + raw_input(str(number) + " in binary: ")
		# If the player answers incorrectly, increase the error counter by 1.
		if final_binary != binary_answer:
			error_count += 1

	print_chain(answer_chain, number, error_count)
	print "Grade:" + grade(error_count)
	# Ask if the player wishes to try again. Convert the answer to lowercase.
	#If the player answers with anything but "n" the player will start again.
	keep_playing = raw_input("Try again? (y/n) ").lower()
