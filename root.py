from command_node import CommandNode


class Root(CommandNode):
    def __init__(self, help_message, logger):
        super().__init__('', '<command> [args]', help_message, logger)