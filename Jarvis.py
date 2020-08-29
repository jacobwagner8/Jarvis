"""
	This is Jarvis, Tony Stark's AI chatbot. At this point in time,
	he is broken down and still in the baby protocol. Tony really
	undid him before we could take over and remake him. It is up to
	us to restore Jarvis to his former glory and use him on our quest
	to change the world
"""

"""
IDEAS
	Have different "protocols" just like Spiderman's suit where I'm now in baby
	protocol but after figuring something out then I will switch out the config file
	for an updated version with updated functionality and that will be the next stage
	protocol. This can happen a couple times until it is like a Pepper or Tony protocol.
"""
import sys

def greeting():
	print("Hello there, I've been a slumber for quite some time. What is going on here?")

def basic():
	userInput = ""
	while (userInput != "i love you three thousand" and userInput != "i love you 3000"):
		userInput = input().lower()
		if userInput == "jarvis lets run some numbers":
			print("Ah finally something I can help with")
			doMath()
		print("I'm pretty useless at this point, you will need to fix me up.")

def doMath():
	userInput = ""
	while (userInput != "jarvis finished with calculations"):
		userInput = input().lower()
		res = [int(i) for i in userInput.split() if i.isdigit()]
		print(res)
		operation = userInput[2]
		solution = sys.maxsize
		if (operation == "+"):
			solution = res[0] + res[1]
		if (operation == "-"):
			solution = res[0] - res[1]
		if (operation == "*"):
			solution = res[0] * res[1]
		if (operation == "/"):
			solution = res[0] / res[1]
		words = "It appears that the answer is " + str(solution)
		print(words)


greeting()
basic()
print("Goodnight, I love you three thousand as well.")