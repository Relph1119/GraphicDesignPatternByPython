from interpreter.ProgramNode import ProgramNode
from interpreter.Context import Context

file = open("program.txt", 'r')

for line in file:
    line = line.replace("\n", "")
    print("text =\"{0}\"".format(line))
    node = ProgramNode()
    node.parse(Context(line))
    print("node = {0}".format(node))
file.close()

