#!/usr/bin/python3
"""
    In the AirBnB Clone Project, the "console" is a command-line
    interface designed for managing and manipulating project objects,
    facilitating tasks such as creating, updating, deleting, and retrieving data. Additionally, the console functions as a testing and validation tool for the project's storage engine, ensuring effective abstraction of data storage and retrieval.
"""
import cmd
from models.base_model import BaseModel
from uuid import uuid4


class HBNBCommand(cmd.Cmd):
    """ A commandline interpreter class"""
    prompt = "(hbnb) "
    classes_dict = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program \n"""

        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is encountered (Ctrl+D)."""
        print()  # Add a newline before exiting
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        print(end="")

    def do_create(self, arg):
        if (arg):
            if (arg not in HBNBCommand.classes_dict):
                print("** class name missing **")
            else:
                for Key, value in HBNBCommand.classes_dict.items():
                    if (Key == arg):
                        my_model = value()
                        my_model.save()
                        print(my_model.id)
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Print a string representation of an class instance to terminal
            accepts   class name and id as arguments """
        if (args):
            argstok_list = args.split(' ')
            if (len(argstok_list) <= 1):
                print("** instance id missing **")
                return False

            if (argstok_list[0] not in HBNBCommand.classes_dict):
                print("** class doesn't exist **")
                return

            strkey = argstok_list[0] + '.' + argstok_list[1]

            if (strkey in storage.all()):
                print(storage.all()[strkey])
            else:
                print("** no instance found **")
                return
        else:
            print("** class name missing **")
            return


if __name__ == '__main__':

    HBNBCommand().cmdloop()
