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

# Determines a grade based on the number of errors a player has made.
def grade(error_count):
	if error_count > 10:
		grade = "X"
	elif error_count > 8:
		grade = "E"
	elif error_count > 6:
		grade = "D"
	elif error_count > 4:
		grade = "C"
	elif error_count > 2:
		grade = "B"
	elif error_count > 0:
		grade = "A"
	else:
		grade = "PERFECT"
	
	return grade
