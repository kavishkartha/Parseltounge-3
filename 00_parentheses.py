newString = ''
userString = input("Please enter a string: ")
count = 1
userString = userString.lower()

for char in userString:
    if count % 2 == 0:
        newString += char.upper()
        count += 1
    else:
        newString += char
        count += 1
print(newString)

def splitStr(string):
    return [ch for ch in string]

newStringSplit = splitStr(newString)
newStringLen = len(newStringSplit)
newStringFinalChar = newStringLen - 1

if newStringSplit[0] == "(" and newStringSplit[newStringFinalChar] == ")":
    print("Balanced!")
else:
    print("Not Balanced!")
