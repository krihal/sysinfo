import os
import sys
import imp

from timer import *
from module import *
    
def read_config(path):
    timers = dict()
    try:
        import config
    except ImportError:
        print "No configuration file (config.py) found. Exiting."
        sys.exit(-2)
    module = Module("adapters/")
    for key in config.adapters.iterkeys():
        module.load(config.adapters[key]['file'])
        obj = module.get_instance(key)
        timers[key] = TimerEvent(config.adapters[key]['interval'], obj.get_stats)

if __name__ == '__main__':
    read_config("adapters/")
