import random

statesList = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

randomState = random.choice(statesList)
capitolsList = ["Montogomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "Saint Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]

capitol = ""

if randomState == statesList[0]:
    capitol = capitolsList[0]
if randomState == statesList[1]:
    capitol = capitolsList[1]
if randomState == statesList[2]:
    capitol = capitolsList[2]
if randomState == statesList[3]:
    capitol = capitolsList[3]
if randomState == statesList[4]:
    capitol = capitolsList[4]
if randomState == statesList[5]:
    capitol = capitolsList[5]
if randomState == statesList[6]:
    capitol = capitolsList[6]
if randomState == statesList[7]:
    capitol = capitolsList[7]
if randomState == statesList[8]:
    capitol = capitolsList[8]
if randomState == statesList[9]:
    capitol = capitolsList[9]
if randomState == statesList[10]:
    capitol = capitolsList[10]
if randomState == statesList[11]:
    capitol = capitolsList[11]
if randomState == statesList[12]:
    capitol = capitolsList[12]
if randomState == statesList[13]:
    capitol = capitolsList[13]
if randomState == statesList[14]:
    capitol = capitolsList[14]
if randomState == statesList[15]:
    capitol = capitolsList[15]
if randomState == statesList[16]:
    capitol = capitolsList[16]
if randomState == statesList[17]:
    capitol = capitolsList[17]
if randomState == statesList[18]:
    capitol = capitolsList[18]
if randomState == statesList[19]:
    capitol = capitolsList[19]
if randomState == statesList[20]:
    capitol = capitolsList[20]
if randomState == statesList[21]:
    capitol = capitolsList[22]
if randomState == statesList[23]:
    capitol = capitolsList[23]
if randomState == statesList[24]:
    capitol = capitolsList[24]
if randomState == statesList[25]:
    capitol = capitolsList[25]
if randomState == statesList[26]:
    capitol = capitolsList[26]
if randomState == statesList[27]:
    capitol = capitolsList[27]
if randomState == statesList[28]:
    capitol = capitolsList[28]
if randomState == statesList[29]:
    capitol = capitolsList[29]
if randomState == statesList[30]:
    capitol = capitolsList[30]
if randomState == statesList[31]:
    capitol = capitolsList[31]
if randomState == statesList[32]:
    capitol = capitolsList[32]
if randomState == statesList[33]:
    capitol = capitolsList[33]
if randomState == statesList[34]:
    capitol = capitolsList[34]
if randomState == statesList[35]:
    capitol = capitolsList[35]
if randomState == statesList[36]:
    capitol = capitolsList[36]
if randomState == statesList[37]:
    capitol = capitolsList[37]
if randomState == statesList[38]:
    capitol = capitolsList[38]
if randomState == statesList[39]:
    capitol = capitolsList[39]
if randomState == statesList[40]:
    capitol = capitolsList[40]
if randomState == statesList[41]:
    capitol = capitolsList[41]
if randomState == statesList[42]:
    capitol = capitolsList[42]
if randomState == statesList[43]:
    capitol = capitolsList[43]
if randomState == statesList[44]:
    capitol = capitolsList[44]
if randomState == statesList[45]:
    capitol = capitolsList[45]
if randomState == statesList[46]:
    capitol = capitolsList[46]
if randomState == statesList[47]:
    capitol = capitolsList[47]
if randomState == statesList[48]:
    capitol = capitolsList[48]
if randomState == statesList[49]:
    capitol = capitolsList[49]

print("Ready: " + randomState)
userGuess = input()
if userGuess == randomState:
    print("Done")
else:
    print("nil")
