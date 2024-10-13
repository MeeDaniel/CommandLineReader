from command import Command
from command_node import CommandNode
from error import *
from logger import Logger
from runner import Runner
from root import Root


if __name__ == "__main__":
    logger = Logger()
    root = Root("Help message", logger)
    runner = Runner(root)
    
    class Math(CommandNode):
        
        class Add(Command):
            def __init__(self):
                super().__init__('add', 'add <number> <number>', 'Adds two numbers', logger)

            def execute(self, a, b):
                self.logger.log(f"Added {a} and {b} to {int(a) + int(b)}")
        
        class Sub(Command):
            def __init__(self):
                super().__init__('sub', 'sub <number> <number>', 'Subtracts two numbers', logger)

            def execute(self, a, b):
                self.logger.log(f"Subtracted {a} and {b} to {int(a) - int(b)}")

        class Mul(Command):
            def __init__(self):
                super().__init__('mul', 'mul <number> <number>', 'Multiplies two numbers', logger)

            def execute(self, a, b):
                self.logger.log(f"Multiplied {a} and {b} to {int(a) * int(b)}")

        class Div(Command):
            def __init__(self):
                super().__init__('div', 'div <number> <number>', 'Divides two numbers', logger)

            def execute(self, a, b):
                self.logger.log(f"Divided {a} and {b} to {int(a) / int(b)}")
    
        def __init__(self):
            super().__init__('math', 'math <operation> [args]', 'Math commands', logger)
            self.add_child(Math.Add())
            self.add_child(Math.Sub())
            self.add_child(Math.Mul())
            self.add_child(Math.Div())
        
    root.add_child(Math())
    
    while True:
        line = input("> ")
        if line == "exit":
            break
        runner.input(line)
