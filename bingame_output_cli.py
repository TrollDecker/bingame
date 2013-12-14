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

from bingame_output import *

# Clears the screen and outputs the player's current progress, and their current error count.
def cli_print_chain(answer_chain, number, error_count):
	clear_screen()
	print str(number)
	print "-----------"
	for answer in answer_chain:
		print build_answer(answer)
	print ""
	print "Errors: " + str(error_count)

# Provide an intro explaining how to play (CLI).
def cli_intro():
	clear_screen()
	print build_intro()
	raw_input("Got that? Hit enter to begin.")
