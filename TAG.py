import time, random, os, sys

timeline=""

sack=[]

container={}

def cleanup(x): #cleans up input
	return x.lower().strip().translate({ord(i):None for i in  "?!@#$%^&*',.:;+=/\|][}{-_("})
def slwreveal2(x,y):
	line=x
	y=y
	enile=""
	for i in line:
		os.system("clear")
		enile += i
		print(enile)
		time.sleep(y)
class color:
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

def timewarp(x):
	global timeline
	global sack
	sack=[]
	if int(x) >=1990 and int(x) <=2050:
		timeline += "modern "
	elif int(x) >=500 and int(x) <=1500:
		timeline += "medieval "
	elif int(x) <500:
		timeline += "ancient "
	elif int(x) >2050:
		timeline += "future "
	else: #fix
		slwreveal2("TIME INVALID.....MAJOR MALFUNCTION.....*CRASH IMMINENT*",.12)
		timeline = "DEAD"

def checkshot(x,y):
	hr=int(x)
	minutes=int(y)
	if hr >=21 and hr <=23 and minutes >=10 and minutes <60:
		return "Kill Confirmed. Mission Accomplished."
	else:
		return "Shot missed, guards allerted.\nMission Failed"

slwreveal2("Text Adventure Game",.05)
time.sleep(1)
print("\nHow far can you go?\n")
time.sleep(1)
input("How many players?> ")
slwreveal2(". . .\n",.5)
print("This is just a one player game, so idk why I even asked ('3')\n")
name=input("Player 1 NAME: ")
age=int(cleanup(input("Player 1 AGE: ")))
gender=cleanup(input("Player 1 Gender: "))
if gender=="male" or gender=="m" or gender=="f" or gender=="female" or gender=="other": #fix
	gender=gender
else:
	gender="other"
	print("Not a real gender...")
	time.sleep(2)

