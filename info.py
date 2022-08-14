
from genericpath import isdir, isfile
import os
import pprint
import argparse
import emoji
import colored_text as clrtxt
from colored_text import Color

# NRF & Zephyr path
NRF_DRIVE = "C:\\"
NRF_ROOT = "ncs"
CONNECT_VERSION = "v2.0.2"
NRF_ROOT_PATH = os.path.join(NRF_DRIVE, "ncs")
ZEPHYR_ROOT   = os.path.join(NRF_DRIVE, NRF_ROOT, CONNECT_VERSION, "zephyr")
ZEPHYR_CFG    = os.path.join(ZEPHYR_ROOT, "boards", "arm")

#suffixes
SUFFIX_CONFIG = "_defconfig"
SUFFIX_DEVICE_TREE = ".dts"
#Board info
BOARD = {"nrf52840dk": "nrf52840dk_nrf52840"}
board = "nrf52840dk" #current board string

# Environment variables
env_vars = os.environ
env_printer = pprint.PrettyPrinter(indent=2, width=170)

def currentEnvPath():
    path = env_vars['PATH']
    print('\n'.join(map(str, path.split(';'))))

def allEnvVars():
    env_printer.pprint(dict(env_vars))

def checkPath():
    if not os.path.isdir(NRF_ROOT_PATH):
        print(f"NRF path does not exist {NRF_ROOT_PATH}")
    if not os.path.isdir(ZEPHYR_ROOT):
        print(f"Zephyr path does not exist {ZEPHYR_ROOT}")

def openFile(path):
    if os.path.isdir(path):
        print(path)
    else:
        clrtxt.notFound("Target file", path)

def showBoardFileLocation(suffix, resource_txt):
    file_name = BOARD[board] + suffix
    file_path = os.path.join(ZEPHYR_CFG, BOARD[board], file_name)
    if os.path.isfile(file_path):
        clrtxt.output(Color.LIGHT_CYAN, file_path)
    else:
        clrtxt.notFound(resource_txt, file_path)

def showBoardFolder():
    path = os.path.join(ZEPHYR_CFG, BOARD[board])
    if os.path.isdir(path):
        clrtxt.output(Color.LIGHT_PURPLE, path)
    else:
        clrtxt.notFound("Board Configuration File", path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='nrf utilities')
    parser.add_argument('-p', '--path', help='Shows the PATH of the environment variables', action='store_true')
    parser.add_argument('-o', '--open', help='Open a file using vs code', type=str, action="store")
    parser.add_argument('-c', '--config', help= f'Show board configuration file ({SUFFIX_CONFIG}) in zephyr', action="store_true")
    parser.add_argument('-d', '--devicetree', help= f'Show board device tree file ({SUFFIX_DEVICE_TREE}) in zephyr', action="store_true")
    parser.add_argument('-f', '--folder', help= f'Show board settings folder in zephyr', action="store_true")
    
    print(emoji.emojize(f":water_wave: nrf home location: {NRF_ROOT_PATH}, version: {CONNECT_VERSION}, :gear:  board: {board}"))
    checkPath()
    
    args = parser.parse_args()

    if args.path:
        currentEnvPath()
    elif args.config:
        showBoardFileLocation(SUFFIX_CONFIG, "Board Configuration File")
    elif args.devicetree:
        showBoardFileLocation(SUFFIX_DEVICE_TREE, "Board Device Tree File")
    elif args.open and len(args.open) > 0:
        # !!! No need to implement, just use ctrl+mouse click in the vscode terminal
        openFile(args.open)
    elif args.folder:
        showBoardFolder()
    else:
        clrtxt.output(Color.GREEN, "printing helps")
        parser.print_help()
