from error import MissingArgument


def get_args(order, *args, **kwargs):
    ar = []
    kwrd = kwargs.copy()
    for i, arg in enumerate(args):
        if i < len(order):
            kwrd[order[i]] = arg
        else:
            ar = args[i:]
            break
    
    for k in order:
        if k not in kwrd:
            raise MissingArgument(f"Missing required argument: {k}")
    
    return ar, kwrd


if __name__ == "__main__":
    print(get_args(['name'], 'math', 'add', '1', '2'))