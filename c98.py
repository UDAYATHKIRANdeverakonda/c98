

f = open("text.txt")


f = open("text.txt")
fileLines = f.readlines()

for line in fileLines:
    print(line)

introString = "My name is Udayathkiran. I like to play cricket,chess,study and code."
words = introString.split(",")
print(words)




def greet(Name):
    print("Hello , " + Name + " How are you ?")

greet("Udayathkiran")