import os, re

def makeOptions(options):
    optionsString = ""
    for key, value in options.items():
        optionsString += "{}: {}\n".format(key, value)
    return optionsString

def getOption(options):
    askForOption = True
    action = None
    while(askForOption):
        inputString = makeOptions(options)
        action = input(inputString)
        if action in options.keys():
            askForOption = False
    
    return action

def getMode(optionChosen, options):
    instruction = options.get(optionChosen)
    match = re.compile(r'Read|Delete|Append').match(instruction).group(0)

    mode = {
        "Read": "r",
        "Delete": "w",
        "Append": "a"
    }.get(match)

    return mode

def readFile(filename):
    file = open(filename, "r")
    for line in file.readlines():
        print(line)

def executeInstruction(filename, mode):
    if mode == "r":
        readFile(filename)
    else:
        file = open(filename, mode)
        text = input("Please enter your note: ")
        file.write("{}\n".format(text))
        file.close()

def takeNote(options):

    filename = input("Welcome to Note Taker.\nPlease enter a file name: ")

    if os.path.isfile(filename):
        option = getOption(options)
        mode = getMode(option, options)
        executeInstruction(filename, mode)
    else:
        executeInstruction(filename, "w")

options = {
    "A": "Read the file.",
    "B": "Delete the file and start over.",
    "C": "Append the file"
}

if __name__ == "__main__":
    takeNote(options)