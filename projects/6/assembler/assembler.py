import re
# read in all the lines from the .asm file and put into an array
def readFile(filename):
    file1 = open(filename, 'r')
    lines = file1.readlines()
    return lines

# remove the comments and whitespace from input
def cleanLines(lines):
    cleanLines = []
    comment = re.compile
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
    
    
    
    
filename = "Add.asm"
ready = parseFile(filename)
for i in ready:
    print(i)
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