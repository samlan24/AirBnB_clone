#!/usr/bin/python3
"""entry point of the command interpreter"""

import cmd
import json
from models import storage
import re
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not line:
            print("** class name missing **")
            return
        try:
            cls = eval(line)
            new_instance = cls()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objs = BaseModel.all(BaseModel())
        key = "{}.{}".format(args[0], args[1])
        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objs = BaseModel.all(BaseModel())
        key = "{}.{}".format(args[0], args[1])
        if key not in all_objs:
            print("** no instance found **")
        else:
            del all_objs[key]
            BaseModel.save(BaseModel())
            BaseModel.reload(BaseModel())

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        all_objs = BaseModel.all(BaseModel())
        if not args:
            print([str(obj) for obj in all_objs.values()])
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in all_objs.items()
               if key.split('.')[0] == args[0]])

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objs = BaseModel.all(BaseModel())
        key = "{}.{}".format(args[0], args[1])
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(all_objs[key], args[2], args[3].strip('"'))
        BaseModel.save(BaseModel())
        BaseModel.reload(BaseModel())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
