class Logger:
    def __init__(self):
        self.logs = []

    def construct_message(self, *msgs, sep=' ', end='\n'):
        return sep.join(str(msg) for msg in msgs) + end
    
    def log(self, *msgs, sep=' ', end='\n'):
        msg = self.construct_message(*msgs, sep=sep, end=end)
        self.logs.append(msg)
        print(msg)
