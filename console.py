#!/bin/bash/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ exit the program """
        return True

    def do_EOF(self, arg):
        """ exit with ctrl + D """
        return True

    def emptyline(self):
        """ an empty line is entered (do nothing) """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
