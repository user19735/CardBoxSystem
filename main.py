import sys
sys.path.append("LibaryAndStorage")
from CardBoxLib import *

if __name__ == "__main__":
    
    if(sys.argv[1] == "-t" or sys.argv[1] == "--train"):
        train()
    elif(sys.argv[1] == "-dw" or sys.argv[1] == "--deleteWord"):
        print("Function does not work yet.")
        nothing = input("Press Enter to go back to menu")
    elif(sys.argv[1] == "-cw" or sys.argv[1] == "--createWord"):
        createNewWord()
    elif(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        #placeholder for future --help or -h Feature
        pass