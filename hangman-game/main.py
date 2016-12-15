import random
from random import randint
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

chances = 11
right = 0
points = 0
underScores = ""

questions = ["In what year was Python created?","How do you combine rows in SQL?","What does <div> stand for?","Who invented HTML?","How many characters does the ASCII standard contain?","What is error code 502?"]
queries = ["1989", "JOINS", "DIVISION", "TIM BERNERS LEE", "128", "BAD GATEWAY", "DELETE", "DESC", "ASC", "UPDATE", "JOINS", "BETWEEN", "UPDATE", "PRIMARY_KEY"]
usedLetters = []

while True:
	cls()
	#select random int to select query from array
	questionNum = randint(0,len(queries)-1)
	#get character count from selected query
	for i in range(len(queries[questionNum])):
		#add underscores in ammount of characters
		underScores += "_"
	#check if you have enough chance to go further
	while chances>0:
		#display the ammount of chances left
		print("Chances: " + str(chances))
		#display the used letters
		print('Used letters: '+', '.join(usedLetters))
		#display the ammount of points 
		print(str(points)+" Points ")
		#store the user input in a variable
		user_input = input(underScores+"\n")
		#check if user input is not longer than 1 character
		if len(user_input) == 1:
			#check if letter is used once in the query
			if user_input in usedLetters:
				print("Already used this letter")
			else:
				#check if query contains user input
				if user_input in queries[questionNum]:

					#get position of the letter in the query
					positions = findOccurences(queries[questionNum], user_input)

					for position in positions:
						underScores = underScores[:position] + user_input + underScores[position + 1:]
						#underScores = underScores.replace(underScores[position], user_input)
						right+=1
					
					print("Thats right right:" + str(right))
					
					#add this letter to used
					usedLetters.append(user_input)
					#check if whole query is guessed
					if right == len(queries[questionNum]):
						#clear underscores
						underScores = ""
						#clear right answers variable
						right = 0
						#clear used letter list
						del usedLetters[:]
						break
					else:
						user_input = ""
						continue
				else:
					#querydoes not contain letter
					#add this letter to used
					usedLetters.append(user_input)
					#reset user input
					user_input = ""
					#decrease the chances variable
					chances-=1
					continue
		else:
			#input is longer than 1

			#check if input is the correct query
			if user_input == queries[questionNum]:
				right = 0
				del usedLetters[:]
				underScores = ""
				break
			else:
				chances = 0
				break

	if chances == 0:
		#lost no point is rewarded
		print("""\

                                           _________
                                           |         |
                                           |         0 R I P
                                           |        /|\
                                           |        / \
                                           |
                                           |
                    """)
		break
	else:
		#you've won a point is rewarded
		points+=1
		continue
