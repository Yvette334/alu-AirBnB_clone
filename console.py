#!/usr/bin/python3
"""
Command interpreter for the HBNB program
"""
import cmd
import json
import shlex
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command processor for HBNB program"""
    prompt = '(hbnb) '
    valid_classes = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the programme in non-interactive mode"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id
        Usage: create <class name>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        Usage: show <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = args[0] + "." + args[1]
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = args[0] + "." + args[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        args = shlex.split(arg)
        objects = storage.all()
        obj_list = []

        if len(args) == 0:
            for obj in objects.values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, obj in objects.items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in objects:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            obj = objects[key]
            attr_name = args[2]
            attr_value = args[3]
            # Skip protected attributes
            if attr_name in ["id", "created_at", "updated_at"]:
                return
            # Try to convert value to appropriate type
            try:
                if attr_value.isdigit():
                    attr_value = int(attr_value)
                elif attr_value.replace('.', '', 1).isdigit() and \
                        attr_value.count('.') < 2:
                    attr_value = float(attr_value)
            except AttributeError:
                pass
            setattr(obj, attr_name, attr_value)
            obj.save()

    def do_count(self, arg):
        """Counts the number of instances of a class
        Usage: count <class name> or <class name>.count()
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for obj in storage.all().values():
                if args[0] == obj.__class__.__name__:
                    count += 1
            print(count)

    def do_models(self, arg):
        """List all available models"""
        print(", ".join(self.valid_classes))

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        arg_list = arg.split('.')
        if len(arg_list) == 1:
            print("*** Unknown syntax: {}".format(arg))
            return
        class_name = arg_list[0]
        command = arg_list[1].split('(')[0]
        args = arg_list[1].split('(')[1].rstrip(')')
        # Handle different command formats
        if command == 'all':
            self.do_all(class_name)
        elif command == 'count':
            self.do_count(class_name)
        elif command == 'show':
            id = args.strip('"\'')
            self.do_show(class_name + ' ' + id)
        elif command == 'destroy':
            id = args.strip('"\'')
            self.do_destroy(class_name + ' ' + id)
        elif command == 'update':
            # Check for dictionary update format
            dict_match = re.search(r"([^{]*),\s*({.*})(.*)", args)
            if dict_match:
                id = dict_match.group(1).strip('\'"')
                try:
                    attr_dict = eval(dict_match.group(2))
                    for attr_name, attr_value in attr_dict.items():
                        update_cmd = '{} {} {} "{}"'.format(
                            class_name, id, attr_name, attr_value)
                        self.do_update(update_cmd)
                except Exception as e:
                    print("*** Error: {}".format(e))
            else:
                # Handle regular update format
                args_list = args.split(',')
                id = args_list[0].strip('\'"')
                if len(args_list) > 1:
                    attr_name = args_list[1].strip('\'" ')
                    if len(args_list) > 2:
                        attr_value = args_list[2].strip('\'" ')
                        self.do_update('{} {} {} "{}"'.format(
                            class_name, id, attr_name, attr_value))
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
