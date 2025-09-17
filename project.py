import random

capitalbeginner = ["USA WashingtonDC", "Russia Moscow", "Canada ", "China", "Japan", "Australia", "UK", "UAE", "New Zealand", "Mexico", "Brazil", "Italy", "Greece", "SouthKorea", "India", "Germany", "France", "Egypt", "Poland", "Hungary", "Thailand", "Finland", "Israel", "Spain", "Singapore", "NorthKorea", "Vietnam", "Nepal", "Norway", "Malaysia", "SaudiArabia", "Qatar", "Indonesia", "Afghanistan", "Ukraine", "Belgium", "Turkey", "Argentina", "Jamaica"]
capitaleasy = ["Belarus Minsk", "Austria Vienna", "Colombia Bogota"]
capitalmedium = []
capitalhard = []
capitalexpert = []

def help():
    print("\nTo start the program, type 'capital cities'.\nWhen you score 100 percent on a quiz, you collect a point.\nType 'progress' to view your quiz points.\n" )
    initiate()

def learn(difficulty):
    print("\nLets's get started! Type the capital city to move on to the next one.\n")
    #flashcard program goes here

def beginnerquiz():
    random.shuffle(capitalbeginner)
    points = []
    for item in capitalbeginner:
        question = item.split()
        print(question[0])
        answer = input("Answer: ")
        if answer == question [1]:
                points.append(1)
        continue
    result = sum(points)
    checkresult = sum(points) / len(capitaleasy) * 100

    if checkresult == 100:
        print("\nCongratulations! You scored 100 percent and earnt a progress point!\n")
    else: print("\nResult: " + str(result) + " out of 39. " + "Score 100 percent to earn a progress point!\n")

def quiz(easy):
    #print("")
    random.shuffle(capitaleasy)
    points = []
    for item in capitaleasy:
        question = item.split()
        print("\n" + question[0])
        answer = input("Answer: ")
        if answer == question [1]:
                points.append(1)
        continue
    result = sum(points)
    checkresult = sum(points) / len(capitaleasy) * 100

    if checkresult == 100:
        print("\nCongratulations! You scored 100 percent and earnt a progress point! \n")
    else: print(" \nResult: " + str(result) + " out of 39. " + "Score 100 percent to earn a progress point! \n" )


def mediumquiz():
    random.shuffle(capitalmedium)
    points = []
    for item in capitalmedium:
        question = item.split()
        print(question[0])
        answer = input("Answer: ")
        if answer == question [1]:
                points.append(1)
        continue
    result = sum(points)
    checkresult = sum(points) / len(capitaleasy) * 100

    if checkresult == 100:
        print("Congratulations! You scored 100 percent and earnt a progress point!")
    else: print("Result: " + str(result) + " out of 39." + "Score 100 percent to earn a progress point!" )
    
def hardquiz():
    random.shuffle(capitalhard)
    points = []
    for item in capitalhard:
        question = item.split()
        print(question[0])
        answer = input("Answer: ")
        if answer == question [1]:
                points.append(1)
        continue
    result = sum(points)
    checkresult = sum(points) / len(capitaleasy) * 100

    if checkresult == 100:
        print("Congratulations! You scored 100 percent and earnt a progress point!")
    else: print("Result: " + str(result) + " out of 39." + "Score 100 percent to earn a progress point!" )

def expertquiz():
    random.shuffle(capitalexpert)
    points = []
    for item in capitalexpert:
        question = item.split()
        print("\n", question[0])
        answer = input("Answer: ")
        if answer == question [1]:
                points.append(1)
        continue
    result = sum(points)
    checkresult = sum(points) / len(capitaleasy) * 100

    if checkresult == 100:
        print("Congratulations! You scored 100 percent and earnt a progress point!")
    else: print("Result: " + str(result) + " out of 39." + "Score 100 percent to earn a progress point!" )


def initiate():
    choice = input("What would you like to do? \n")
    if choice == "get help":
        help()
    if choice == "begin":
        difficulty = input("\nChoose a difficulty level: (beginner/easy/medium/hard/expert) \n")
        if difficulty == "beginner":
            beginnerquiz()
        elif difficulty == "easy":
            easyquiz()
        elif difficulty == "medium":
            mediumquiz()
        elif difficulty == "hard":
            hardquiz()
        elif difficulty == "expert":
            expertquiz()
        else: print("Invalid input, please try again. \n"); initiate()
    else: print("Invalid input, please try again. \n"); initiate()

#def progress():
#Needs to be figured out aaaa

print("\nWelcome to GeoRefiner.")
print("Type 'get help' to view available commands.\n")
initiate()
