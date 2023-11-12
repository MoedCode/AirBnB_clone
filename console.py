#!/usr/bin/python3
"""
    In the AirBnB Clone Project, the "console" is a command-line
    interface designed for managing and manipulating project objects,
    facilitating tasks such as creating, updating, deleting, and retrieving data. Additionally, the console functions as a testing and validation tool for the project's storage engine, ensuring effective abstraction of data storage and retrieval.
"""
import cmd
from models.base_model import BaseModel
from uuid import uuid4
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


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

            if (strkey in storage.reload):
                print(storage.all()[strkey])
            else:
                print("** no instance found **")
                return
        else:
            print("** class name missing **")
            return

    def do_update(self, args):
        if args is not None and len(args) != 0:

            argstok_list = args.split(' ')
            asl_len = len(argstok_list)
            stor_dict = storage.all()
            if (argstok_list[0] not in HBNBCommand.classes_dict):
                print("** class doesn't exist **")
                return
            if (asl_len == 1):
                print("** instance id missing **")
                return

            if (asl_len == 2):
                print("** attribute name missing **")
                return
            if (asl_len == 3):
                print("** value missing **")
                return
            search_key = argstok_list[0] + '.' + argstok_list[1]
            print("search key => ", search_key)
            if (stor_dict not in stor_dict.keys()):
                print("** no instance found **")
            else:
                # search key is Class +
                class_intst = stor_dict[search_key]
                ins_dict = class_intst.__dict__
                atrkey = argstok_list[2]
                atrvalue = argstok_list[3]
                if atrkey in ins_dict:
                    ins_dict[atrkey] = (type(ins_dict[atrkey])(atrvalue))
                else:
                    ins_dict[atrkey] = eval(atrvalue)
                storage.save()
        else:
            print("** class name missing **")


if __name__ == '__main__':

    HBNBCommand().cmdloop()
