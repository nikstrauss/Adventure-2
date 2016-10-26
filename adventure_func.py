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
	elif race == "E":
		hp = 3 	
		ap = 0
		st = 4
		sp = 6
		iq = 7
		mp = 8
		lk = 6
	elif race == "O":
		hp = 8
		ap = 2
		st = 7
		sp = 3
		iq = 2
		mp = 2
		lk = 2
	if race == "H":
		race = "Human"
	elif race == "E":
		race = "Elf"
	elif race == "O":
		race = "Orc"
	cc = input("What is thy class [W]arrior, [M]age, or [R]ouge? ")
	if cc == "W":
		hp = hp+2
		st = st+2
		sp = sp+1
		mp = 0
	elif cc == "M":
		hp = hp-2
		st = st-3
		sp = sp-3
		mp = mp+5
		lk = lk-2
	elif cc == "R":
		hp = hp-1
		st = st-1
		sp = sp+3
		mp = mp-2
		lk = lk+3
	if cc == "W":
		cc = "Warrior"
	elif cc == "M":
		cc = "Mage"
	elif cc == "R":
		cc = "Rouge"
	print ("You are",name,"The",race, cc)
	print ("Your stats are as follows \n Your hitpoint total is", hp,"\n Your strenght total is", st, "\n Your speed total is", sp, "\n Your magic total is", mp, "\n Your luck total is", lk )
else: print ("I asked a simple question, which you did not answer. Be gone with you!")