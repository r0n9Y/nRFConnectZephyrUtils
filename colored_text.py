#https://unicode.org/emoji/charts/emoji-list.html
import emoji
# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
from enum import Enum, unique
#  list comprehension :(
"""
https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html
Black       0;30     Dark Gray     1;30
Blue        0;34     Light Blue    1;34
Green       0;32     Light Green   1;32
Cyan        0;36     Light Cyan    1;36
Red         0;31     Light Red     1;31
Purple      0;35     Light Purple  1;35
Brown       0;33     Yellow        1;33
Light Gray  0;37     White         1;37
"""
@unique
class Color(Enum):
    WHITE =         "\033[00m"
    RED   =         "\033[0;31m"
    LIGHT_RED =     "\033[1;31m"
    GREEN  =        "\033[92m"
    LIGHT_GREEN =   "\033[1;32m"
    YELLOW =        "\033[93m"
    BLUE =          "\033[0;34m"
    LIGHT_BLUE =    "\033[94m"
    PURPLE =        "\033[0;35m"
    LIGHT_PURPLE =  "\033[1;35m"
    CYAN =          "\033[0;36m"
    LIGHT_CYAN =    "\033[1;36m"
    LIGHT_GRAY =    "\033[0;37m"
    DARK_GRAY =     "\033[1;30m"
    BROWN =         "\033[0;33m"
    BLACK =         "\033[98m"
    DEFAULT =       "\033[0m"
    pass

def output(color, text):
    if isinstance(color, Color):
        print(color.value + text + Color.DEFAULT.value)
    else:
        print(f"{text + Color.DEFAULT.value}")

def setDefaultColor(color):
    if isinstance(color, Color):
        Color.DEFAULT = color
    else:
        Color.DEFAULT = Color.WHITE

def colored(color, text):
    if isinstance(color, Color):
        return color.value + text + Color.DEFAULT.value
    else:
        return text + Color.DEFAULT.value

def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def warning(text):
    print(emoji.emojize(f':warning: {text}'))

def error(text):
    print(emoji.emojize(f':cross_mark: {text}'))

def notFound(resource, location):
    print(emoji.emojize(f':cross_mark: {resource} does NOT exist [{location}]'))
