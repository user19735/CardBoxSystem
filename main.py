import sys
sys.path.append("LibaryAndStorage")
from CardBoxLib import *

if __name__ == "__main__":
    deleteWord()
    if(sys.argv[1] == "-t" or sys.argv[1] == "--train"):
        train()
    elif(sys.argv[1] == "-dw" or sys.argv[1] == "--deleteWord"):
        deleteWord()
    elif(sys.argv[1] == "-aw" or sys.argv[1] == "--addWord"):
        addNewWord()
    elif(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        #placeholder for future --help or -h Feature
        pass