import os, re

def makeOptions(options):
    ''' Formats dictionary key/value pairs into
        a multiline string in the format:
        key1: value1,
        key2: value2,
        ...
        keyN, valueN
    '''
    optionsString = ""
    for key, value in options.items():
        optionsString += "{}: {}\n".format(key, value)
    return optionsString

def getOption(options):
    ''' Displays a set of options
        and returns the user selected option
        (if and only if valid)
    '''
    askForOption = True
    action = None
    while(askForOption):
        inputString = makeOptions(options)
        action = input(inputString)
        if action in options.keys():
            askForOption = False
    
    return action

def getMode(optionChosen, options):
    ''' Matches user-selected option
        with file I/O mode and returns that mode 
    '''
    instruction = options.get(optionChosen)
    match = re.compile(r'Read|Delete|Append').match(instruction).group(0)

    mode = {
        "Read": "r",
        "Delete": "w",
        "Append": "a"
    }.get(match)

    return mode

def readFile(filename):
    '''Reads each line of a file
    '''
    file = open(filename, "r")
    for line in file.readlines():
        print(line)

def executeInstruction(filename, mode):
    '''Takes a filename and a mode and executes
        the file I/O for that instruction set
    '''
    if mode == "r":
        readFile(filename)
    else:
        file = open(filename, mode)
        text = input("Please enter your note: ")
        file.write("{}\n".format(text))
        file.close()

def takeNote(options):
    '''Prompts the user for a filename and reads,
        writes, or appends to the file
    '''
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