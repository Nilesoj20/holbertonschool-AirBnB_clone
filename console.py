#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
<<<<<<< HEAD
from models.base_model import BaseModel
from models import storage
=======
from models import storage
from models.user import User
from models.base_model import BaseModel

>>>>>>> 8ca093358a600f0a3eb26f0a8750418707bbd09d

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB"""

    prompt = '(hbnb) '
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """ exit the program """
        return True

    def do_EOF(self, arg):
        """ exit with ctrl + D """
        return True

    def emptyline(self):
        """ an empty line is entered (do nothing) """
        pass

<<<<<<< HEAD
    def do_create(self, arg):
        """create a new instance"""
        args = arg.split()
        if not args:
            print("** class name missiong **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        instance = eval(class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representantion of a instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found**")
            return
        print(instances[key])

    def do_destroy(self, arg):
        """Deletes and instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instances found **")
            return
        del instances[key]
        storage.save()

    def do_all(self, arg):
        """print all string representations of instances"""
        args = arg.split()
        instances = storage.all()
        if not args:
            print([str(instance) for instance in instances.values()])
        else:
            class_name = args[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            filtered_instances = [
                    str(instance)
                    for instance in instances.values()
                    if instance.__class__.__name__ == class_name
            ]
            print(filtered_instances)

    def do_update(self, arg):
        """updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()
=======
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
>>>>>>> 8ca093358a600f0a3eb26f0a8750418707bbd09d


if __name__ == '__main__':
    HBNBCommand().cmdloop()