#Chapter 1	TIME SELECTION
slwreveal2("Chapter 1: A 'humble' beginning",.12)
print("\nYou find yourself in your home, rummaging through your clothes, when you realize that you forgot one of the most basic things.\n\nSomething most people have no trouble remembering.")
time.sleep(3)
timewarp1=cleanup(input("What year is it?> "))
timewarp(timewarp1)
print("\n"+color.BOLD+timeline+color.END+"\n")
#EVENTS Ch. 1
if timeline == "modern ":
	input("Press Enter to continue...")
	print("'Right, right.....' you think. Gazing out the window of your apartment in homey Saint Albans, Vermont")
	print("\nYou put on some casual clothing, stuffed your phone in your pocket, and headed outside.")
	sack += ["Phone"]
	time.sleep(1)
	print("\n		A "+color.BOLD+"PHONE"+color.END+" has been added to your inventory.")
	print("\n		You have: "+" ".join(sack)+", in your inventory.\n") #for showing inventory
	input("Press Enter to Continue...")
	print("You open the door and feel a gust of wind blow through your hair.\n")
	time.sleep(1)
	print("Soothing...\n")
	time.sleep(1)
	print("It was enough to make anyone smile and be happy with life all around them.\n")
	input("Press Enter to Continue...")
	slwreveal2("TOO BAD YOU ARE NOT ANYONE\n",.12)
	print("Your name is "+color.RED+name+color.END+"\n")
	time.sleep(1)
	print("It is WW3")
	time.sleep(1)
	print("\nAnd you are a hired assassin for the American Government.")
	time.sleep(1)
	print("\n	Report to the given location for briefing on your next assignment.\nBe there ON TIME, otherwise you will be terminated.")
	input("Press Enter to Continue...")
	if age >=16:
		timeline += "1" #first option, second option and so forth. Doesn't start with 0
	elif age <16:
		timeline += "2"
	if timeline == "modern 1":
		print("You head down to the parking lot and you get into your white convertible, issued by the government of course.\nThen you drive to the rendezvous.\n")
		time.sleep(1)
		print("The given location is a dark alley on the side of a nighclub.\nA man in a hoodie is seemingly waiting for you.")
		print("Do you trust him?")
		trust = ""
		while trust not in ['yes','no']:
			trust=cleanup(input("Yes or No> "))
			if trust not in ['yes','no']:
				print("That's not an option.")
		if trust=="yes":
			print("You walk up to the man, and he hands you a manilla folder.\n")
			timeline += " trust"
		elif trust=="no":
			print("You walk away from the man.\n")
			timeline = "modern 1 fail"
			print("Mission 1 abandoned\n")
			input("Press Enter to Continue")
		if timeline == "modern 1 trust":
			print("You walk back to your car, and read your next assignment.\n")
			input("Press Enter to read briefing...")
			print(color.RED+"		MISSION BRIEFING\n	Your next assignment is the termination of subject 'EXX-244'.\n	A dangerous criminal overlord who has been blocking international trade between the United States and 4 countries he is controlling.\n	")
			print("	We will provide you with a firearm, and transportation until 15 kilometers from the target.\n")
			print("	You are REQUIRED to execute the subject during the given hours.\n It is the time segment in which the subject is most actively walking the compound where he is located.\n Special Forces will be infiltrating the compound and engaging the west wing.")
			print("	It is crucial that the execution takes place during the given times. Subject EXX-244 must NOT be alerted of the presence of the Special forces unit when they are breaching. The mission will be considered compromised, and you will be terminated.")
			print("\n		PARAMETERS:\n")
			print("\n-You must execute subject EXX-244 between "+color.END+color.BOLD+"21:10"+color.END+color.RED+" and "+color.END+color.BOLD+"23:59"+color.END+color.RED)
			print("\n-You must leave the attack site immediately after the assignment is complete")
			print("\n-You must leave no trace of your existence at the attack site, or in the country")
			print("\nFailure to meet ANY of the above parameters will result in termination\n"+color.END)
			input("READ ^ Before you press Enter to continue...")
			slwreveal2("MISSION 1",.12)
			print("\nYou arrive at the attack site. You've been provided with a government issue anti-personnel sniper rifle. A "+color.BOLD+".408 M200 Intervention"+color.END+"\n and "+color.BOLD+"35 sniper rounds"+color.END+".\n")
			print("\n		A "+color.BOLD+"Sniper Rifle"+color.END+" has been added to your inventory.")
			print("\n		"+color.BOLD+"35 srounds"+color.END+" have been added to your inventory.") #container NOT sack stackable
			sack += ["Sniper"]
			container["srounds"] = 35
			print("\n		You have: "+" ".join(sack)+" in your inventory.")
			print("\n		You have: "+str(container)+" in your container.\n")
			print("You creep through bushes and trees, heading towards the compound.\nYou are about 1.5 km away.\n") #change environment for country
			print("You come across two paths. One leads to higher ground, the other lower ground.\n")
			path=cleanup(input("Higher or Lower?> "))
			if path=="higher":
				timeline += " higher"
				print("\n'Always higher' you think, as you trudge up the hill.")
				time.sleep(1)
				print("\nYou gaze over the vast area that the compound covers.\nHundreds of guards stand watch, oblivious to the imminent threat.")
				print("\nYou settle down on the ground and prop your tripod up. The subject is barely visible, you are not sure if the shot would make it.\n")
				time.sleep(1)
				print("You see a rickety old watch tower, seemingly abandoned, that you could use for a better vantage point.")
				climb=""
				while climb not in ["yes", "no"]:
					climb=cleanup(input("Yes or No, Climb the tower?> "))
					if climb not in ["yes", "no"]:
						print("That's not an option.")
				if "no" in climb:
					print("You decide that the spot you lie in feels adequate.\nBesides, that tower looks like it could collapse at any minute.")
					print("\nYou grip your M200 firmly, eye down sights.\nYou've done this a hundred times.\nYou set a wind guage, and carefully calculate for bullet drop.\nAll that is left is to wait for the scheduled time.\n")
					while True:
						input("Press Enter to check time...")
						timez=str(random.randrange(24))+":"+str(random.randrange(50)+10)
						print(timez)
						timevar=timez.split(":")
						hr=int(timevar[0])
						minutes=int(timevar[1])
						choice=input("Shoot or Wait?> ")
						if choice== "shoot":
							outtext=checkshot(hr,minutes)
							break
						else:
							continue
					print(outtext)
					container["srounds"]-=1
					if outtext=="Kill Confirmed. Mission Accomplished.":
						timeline = "modern 1 CH1"
						container["medals"]=1
						print("You have "+str(container)+" in your container")
						input("Press Enter to Continue")
					elif outtext=="Shot missed, guards allerted.\nMission Failed":
						timeline = "modern 1 fail"
						input("Press Enter to Continue")
				if "yes" in climb:
					print("You decide that the higher vantage point is worth the risk.\n")
					slwreveal2("You climb up the tow-",.3)
					print("*CRACK*\n")
					time.sleep(3)
					print("*CRACKETY CRACK*\n")
					time.sleep(2)
					print("'crap'\n")
					time.sleep(1)
					print("The entire tower collapses, and you land on your back.\n")
					print("Luckily you weren't hurt, but you ripped your clothes and "+color.BOLD+"SMASHED YOUR PHONE "+color.END+"to bits.")
					sack.remove("Phone")
					print("\n		A "+color.BOLD+"PHONE"+color.END+" has been removed from your inventory.")
					print("\n		You have: "+" ".join(sack)+", in your inventory.\n")
					time.sleep(2)
					print("You walk back to your original spot, and set your tripod back up.")
					print("\nYou grip your M200 firmly, eye down sights.\nYou've done this a hundred times.\nYou set a wind guage, and carefully calculate for bullet drop.\nAll that is left is to wait for the scheduled time.\n")
					while True:
						input("CAN'T CHECK TIME WITHOUT PHONE. Press Enter...")
						timez=str(random.randrange(24))+":"+str(random.randrange(50)+10)
						timevar=timez.split(":")
						hr=int(timevar[0])
						minutes=int(timevar[1])
						choice=input("Shoot or Wait?> ")
						if choice== "shoot":
							outtext=checkshot(hr,minutes)
							break
						else:
							continue
					print(outtext)
					container["srounds"]-=1
					if outtext=="Kill Confirmed. Mission Accomplished.":
						timeline = "modern 1 CH1"
						container["medals"]=1
						print("You have "+str(container)+" in your container")
						input("Press Enter to Continue")
					elif outtext=="Shot missed, guards allerted.\nMission Failed":
						timeline = "modern 1 fail"
						input("Press Enter to Continue")

			elif path=="lower":
				timeline += " lower"
				print("You decided to stick to lower grounds.")
				time.sleep(1)
				print("\nYou wade your way through more brushery and realize that this wasn't the greatest descision.\n")
				time.sleep(2)
				print("In order to get a good shot, you need to get closer to the compound.\nYou proceed to get closer to the compound.\n"+color.GREEN+"4 GUARDS NOTICE YOU LURKING ABOUT"+color.END)
				#implement quicktime here
				print("\nYou are shot on the spot.")
				input("Press Enter to continue...")
				timeline="DEAD"


	if timeline == "modern 2":
		timeline = "modern 2 fail"
		print("You are not old enough to drive to the rendevous.")
		print("Mission 1 unable to complete.")
		input("Press Enter to Continue...")

	if timeline == "modern 1 CH1" or timeline == "modern 1 fail" or timeline == "modern 2 fail":
		os.system("clear")
		print("Before we can continue, I am required to ask you a really important question.\n")
		time.sleep(2)
		print("Will you take the "+color.RED+"RED "+color.END+"pill, or the "+color.BLUE+"BLUE "+color.END+"pill?\n")
		pill=cleanup(input("Red or Blue?> "))
		if pill=="red":
			line="WHO THE HELL PICKS THE RED PILL!?!"
			enile=""
			for i in line:
				enile += i
				print(enile)
				print(enile)
				print(enile)
				print(enile)
				print(enile)
				print(enile)
				print(enile)
				print(enile)
				print(enile)
				print(enile)
				print(enile)
				print(enile)
				time.sleep(.1)
			sys.exit()
