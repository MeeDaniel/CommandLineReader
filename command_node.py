from command import Command
from _util import *

from typing import List


class CommandNode(Command):
    def __init__(self, name: str, usage_text: str, help_text: str, logger, children: List[Command] = None):
        super().__init__(name, usage_text, help_text, logger)
        self.children = children or []
    
    def add_child(self, child: Command):
        self.children.append(child)
    
    def remove_child(self, child: Command):
        self.children.remove(child)
    
    def execute(self, *args, **kwargs):
        args, kwargs = get_args(['name'], *args, **kwargs)
        for child in self.children:
            if child.name == kwargs['name']:
                kwargs.pop('name')
                return child(*args, **kwargs)