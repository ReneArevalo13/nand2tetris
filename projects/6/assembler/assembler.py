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
    return zip(clean, commands)

# get the binary code for an A instruction @value, where value will be the binary rep of the decimal number
def processA(line):
    out = "0000000000000000"
    num = int(line[1:])
    ans = format(num, 'b')
    cut = 16 - len(ans)
    new = out[0:cut] + ans
    return new

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
        # print("comp is: " + comp)
    else:
        # use comp0 dictionary, set a bit to 0
        comp = "0" + comp0.get(commands[1])
        # print("comp is: " + comp)
        
    destination = dest.get(commands[0])
    # print("destination is: " + destination)
    jmp = jump.get(commands[2])
    # print("jump is : " + jmp)
    return "111" + comp + destination + jmp

def processC(line):
    commands = compCommands(line)
    return buildCbinary(commands)

def process(lines):
    f = open("Prog.hack", "w")
    for line, commandType in lines:
        
        if (commandType == "a_command"):
            # print("Processing A command")
            out = processA(line) + "\n"
            # print(out)
            f.write(out)
        elif (commandType == "c_command"):
            # print("Processing C command")
            out = processC(line) + "\n"
            # print(out)
            f.write(out)
            
    f.close

# driver function        
def driver():
    filename = input("Please enter the assembly file: ")
    ready = parseFile(filename)
    process(ready)
    
    
    
    



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

# filename = "Add.asm"
# ready = parseFile(filename)
# process(ready)

driver()

# for i in ready:
#     print(i)
    
# test = "@45"
# print(processA(test))

# lines = readFile(filename)
# clean = cleanLines(lines)
# print(lines)
# print(clean)
# for line in lines:
#     print(line)
# print(clean)
# commands = commandType(clean)
# print(commands)


# for i in clean:
#     print(i[0])
    
# for c in clean:
#     # print(c)
#     for char in c:
#         print(char)



# out = "0000000000000000"
# num = 45
# ans = format(num, 'b')
# print("The binary string is", ans)
# print("the length of this binary is: " + str(len(ans)))
# cut = 16 - len(ans)
# new = out[0:cut]+ans
# print(new)

# test = "D=D-A"
# commands = processC(test)
# print(commands)
# out = buildCbinary(commands)
# print(out)

# print("A is: " + out)
# print("B is: 1110010011010000")
# print(out == "1110010011010000")

# test = "@3"
# out = processA(test) + "\n"
# print(out)

