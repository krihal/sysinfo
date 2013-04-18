import os
import sys
import imp
import redis

from timer import *
from module import *

try:
    import config
except ImportError:
    print "No configuration file (config.py) found. Exiting."
    sys.exit(-2)

class Collector(object):
    def __init__(self, redis_server='localhost', adapters='adapters/'):
        self.redis = redis.Redis(redis_server)
        self.adapters = adapters
        self.timers = dict()

        try:
            self.redis.info()
        except:
            print "Connection to Redis server failed!"
            sys.exit(-2)

    def read_config(self, path):
        self.module = Module(self.adapters)
        for key in config.adapters.iterkeys():
            self.module.load(config.adapters[key]['file'])            

    def collect(self, name, func):
        if self.redis.rpush(name, func()) is False:
            print "%s: Failed to store value!", name
        else:
            print "Put value!"

    def set_adapters(self):
        for key in config.adapters.iterkeys():
            obj = self.module.get_instance(key)
            self.timers[key] = TimerEvent(config.adapters[key]['interval'], 
                                          self.collect, key, obj.get_stats)

if __name__ == '__main__':
    c = Collector()
    c.read_config("adapters/")
    c.set_adapters()
