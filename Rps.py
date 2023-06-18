import random 

start = input("You want to play RPS? (Y/N) ")
if start == "Y" or "y" or "yes" or "Yes":
	game = input ("Ok, Choose (R/P/S) ")
	if game == "R":
		r = random.randint(1,3)
		if r == 1:
			print("GG i choose Scissors and lost!")
		elif r == 2:
			print("GG i won by choosing paper")
		elif r == 3:
			print("Its a Draw")
	elif game == "P":
		p = random.randint(1,3)
		if p == 1:
			print("Wow i lost because i chose Rock")
		elif p == 2:
			print("Its a Draw")
		elif p == 3:
			print("Haha i won because i chose scissors")
	elif game == "S":
		s = random.randint(1,3)
		if s == 1:
			print("Its a Draw")
		elif s == 2:
			print("Ooo i won cuz i chose rock")
		elif s == 3:
			print("NOOOOOO i lost because i chose paper")
	else:
		print("You weren't supposed to choose that!")
else:
	print("ok, maybe next time you will play")