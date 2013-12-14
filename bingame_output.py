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

import os

def clear_screen():
	# Clears the screen, using the operating system command "cls" in Windows and "clear" in Unix-likes.
	os.system("cls" if os.name == "nt" else "clear")

# Need to build the intro first...
def build_intro():
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
	
	return intro_text

def build_answer(answer):
	return str(answer[0]) + " r" + str(answer[1])
