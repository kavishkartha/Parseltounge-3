import random

stringList = ["black", "green", "white", "dough", "zebra"]
guessCount = 10
randomString = random.choice(stringList)

def randomStrSplit(randomStr):
    return [ch for ch in randomStr]

randomStringSplit = randomStrSplit(randomString)

while guessCount == 10:
    guessCount -= 1
    print("The secret word begins with the letter " + randomStringSplit[0] + " and is 5 letters long.")
    print("GUESS: ")
    userGuess = input()
    userGuessSplit = randomStrSplit(userGuess)
    userGuessLen = len(userGuessSplit)

    if userGuess == "":
        print("You wasted a guess =P")
    if userGuessLen > 5:
        print("0, 1, 2, 3, 4 that’s how we count to five!")
    if 1 <= userGuessLen < 5:
        print("0, 1, 2, 3, 4 that's how we count to five!")
    if userGuess == randomString:
        print("Good Job! You are one with the Source.")
    if userGuessSplit[0] == randomStringSplit[0]:
        print("You have " + str(guessCount) + " gueses left")
