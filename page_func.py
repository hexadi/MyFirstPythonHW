from subprocess import call
from os import get_terminal_size
from platform import system
# Get terminal window size
space, height = get_terminal_size()


# Clear Screen Function
def clearScreen():
    if (system() == 'Windows'):
        call("cls", shell=True)
    else:
        call("clear", shell=True)


def int_input(start=None, stop=None, type_=None):
    inp = input().strip()
    if (type_ == "float"):
        try:
            inp = float(inp)
        except ValueError:
            return False
    elif inp.isnumeric():
        inp = int(inp)
    else:
        return False
    if (start is not None and inp < start):
        return False
    if (stop is not None and inp > stop):
        return False
    return inp


# Make one line with box function
def page_line(strings, symbol="#"):
    # Find left and right space
    s = len(strings)/2
    if (int(space/2) != space/2 and int(s) == s):
        s1, s2 = int(s), int(s-1)
    elif (int(space/2) == space/2 and int(s) != s):
        s1, s2 = int(s+1), int(s)
    else:
        s1, s2 = int(s), int(s)
    # Print full line
    print(symbol + (" " * (int((space-2)/2) - s1)) + strings +
          (" " * (int((space-2)/2) - s2) + symbol))


# Make full page of box
def page(Lists, symbol="#"):
    clearScreen()
    # Find top and bottom space of page
    h = height/2 - len(Lists) / 2
    if (int(h) != h):
        h1, h2 = int(h-1), int(h-2)
    else:
        h1, h2 = int(h-1), int(h-3)
    # Print full page
    print(symbol*space)
    [print(symbol + " " * (space - 2) + symbol) for i in range(h1)]
    for e in Lists:
        # if
        if isinstance(e, int):
            [print(symbol + " " * (space - 2) + symbol) for i in range(e)]
        elif isinstance(e, str):
            page_line(e, symbol)
    [print(symbol + " " * (space - 2) + symbol) for i in range(h2)]
    s = len("Enter :   ")/2
    if (int(space/2) != space/2):
        s1, s2 = s-1, s
    else:
        s1, s2 = s, s
    print(symbol + " " * int(space/2 - s1) + "Enter : \0337", end="")
    print(" " * int(space/2 - s2) + symbol + "\n" + symbol
          + " " * (space - 2) + symbol + "\n" + symbol*space + "\0338",
          end="")
