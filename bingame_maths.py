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
