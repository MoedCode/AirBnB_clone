#!/usr/bin/python3
"""
    In the AirBnB Clone Project, the "console" is a command-line
    interface designed for managing and manipulating project objects,
    facilitating tasks such as creating, updating, deleting, and retrieving data. Additionally, the console functions as a testing and validation tool for the project's storage engine, ensuring effective abstraction of data storage and retrieval.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A commandline interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is encountered (Ctrl+D)."""
        print()  # Add a newline before exiting
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        # print("An empty line doesn't execute anything.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
