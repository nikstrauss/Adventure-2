print ("Welcome to Adventure 2!")
start = input("Do you want to play? ")
if start == "no":
	input("Ok, press any key to exit")
elif start == "yes":
	name = input("What is your name, Adventurer? ")
race = input("Are you a [H]uman, a [E]lf or a [O]rc ")
if race == "H":
	hp = 5 #Health
	ap = 0 #Armor
	st = 5 #Strength
	sp = 5 #Speed
	iq = 5 #Intelgence 
	mp = 5 #Magic
	lk = 5 #Luck
	print ("Hail, Human", name)
elif race == "E":
	hp = 3
	ap = 0
	st = 4
	sp = 6
	iq = 7
	mp = 8
	lk = 6
	print ("Hail, Elf", name)
elif race == "O":
	hp = 8
	ap = 2
	st = 7
	sp = 3
	iq = 2
	mp = 2
	lk = 2
	print ("Hail, Orc", name)
