from json import loads
from .error import Error
from .logger import Logger


class Command:
    def __init__(self, name, usage_text, help_text, logger: Logger):
        self.name = name
        self.help_text = help_text
        self.usage_text = usage_text
        if not isinstance(logger, Logger):
            raise TypeError("logger must be an instance of Logger")
        self.logger = logger

    def execute(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement the execute method.")
    
    def __call__(self, *args, **kwargs):
        try:
            return self.execute(*args, **kwargs)
        except Error as e:
            print(f"{str(e)=}")
            info = loads(str(e).replace("'",'"'))
            self.logger.log(f"{info['name']}Error: {info['desc']}")

    def help(self):
        return self.help_text

    def usage(self):
        return self.usage_text

    def __str__(self):
        return f"<{self.__class__.__name__} {self.name}>"