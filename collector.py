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

from threading import Timer

#
# Timer class
#
class TimerEvent():
    """ Really simple timer class. Create a new timer thread and tell
    it run every interval second. """

    def __init__(self, interval, function, *args, **kwargs):
        self.__timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def __run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self.__run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

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
        return self.modules[name].main

    def unload(self, name):
        if self.__loaded(name) == False:
            raise ModuleNotLoaded
        del self.modules[name]
        return self.modules    

def read_config(path):
    timers = dict()
    try:
        import config
    except ImportError:
        print "No configuration file (config.py) found. Exiting."
        sys.exit(-2)
    module = Module("adapters/")
    for key in config.adapters.iterkeys():
        func = module.load(config.adapters[key]['file'])
        timers[key] = TimerEvent(config.adapters[key]['interval'], func)

if __name__ == '__main__':
    read_config("adapters/")
    
#    m = Module("adapters/")
#    print m.load("test")
#    print m.unload("test")
