#!/usr/bin/python3
"""
    In the AirBnB Clone Project, the "console" is a command-line
    interface designed for managing and manipulating project objects,
    facilitating tasks such as creating, updating, deleting, and retrieving data. Additionally, the console functions as a testing and validation tool for the project's storage engine, ensuring effective abstraction of data storage and retrieval.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ A commandline interpreter class"""
    prompt = "(hbnb) "

    def emptyline(self):
        """override the method and shouldn't execute any thing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':

    HBNBCommand().cmdloop()
