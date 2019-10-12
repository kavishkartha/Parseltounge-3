import random

stringList = ["ape", "supreme", "white", "air", "champion"]
guessCount = 10
randomString = random.choice(stringList)

def randomStrSplit(randomStr):
    return [ch for ch in randomStr]

randomStringSplit = randomStrSplit(randomString)
print("The secret word begins with the letter " + randomStringSplit[0])
print("GUESS: ")
userGuess = input()
userGuessSplit = randomStrSplit(userGuess)
userGuessLen = len(userGuessSplit)
