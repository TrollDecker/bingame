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

import math

# Takes the current progress value and halfs it. Then takes that and rounds it down.
# Then divides the difference by 5 and multiplies it by 10, resulting in either 1 or 0.
def get_remainder(progress):
	half_progress = float(progress) / 2
	half_progress_rounded = math.floor(half_progress)
	return int((half_progress - half_progress_rounded) / 5 * 10)

# What it says on the tin. :\
def half_number(progress):
	return int(math.floor(float(progress / 2)))
