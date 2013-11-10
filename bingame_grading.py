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
