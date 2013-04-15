import os
import sys
import imp

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

    def __init__(self, path):
        self.path = path
        if path[-1] is not '/':
            self.path = path + "/"
        self.modules = dict()
        sys.path.append(path)

    def __loaded(self, name):
        if not name in self.modules:
            return False
        return True      

    def load(self, modulename):
        name = os.path.splitext(os.path.basename(modulename))[0]
        if os.path.isfile(self.path + name + ".py") == False:
            raise ModuleNotFound("Module %s not found" % name)
        if self.__loaded(name):
            raise ModuleAlreadyLoaded
        self.modules[name] = imp.load_module(name, *imp.find_module(name, [self.path]))
        return self.modules[name]

    def unload(self, name):
        if self.__loaded(name) == False:
            raise ModuleNotLoaded
        del self.modules[name]
        return self.modules    
