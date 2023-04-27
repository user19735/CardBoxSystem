import sys
sys.path.append("LibaryAndStorage")
from CardBoxLib import Libary


if __name__ == "__main__":
    
    if(sys.argv[1] == "-t" or sys.argv[1] == "--train"):
        Libary().train()
    elif(sys.argv[1] == "-dw" or sys.argv[1] == "--deleteWord"):
        print("Function is not implemented yet.")
        nothing = input("Press Enter to go back to the menu.")
    elif(sys.argv[1] == "-cw" or sys.argv[1] == "--createWord"):
        Libary().createNewWord()
    elif(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        #placeholder for future Feature
        pass