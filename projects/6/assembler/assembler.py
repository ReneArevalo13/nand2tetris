import re
# read in all the lines from the .asm file and put into an array
def readFile(filename):
    file1 = open(filename, 'r')
    lines = file1.readlines()
    return lines

# remove the comments and whitespace from input
def cleanLines(lines):
    cleanLines = []
    for line in lines:
        # remove the comments //
        if re.search("//(.*)", line):
            continue
        #remove the whitespace and "\n"
        if line.strip():
            cleanLines.append(line.strip())
        
    return cleanLines

# perform the first pass to build out the symbol table
# input is zip of clean lines and command type
def firstPass(lineTuple):
    lineNumber = []
    linecount = -1

    for line in lineTuple:
        if line[1] == "l_command":
            label = getBetweenParentheses(line[0])
            symbolTableCopy[label] = linecount + 1
            continue
        else:
            lineNumber.append(line)
            linecount += 1
    return lineNumber   

def secondPass(lineTuple):
    variableStart = 16
    for line in lineTuple:
        if line[1] == "a_command":
            label = line[0][1:]
            if label in symbolTableCopy:
                continue
            else:
                processVariables(line[0], variableStart)
                variableStart += 1
             

# take a single line and determine what type of command it is. a_command, c_command, l_command
def commandType(line):
    commands = []
    for char in line:
        first = char[0]
        if first == "@":
            commands.append("a_command") 
        elif first == "(":
            commands.append("l_command") 
        else:
            commands.append("c_command")
    return commands

# parse the file and returns a tuple iterator {command, commandType}
def parseFile(filename):
    lines = readFile(filename)
    clean = cleanLines(lines)
    commands = commandType(clean)
    return list(zip(clean, commands))

def passThrough(commandList):
    firstPass(commandList)
    secondPass(commandList)

# get the binary code for an A instruction @value, where value will be the binary rep of the decimal number
def processA(line):
    out = "0000000000000000"
    var = line[1:]
    # print(line[1:])
    if var.isnumeric():  
        num = int(line[1:])
        ans = format(num, 'b')
        cut = 16 - len(ans)
        new = out[0:cut] + ans
    else:
        num = symbolTableCopy[var]
        ans = format(num, 'b')
        cut = 16 - len(ans)
        new = out[0:cut] + ans
    return new

def processVariables(line, variableStart):
    symbol = line[1:]
    if symbol[0].isalpha(): 
        symbolTableCopy[symbol] = variableStart
    
# process the C commands into it's dest, comp, and jmp commands
def compCommands(line):
    # retrieve the destination i.e. left of the equal sign
    if ("=" in line):
        dest = line.split("=")[0]
        rest = line.split("=")[1]
        if (";" in rest):
            comp = rest.split(";")[0]
            jmp = rest.split(";")[1]
        else:
            comp = rest
            jmp = "null"
    else:
        dest = "null"
        if (";" in line):
            comp = line.split(";")[0]
            jmp = line.split(";")[1]
        
    return [dest, comp, jmp]

# build the binary represenation of a c command
def buildCbinary(commands):
    
    if ("M" in commands[1]):
        # use comp1 dictionary, set a bit to 1
        comp = "1" + comp1.get(commands[1])
    else:
        # use comp0 dictionary, set a bit to 0
        comp = "0" + comp0.get(commands[1])
        
    destination = dest.get(commands[0])
    # print("destination is: " + destination)
    jmp = jump.get(commands[2])
    # print("jump is : " + jmp)
    return "111" + comp + destination + jmp

def processC(line):
    commands = compCommands(line)
    return buildCbinary(commands)

def process(lines):
    passThrough(lines)
    f = open("Prog.hack", "w")
    for line, commandType in lines:
        if (commandType == "a_command"):
            out = processA(line) + "\n"
            f.write(out)
        elif (commandType == "c_command"):
            out = processC(line) + "\n"
            f.write(out)
            
    f.close

def compareOutputs(file1, file2):
    file1Out = readFile(file1)
    file2Out = readFile(file2)
    return file1Out == file2Out

def getBetweenParentheses(word):
    return word.split("(")[1].split(")")[0]
    
# driver function        
def driver():
    filename = input("Please enter the assembly file: ")
    ready = parseFile(filename)
    process(ready)
    symbolTableCopy.clear()
    
    
    
    



# Build dictionaries needed to build binary representation
comp0 = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110000",
    "!D": "001101",
    "!A": "110001",
    "-D": "001111",
    "-A": "110011",
    "D+1": "011111",
    "A+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "D+A": "000010",
    "D-A": "010011",
    "A-D": "000111",
    "D&A": "000000",
    "D|A": "010101"
    }

comp1 = {
    "M": "110000",
    "!M": "110001",
    "-M": "110011",
    "M+1": "110111",
    "M-1": "110010",
    "D+M": "000010",
    "D-M": "010011",
    "M-D": "000111",
    "D&M": "000000",
    "D|M": "010101"
    }
dest = {
    "null": "000",
    "M": "001",
    "D": "010", 
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111" 
    }
    
jump = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100", 
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}


# Predefined symbols that are needed for symbolic programming
symbolTable = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4, 
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576
}

symbolTableCopy = symbolTable.copy()

driver()
filename1 = "Pong.hack"
filename2 = "Prog.hack"
print(compareOutputs(filename1, filename2))
