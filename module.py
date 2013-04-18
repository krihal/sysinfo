import os
import sys
import imp
import inspect

#
# Loadable module exceptions
#
class ModuleAlreadyLoaded(Exception): pass
class ModuleNotLoaded(Exception): pass
class ModuleNotFound(Exception): pass
class ModuleError(Exception): pass

#
# Loadable module class 
#
class Module():
    """ Use IMP to handle loadable modules and store them in a
    list. Also provide wrappers to find out if a module is already
    loaded or not. """

    #
    # Class constructor
    #
    def __init__(self, path):
        self.path = path
 
        # Check if we need to append a slash
        if path[-1] is not '/':
            self.path = path + "/"

        # Extend the system path
        self.modules = dict()
        sys.path.append(path)

    #
    # See if a module is already loaded or not
    #
    def __loaded(self, name):
        # Iterate module list
        if not name in self.modules:
            return False
        return True      

    #
    # Load module
    #
    def load(self, modulename):
        # Get the module path
        name = os.path.splitext(os.path.basename(modulename))[0]

        # Verify that the module really exists
        if os.path.isfile(self.path + name + ".py") == False:
            raise ModuleNotFound("Module %s not found" % name)

        # Is it already loaded?
        if self.__loaded(name):
            raise ModuleAlreadyLoaded

        # If not, load it
        self.modules[name] = imp.load_module(name, *imp.find_module(name, [self.path]))

        return self.modules[name]

    #
    # Unload module
    # 
    def unload(self, name):
        # Is it loaded?
        if self.__loaded(name) == False:
            raise ModuleNotLoaded

        # Rmove it from the modules list
        del self.modules[name]
        return self.modules    

    #
    # Get a module object
    #
    def get_instance(self, name):
        # Modules are not supposed to contain more than one class
        try:
            members = inspect.getmembers(self.modules[name])
        except KeyError, e:
            return None

        # Iterate all functions
        for k, v in members:
            if name + "class" in k.lower():
                instance = v
                return v()
        return None
