import time
import pyfiglet


""" saved this for future Windows Version
def menu():
    print("\033[1m[1] Train\n[2] Delete a Word\n[3] Create a new Word\n[4] Quit")
    option = str(input("Which Option do you choose: "))
    if option == "1" or option == "2" or option == "3" or option == "4":
        if option == "1":
            Libary.train()    
        elif option == "2":
            pass
        elif option == "3":
            Libary.createNewWord()
        elif option == "4":
            Libary.Exit()
def Exit():
    print("\033[?25h")
    print("\033[2J")
    print("\033[H")
    print("Exiting now.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    exit()
"""

def createNewWord():
    word = str(input("Enter a Word: "))
    definition = str(input("Enter a definition: "))
    file = open("LibaryAndStorage/Words", "a")
    file.write(f"{textToBinary(word)}\n{textToBinary(definition)}\n")
    return input("Enter again to go back to menu")

def train():
    terms = splitLines(openFileAndSplitLines("LibaryAndStorage/Words"))[0]
    definitions = splitLines(openFileAndSplitLines("LibaryAndStorage/Words"))[1]
    number = input(f"Which word do you want? You can choose from {len(terms)} Word(s): ")
    try:
        number = int(number)
    except:
        exit()
    for i in range(len(terms)+1):
        if i == number:
            print(terms[i-1])
            question = input("Press Enter if you want to hear the definition")
            print(definitions[i-1])
            return input("Enter again to go back to menu")



def openFileAndSplitLines(path):
    file = open(path, "r")
    return file.read().splitlines()

def splitLines(lines):
    counter = 0
    wordCounter = 0
    terms = []
    definitions = []
    upperBorderRange = int(len(lines)/2)
    for i in range(0,upperBorderRange):
        terms.append(binaryToText(lines[counter]))
        definitions.append(binaryToText(lines[counter+1]))
        counter+= 2
        wordCounter += 1
    return terms, definitions

def textToBinary(text):
    return " ".join(format(ord(c), "b") for c in text)
    
def binaryToText(binary):
    return "".join(chr(int(c, 2)) for c in binary.split(" "))