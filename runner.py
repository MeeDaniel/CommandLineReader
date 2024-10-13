from logger import Logger
from command_node import CommandNode


class Runner:
    def __init__(self, root: CommandNode):
        if not isinstance(root, CommandNode):
            raise TypeError("root must be an instance of CommandNode")
        self.root = root
    
    def input(self, line):
        self.root(*line.split())