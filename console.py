#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
from models import storage
from models.user import User
from models.base_model import BaseModel


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

    def show_user(self, arg):
        """Displays the information of a specific user """
        div_arg = parse(arg)
        obj_dict =  storage.all()
        print(obj_dict["{}.{}".format(div_arg[0], div_arg[1])])

    def create_user(self, arg):
        """Create a new user with the provided attributes"""
        div_arg = parse(arg)
        print(eval(argl[0])().id)
        storage.save()

    def destroy_user(self, arg):
        """ Deletes a specific user based on his 
        or her ID or identification
        """
        div_arg = parse(arg)
        obj_dict = storage.all()
        del obj_dict["{}.{}".format(div_arg[0], div_arg[1])]
        storage.save()

    def update_user(self,arg):
        """ Updates the attributes of an existing user based
        on their ID or identification
        """
        div_arg = parse(arg)
        obj_dict = storage.all()
        if len(argl) == 4:
            obj = obj_dict["{}.{}".format(div_arg[0], div_arg[1])]
            if div_arg[2] in obj.__class__.__dict__.keys():
                value_t = type(obj.__class__.__dict__[div_arg[2]])
                obj.__dict__[div_arg[2]] = value_t(div_arg[3])
            else:
                obj.__dict__[div_arg[2]] = div_arg[3]
        elif type(eval(div_arg[2])) == dict:
            obj = obj_dict["{}.{}".format(div_arg[0], div_arg[1])]
            for key, value in eval(div_arg[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def all_User(self, arg):
        """ Display string representations of 
        all instances of a given class"""
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
