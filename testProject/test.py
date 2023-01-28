#basic python experiment
import os

from stringModifier import capitalise

message = "Hello world"
print(message)

list1 = ["abc", 34, True, 40, "male"]
stringList = []
for value in list1:
    
    if type(value) == str:
        stringList.append(value)

print(stringList)
fullList = "full list: {}"
stringList.sort(key=str.lower, reverse=True )
print(fullList.format(list1))


txt=input("Enter text to save: \n") # inputed text from terminal


print(capitalise(txt))

if os.path.exists("testFile.txt") == False: #Checks existence of file
    f = open("testFile.txt", "x")
else:
    f = open("testFile.txt", "w")

f.write(txt)
f.close

print("Script finished")