#Chapter 2
		slwreveal2("Chapter 2: Needle in a Haystack",.12)
		print("\nYour next assignment came quicker than expected.\n")
		print("You find the hooded man once more, and you take your next assignment.\n")
		input("Press Enter to read briefing...")
		print(color.RED+"		MISSION BRIEFING\n Good work on your last mission. But I am afraid it is not going to be that easy anymore.\n The assassination of subject EXX-244 has caught a lot of unwanted attention.\n Though the United States has not been found out, we cannot have suspicion grow in those in direct contact with powerful adversaries.\n Your next mission is to execute subject EXX-438.\nEXX-438:'Dimitry Marvol' is a weapons manafacturer, and develops knockoff AR-15's and Desert Eagles for a private militia aimed at bringing down NATO forces.\nA recent intelligence report revealed that he is sanctoning a large stash of the firearms in an underground storeroom.\nWe believe he is becoming aware of the recent actions by the U.S. Government and is planning an attack\nIn order to disguise the transportation of the firearms, he is holding a large party in the mansion located above the storehouse.\nHe is unaware that we have been informed of this. Your job, is to be the cause of the unfortunate accident subject EXX-438 will have at the party.")
		print("You will be provided with transportation to the target site, but unlike the previous mission, we will not proved a weapon.")
		print("		PARAMETERS:\n")
		print("-Infiltrate the extravagance undetected\n")
		print("-Execute subject EXX-438 and disguise the cause of death\n")
		print("-Leave the premesis undetected and without suspicion")
		print("\nFailure to meet ANY of the above parameters will result in termination\n"+color.END)
		input("READ ^ Before you press Enter to continue...")
		slwreveal2("MISSION 2",.12)
		print("\nINPUT NUMBERS TO SELECT OPTIONS. DO NOT INPUT FULL SENTENCES.\n")
		container["suspicion"] = 0
		print("INCORRECT ACTIONS OR RESPONSES MIGHT RAISE SUSPICION. TOO MUCH WILL MAKE YOU FAIL.\n")
		print("You are transported to the party.")
		print("You are dressed up for the occasion in order to blend in more.\n")
		if gender == "m" or gender == "male" or gender == "other":
			time.sleep(1)
			print("You are wearing a black suit with a red tie.\n")
		elif gender == "f" or gender == "female":
			time.sleep(1)
			print("You are wearing a red evening gown.")
		print("You walk along the front yard.\nFountains bursting.\nLigths glimmering.\nNo one aware of your malicious intentions.")
		print("Around a hundred people are walking towards the building, talking with eachother.\n")
		print("You enter the mansion, trying not to attract any attention.\nPeople are talking and drinking, almost unsettling how the lot of them don't even know why the party is even being thrown.\n")
		print("You decide it most effective to wait until the party is in full swing. \nPeople will be less expecting of an attack then.")
		input("Press enter to continue...")
		print("You must remain unnoticed unti-\n")
		time.sleep(1)
		if gender == "m" or gender == "male" or gender == "other":
			timeline="modern CH1 m"
			print("'Hello good sir, I am not sure that I have seen you here before!'\n")
			time.sleep(1)
			print("You are enraged by how quickly you were approached, and by the audacity of the man who came up to you to inquire.\n")
			print("A man in a dark blue suit stands infront of you.\nHe is seemingly of around 40 years, with white and black streaked hair. \nYou notice a strange gold pin on his suit. A triangle with an upside-down cross in the center.")
			print("Respond:\n1-'I just recently met Dimirty, and he insisted I attend this party.'\n2-'I don't want to talk now, leave me alone.'\n3-'I was invited by an unknown sender.'\n4-'I was sent to kill Dimitry'\n5-'I'm a traveler and I happened to just wander in.'\n")
			Person1whoru=cleanup(input("> "))
			if Person1whoru == str(1):
				print("'Oh so you know Dimirty! Charming young man isn't he? I've known the man for years!\n")
				print("What did you think of his ridiculous outfit?!")
				print("Respond:\n1-'I don't quite remember what he was wearing.'\n2-'If I remember correctly, wasn't he just wearing a normal suit?'\n3-'Haha, yeah it was crazy!'\n4-'I'm here to kill Dimirty.'")
				Person1whoru2=cleanup(input("> "))
				if Person1whoru2 == str(1):
					print("'Well that's fine I guess...what exactly brings you here?'\n")
					print("The man rearranges his tie, picks up a glass from a nearby table, and puts his hand in his pocket.\n")
					print("Respond:\n")
					input("> ")
					time.sleep(1)
					print("'Yes, I bet you are.'\n")
					time.sleep(1)
					print("The man begins to act disingenuously. \nHe starts fumbling with something in his pocket. You begin to panick inside.")
					print("'I must ask, what is Dimitry's hair color?'\n")
					print("Respond:\n1-Blonde\n2-Black\n3-Bald\n4-Dark Brown")
					Person1whoru3=cleanup(input("> "))
					slwreveal2("Ah I see. . .",.5)
					if str(3) in Person1whoru3:
						print("'Well it was a pleasure meeting you my good sir. Have a nice day.'\n")
						time.sleep(1)
						timeline += " none"
					else:
						print("You see him clench his fist in his pocket.\n")
						time.sleep(1)
						print("'Security!'\n")
						print("Mission 2 failed")
						timeline = "modern CH1 fail"
				elif Person1whoru2 == str(2):
					print("'Quite right my boy! I was testing if you actually met him or not! I had a feeling that you weren't exactly supposed to be here.\nMy apologies old sport, when you're my age you sometimes see things and meet people you wish you hadn't. And that eventually gets the best of you!.'\n")
					time.sleep(1)
					print("'I met Dimitry when the war was ripe! The man could always drive a bargain, every single time he could talk me into sparing one more grand! But one thing is for sure, he never dissapointed!'")
					print("Respond:\n1-'From what I've known, he sells...firearms. What exactly did you buy those for?'\n2-'From what I've seen, he is a heck of a guy!'")
					Person1whoru4=cleanup(input("> "))
					if Person1whoru4 == str(1):
						print("'....It is rude to stick ones nose in anothers business. But if you really must know, meet me in the east lounge room later tonight. Second door on the left of the second floor.'")
						timeline += " tony"
					if Person1whoru4 == str(2):
						print("'Yes yes! Quite! Well, I could use another martini. It was a pleasure meeting you, you enjoy yourself now!'")
						time.sleep(1.5)
						print("Well done!")
						timeline += " none"
				elif Person1whoru2 == str(3):
					print("'Sure...sure it was.'\n")
					print("'Security!'\n")
					print("Mission 2 failed")
					timeline = "modern CH1 fail"
				elif Person1whoru2 == str(4):
					print("Seriously?")
					timeline="DEAD"

			elif Person1whoru == str(2):
				print("'Well that's no way to talk, young man!'\n He walks away, but you have a feeling that this was a mistake.")
				timeline += " enemy"
			elif Person1whoru == str(3):
				print("'You were? Oddly typical of many of the people here. I apologize for the late introduction, my name is Tony Bethel. I'm from Costa Rica.'")
				print("You responded:'Nice to meet you Mr. Bethel, my name is Arthur Brigham. I am not sure why he wanted me here, but I am enjoying myself either way!\n If you don't mind, I had a lot to drink and am in no condition to converse.'")
				print("'Oh that's just fine my boy, I intend to figure out why so many have been invited for no reason. In the meantime, you have yourself a good time!'\n")
				time.sleep(1.5)
				print("Well done!")
				timeline += " none"
			elif Person1whoru == str(4):
				slwreveal2(". . .\n",.5)
				print("What is wrong with you?")
				time.sleep(1.5)
				timeline="DEAD"
			elif Person1whoru == str(5):
				print("'Well then I reckon that you are not supposed to be here.\nMight I ask you politely to leave?'\n")
				print("You raised suspicion")
				container["suspicion"] += 1
				print("You leave the party, and proceed to inspect the outside of the building.\n")
				timeline += " out"
		if timeline == "modern CH1 m none" or timeline == "modern CH1 m tony" or timeline == "modern CH1 m enemy":
			input("Press Enter to Continue...")
			print("You continue to walk about the parlor. That man bothers you a lttle.\nYou shrug it off and continue the mission.\nYou figure that the party is still adolescent, and you need to give it more time.\nObviously the most important task at hand is figuring out how to kill him, and where to find him.")
			print("You decide to find a group of people to talk to, in order to discover Marvol's whereabouts.\n")
			print("You spy 2 women sitting at a table, you grab yourself a drink and sit across from them.\n")
			time.sleep(1)
			print("'How are you two ladies?'\n")
			time.sleep(1)
			print("The woman on the left is wearing a long green dress, with red hair.\nThe woman on the right was wearing a red dress with blond hair.\n")
			time.sleep(1)
			print("'Party's booming huh?'")
			print("WOMAN RIGHT:'Yeah sure, if you're one that fancies crowds.'")
			print("'You aren't?'")
			print("WOMAN LEFT: 'I am! (turns to her friend) Sheryl, be nice.'")
			print("'Oh, forgive me, I'm Simon Jones. And who do I have the pleasure of meeting? Sherly and...?'\n")
			print("WOMAN LEFT: 'I'm Jenna.'")
			print("'Nice to make your acquaintence. I'm looking for Dimitry himself. Do you know where I can find him?'")
			print("'WOMAN RIGHT: 'I'm sorry, we don't. But why are you looking for him?'")
			print("Respond:\n1-'He asked me to find him during the party.'\n2-'I've never been able to meet the host of the party! I am always one to pay my respects!'\n3-'Imma kill him'\n")
			Person2whoru1=cleanup(input("> "))
			if Person2whoru1==str(1):
				print("Both women look at you sternly.\n")
				time.sleep(1)
				print("WOMAN RIGHT:'He is very particular about the guests that he wants to see him. You would've been told where to go if he told you so, would he not?'\n")
				print("WOMAN LEFT:'Honey, why do REALLY want to meet him?'")
				print("Respond:\n1-'I really wanted to meet him, and I thought pretending like I was invited to meet him would help.'\n2-'He's an old friend of mine'\n")
				Person2whoru2=cleanup(input("> "))
				if Person2whoru2==str(1):
					print("'WOMAN RIGHT: 'You're kinda pathetic'\n")
					print("The women refuse to tell you where he is.")
					print("You raised suspicion")
					container["suspicion"] += 1
					timeline += " route"
				elif Person2whoru2==str(2):
					print("WOMAN LEFT: 'Oh you know Dimitry?! That's amazing!\nWe come to his parties, but we've never actually met him. He usually hangs out in his private lounge upstairs. The only time he ever comes out is to go"+color.BOLD+" outside "+color.END+" for whatever reason.'\n")
					print("\nWOMAN RIGHT:'Jenna, you shouldn't say things you are not sure of.'\nWOMAN LEFT:'But I do know!....I think.'\nWOMAN RIGHT:'Either way, it was nice meeting you...Simon.\n")
					print("You walk away.")
					timeline += " route"
			elif Person2whoru1==str(2):
				print("WOMAN LEFT:'You don't come to these often do ya? No one usually gets to see him. He usually hangs out in his private lounge upstairs.\n Only his closest friends get in there!-\nWOMAN RIGHT:'JENNA!! Will you quiet down?!'\n")
				print("'That's all I needed, thank you ladies.'\n")
				print("You walk away.")
				timeline += " route"
			elif Person2whoru1==str(3):
				print("You know I give the option because I'm bored, I never really expect anyone to select it.\n")
				print("Let me see if you can guess what happens if you hit 'Enter'")
				input("Press Enter to Continue...")
				timeline="DEAD"
			if "route" in timeline:
				print("You wander around the palor a little more.")
				print("The party is bursting, You decide that its time for you move.\n")
				print("1-Explore mansion for other options\n")
				print("2-Head outside\n")
				print("3-Head to private lounge upstairs\n")
				move=cleanup(input("> "))
				if move==str(1):
					print("You decide that you need more places to explore.")
					timeline += " explore"
				elif move==str(2):
					timeline += " out"
				elif move==str(3):
					print("You are unable to go there without special clearance.\n")
					time.sleep(1)
					print("Explore for a way to gain access")
					input("Press Enter to Continue...")
					timeline += " explore"
		if " out" in timeline:
			print("You walk outside the mansion. You proceed to slip around the gardens and courtyard.")
			print("You see two workers unloading crates from a truck.")
			print("1-Wait by truck\n2-Follow men\n")
			truck=cleanup(input("> "))
			if truck == str(1):
				print("You sneak by the outside of the truck.\n")
				time.sleep(1)
				print("You wait.\n")
				time.sleep(1)
				print("And wait.\n")
				time.sleep(1)
				print("And then you hear them walking back.")
				print("What do you do?\n")
				print("\n1-Attack closest man, then farthest\n2-Attack farthest man then closest")
				twomen=cleanup(input("> "))
				if twomen == str(1):
					print("You walk up to the other side of the truck, and slam the first mans head into the truck. HARD. Then you flipped him over your hip.\nHe lands hard on the ground. You drop two quick punches on his face.\nHe knocks out cold.")
					time.sleep(2)
					print("You quickly look up for the second man...")
					time.sleep(2)
					print("...who ran away in order to alert guards.")
					timeline="modern CH1 fail"
				elif twomen == str(2):
					print("You realized that you need to act quick.\nYou grab a nearby stone, and you rush the farther man from behind.\nYou smash the back of his head. He falls to the floor, unconscious and bleeding. You turn to the second man, and-\nFALCON PUNCH HIM IN THE FACE!")
					time.sleep(3)
					print("....it didn't really do much.")
					print("He rushes you")
					input("Press Enter to Continue...")
					print("\nFALCON PUNCH!\n")
					print("He smashes into the ground.")
					time.sleep(3)
					print("Hmm....he twitched...just in case...")
					input("Press Enter to Continue...")
					print("\nFALCON PUNCH!\n")
					container["FALCON PUNCH"]=5
					print("You dispose of the bodies in the back of the truck.")
					print("Put on worker disguise?")
					clothe1=cleanup(input("Yes or No?> "))
					if clothe1 == "yes":
						timeline += " worker"
			if "fail" not in timeline:
				print("You walk towards a door along the side of the mansion.")
				print("Inside is a staircase leading down stairs into a room that can only be accessed through a staircase with stairs and maybe a back door that has a staircase with stairs leading upstairs.")
				print("You cautiously head down...stairs...into the room.")
				print("The room is very large with hundreds of crates lined in rows along the edges.")
				print("You decide to open up one of the crates.")
				input("Press Enter to Continue...")
				print("Inside the crate were the knockoff assault rifles mentioned in the briefing.")
				sack += ["AR-15"]
				time.sleep(1)
				print("\n		An "+color.BOLD+"AR-15"+color.END+" has been added to your inventory.")
				print("\n		You have: "+" ".join(sack)+", in your inventory.\n")
				input("Press Enter to Continue...")
				print("You attempt to leave the store house, two guards approach.")
				time.sleep(1)
				print("\n'Hey! Who's there?! What are you doing?!'\n")
				print("You need to act fast.\n")
				print("1-Run\n2-Hide\n3-OPEN FIRE WITH AR-15!")
				if "Sniper" in sack:
					print("4-OPEN FIRE WITH SNIPER!")
				if "worker" in timeline:
					print("5-Use disguise to pretend to be worker")
				twomen2=cleanup(input("> "))
				if twomen2==str(1):
					print("There is no way out of the room EXCEPT for the stair case they came from, you were caught.")
					print("\nMission 2 failed")
					timeline = "modern CH1 fail"
				elif twomen2==str(2):
					print(".....They already saw you, you were caught.")
					print("\nMission 2 failed")
					timeline = "modern CH1 fail"
				elif twomen2==str(3):
					slwreveal2("*CLICK*\n",.001)
					time.sleep(2)
					print("*CLICK*\n")
					time.sleep(.1)
					print("*CLICK*\n")
					time.sleep(.1)
					print("*CLICK*\n")
					time.sleep(.1)
					print("*CLICK*\n")
					time.sleep(.1)
					print("*CLICK*\n")
					time.sleep(2)
					print("Fun fact: Guns work better with ammo.")
					print("\nMission 2 failed")
					timeline = "modern CH1 fail"
				elif twomen2==str(4):
					shotz=random.randrange(5)
					print(shotz)
					if shotz >=3:
						print("\nBy some miracle, you killed both guards.\n")
						print("PLAYER NOTE: shot NOT heard from storehouse,\nBUT IN FUTURE SITUATIONS YOU WILL BE HEARD DURING STEALTH MISSIONS UNLESS YOU OBTAIN A SILENCER\n")
						container["srounds"]-=shotz
						print(container)
					else:
						print("\nAttempt unsuccessful, either one or both of guards not killed.")
						print("\nMission 2 failed")
						timeline = "modern CH1 fail"
				elif twomen2==str(5):
					print("'I'm just unloading the truck outside.'")
					print("MAN LEFT: 'Oh okay, we heard a lot of noise coming from here.'")
					print("'I knocked over a bunch of crates, and I've been restacking them before I continue.'")
					print("MAN LEFT: 'Ah gotcha, we're going to be patroling the east wing under order of Mr. Marvol to protect Mr. Bethel.\nUnless you want a bullet through your skull, I suggest you join us after you finish up here.'")
					print("'Thank you for telling me, I would've lost my head.'")
					print("\nWell Done!\n")
					print("REMEMBER TO DISPOSE OF THOSE TWO GUARDS AFTER TARGET IS KILLED.\nTHEY WILL EXPECT YOUR ARRIVAL, AND IF YOU ARE NOT PRESENT YOU WILL BE SUSPECTED WHEN TARGET IS KILLED.")
				if "fail" not in timeline:
					print("You head out of the storeroom.")
					print("*IMPORTANT DECISION*")
					print("\n1-Continue looking outside.\n2-Head to parlor.\n")
					move2=cleanup(input("> "))
					if move2 == str(1):
						print("You continue looking for an attack point from the outside.\n")
						print("You scope the back of the house. You can see into some of the larger rooms through their windows. You notice a praticular window that is lit up and rowdy.")
						timeline += " sneak"
					elif move2 == str(2):
						print("You head back to the parlor.")
						timeline += " poison"
		if " explore" in timeline:
			print("Not satisfied with your other ideas, you decide to find a new one.")
			print("It is possible that you can find another way to subdue Dimitry by looking around.")
			print("You start by walking upstairs. There are two large hallways leading in opposite directions.")
			print("Because you already know about Tony's room and Dimitry's lounge on the left, you head towards the right hall.")
			print("You start checking doors.")
			while True:
				print("\n1-Door Left 1\n2-Door Right 1\n3-Door Left 2\n4-Door Right 2\n5-Door Left 3\n6-Door Right 3")
				doorz=int(cleanup(input("> ")))
				if doorz == 1:
					print("You walk into a bedroom. Bed, window, bathroom, the likes.")
					print("Probably best to leave. Would you like to search the room?\n")
					yn=cleanup(input("Yes or No > "))
					if yn == "yes":
						print("You sneak into the room, like a creep, and start going through all the drawers and furniture for something usefull.")
						time.sleep(2)
						print("\nYou find nothing\n")
						input("Press Enter to Continue...")
					else:
						input("Press Enter to Continue...")
				elif doorz == 2:
					print("\nDoor is locked.\n")
					if "Keys" in sack:
						print("Keys didn't work.\n")
					input("Press Enter to Continue...")
				elif doorz == 3:
					print("Its a janitor's closet?...Go in?")
					yn=cleanup(input("Yes or No > "))
					if yn == "yes":
						print("You step into the closet...")
						time.sleep(2)
						print("\nThere is a bucket on the ground...")
						print("Put it on your head?")
						yn=cleanup(input("\nYes or No > "))
						if yn == "yes":
							print("\nYou put the bucket on your head...")
							time.sleep(2)
							print("\nLeave?...")
							yn=cleanup(input("\nYes or No > "))
							if yn == "no":
								time.sleep(2)
								print("\nLeave?...")
								yn=cleanup(input("Yes or No > "))
								if yn == "no":
									time.sleep(2)
									print("\nLeave?...")
									yn=cleanup(input("Yes or No > "))
									if yn == "no":
										time.sleep()
										print("\n. . .")
										time.sleep(8)
										slwreveal2(". . .\n",.5)
										print("This is your fault...\n")
										time.sleep(8)
										print("I gave you the chance...\n")
										time.sleep(8)
										print("Bet you're regretting your decision now huh?\n")
										time.sleep(8)
										input("Press to Continue..")
										print("PSYCH!")
										time.sleep(8)
										print("Ah alright..\n")
										input("Press to Continue..")
									else:
										input("Press Enter to Continue...")
								else:
									input("Press Enter to Continue...")
							else:
								input("Press Enter to Continue...")
						else:
							input("Press Enter to Continue...")
					else:
						input("Press Enter to Continue...")
				elif doorz == 4:
					print("You come across a lounge area, empty at the moment.")
					print("Probably best to leave. Would you like to search the room?")
					yn=cleanup(input("Yes or No > "))
					if yn == "yes":
						print("You enter the lounge area. There are couches, a fireplace, and a pool table.")
						print("You start looking for things that spark interest, there is a desk next to the fireplace.")
						print("You start searching the drawers in the desk.")
						if "Cards" not in sack:
							time.sleep(2)
							print("Cards...")
							print("Take?")
							yn=cleanup(input("Yes or No > "))
							if yn == "yes":
								sack += ["Cards"]
								time.sleep(1)
								print("\n		A "+color.BOLD+"CARDS"+color.END+" has been added to your inventory.")
								print("\n		You have: "+" ".join(sack)+", in your inventory.\n")
								input("Press Enter to Continue...")
						if "1911" not in sack:
							time.sleep(2)
							print("\nColt 1911 .45 CAL (ACP) with some bullets...")
							print("Take?")
							yn=cleanup(input("Yes or No > "))
							if yn == "yes":
								sack += ["1911"]
								container["hrounds"] = 21
								time.sleep(1)
								print("\n		A "+color.BOLD+"1911"+color.END+" has been added to your inventory.")
								print("\n		You have: "+" ".join(sack)+", in your inventory.\n")
								print("\n		You have: "+str(container)+" in your container.\n")
								input("Press Enter to Continue...")
						if "Keys" not in sack:
							time.sleep(2)
							print("\nKeys...")
							print("Take?")
							yn=cleanup(input("Yes or No > "))
							if yn == "yes":
								sack += ["Keys"]
								time.sleep(1)
								print("\n		A "+color.BOLD+"KEYS"+color.END+" has been added to your inventory.")
								print("\n		You have: "+" ".join(sack)+", in your inventory.\n")
								input("Press Enter to Continue...")
						time.sleep(1)
						print("\nYou find nothing else\n")
						input("Press Enter to Continue...")
						print("\nSuddenly, a few staff members walk into the room...\n")
							#subdue members to get clearace to  lounge also learn favorite drink# possible suspicion raise
					else:
						input("Press Enter to Continue...")
				elif doorz == 5: #CREATE ELABORATE STORY LATER
					print("You walk into a bedroom. Bed, window, bathroom, the likes.")
					slwreveal2(". . .",.5)
					print("\nThere is a small goat just sitting in the middle of the main room.\n")
					print("Probably best to leave. Would you still like to search the room?")
					yn=cleanup(input("Yes or No > "))
					if yn == "yes":
						print("You sneak into the room and start going through all the drawers and furniture for something usefull.")
						time.sleep(2)
						print("\nYou find a broken locket and put it back.")
						input("Press Enter to Continue...")
					else:
						input("Press Enter to Continue...")
				elif doorz == 6:
					timeline += " poison"
					break
		if " poison" in timeline:
			print("You find a small, dark staircase going down into a basement of some sort.")
			#basement has bleach and ammonia. mix both with whiskey to kill
			print("Downstairs, you see another long hallway. Through the door on the left, you see there is a small laundry room.")
			print("You walk in to find your typical cleaning supplies and a long line of washers and dryers.")
			while True:
				print("\n1-Search cleaning supplies")
				if " out" not in timeline:
					print("\n2-Search washers and dryers.")
				lawndree=cleanup(input("> "))
				if lawndree == str(2):
					if " waitor" not in timeline:
						print("In one of the dryers, you find a waitors outfit.")
						print("Put on waitor disguise?")
						clothe1=cleanup(input("Yes or No?> "))
						if clothe1 == "yes":
							timeline += " waitor"
					input("Press Enter to continue...")
				elif lawndree == str(1):
					print("You find a wide assortment of cleaning products: ")
					while True:
						if "Air Freshener" not in sack:
							print("Air Freshener?...")
							print("Take?")
							yn=cleanup(input("Yes or No > "))
							if yn == "yes":
								sack += ["Air Freshener"]
								time.sleep(1)
								print("\n		You have: "+" ".join(sack)+", in your inventory.\n")
								input("Press Enter to Continue...")
						if "Ammonia" not in sack:
							print("Ammonia...")
							print("Take?")
							yn=cleanup(input("Yes or No > "))
							if yn == "yes":
								sack += ["Ammonia"]
								time.sleep(1)
								print("\n		You have: "+" ".join(sack)+", in your inventory.\n")
								input("Press Enter to Continue...")
						if "Bleach" not in sack:
							print("Bleach...")
							print("Take?")
							yn=cleanup(input("Yes or No > "))
							if yn == "yes":
								sack += ["Bleach"]
								time.sleep(1)
								print("\n		You have: "+" ".join(sack)+", in your inventory.\n")
								input("Press Enter to Continue...")
						if "Disinfectant Wipes" not in sack:
							print("Disinfectant Wipes...")
							print("Take?")
							yn=cleanup(input("Yes or No > "))
							if yn == "yes":
								sack += ["Disinfectant Wipes"]
								time.sleep(1)
								print("\n		You have: "+" ".join(sack)+", in your inventory.\n")
								input("Press Enter to Continue...")
						print("Keep looking?")
						yn=cleanup(input("Yes or No?> "))
						if yn == "yes":
							input("Press Enter to Continue...")
						elif yn == "no":
							break
					break
			if "Bleach" in sack and "Ammonia" in sack:
				print("You mixed the "+color.BOLD+"BLEACH"+color.END+" and the "+color.BOLD+"AMMONIA"+color.END+" together, and kept the concoction in a small bottle.")
				print("Enough to do a lot of harm.")
				sack.remove("Bleach")
				sack.remove("Ammonia")
				sack += ["Drug"]
				print("\n		You have: "+" ".join(sack)+", in your inventory.\n")
				input("Press Enter to Continue...")
			print("\n*IMPORTANT DECISION*")
			print("\n1-Head to kitchen")
			if " keycard" in sack:
				print("\n2-Head to private lounge")
			if " tony" in timeline:
				print("\n3-Head to the room Tony spoke of")
			move4=cleanup(input("> "))
			if move4 == str(1):
				print("You decided to go to the kitchen area of the mansion.")
				if " worker" in timeline or " waitor" in timeline:
					print("You walk into the kitchen area.")
				else:
					print("You walk into the kitchen area.")
					print("You are not suppossed to be here.")
					print("You raised suspicion.")
					container["suspicion"] += 1
				print("You see other waitors bringing alcohol from a cellar in the back.")
				print("You walk into the cellar, and see many different alcoholic drinks.")
				input("Press Enter to Continue...\n")
				if "Drug" in sack:
					print("You decide that you want to place the poison in a beverage.")
					print("Which beverage do you dump the poison?")
					print("\n1-Beer\n2-")# do research
				else:
					print("What...what are you doing?")
					#fix


			elif move4 == str(2):
				print("You try to go to the private lounge.")
				print("\nYou show your keycard to the guards by the door.")
				time.sleep(3)
				print("\nThey let you in.")
				if " worker" in timeline:
					print("A worker is not suppossed to have clearance in the private lounge.")
					print("You raised suspicion")
					container["suspicion"] += 1
				if " waitor" in timeline:
					print("In order to act naturally with your waitor suit on, you head to the bar.")


			elif move4 == str(3):
				print("Eh...") # finish later



if timeline == "DEAD":
	slwreveal2("GAME OVER",.12)
	time.sleep(1)
	print("YOU LOSE\n"*500)
	sys.exit()

if timeline == "medieval ":
	print("Not done yet")
if timeline == "ancient ":
	print("Not done yet")
if timeline == "future ":
	print("Not done yet")
