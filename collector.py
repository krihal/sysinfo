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
    """ Collector, start one thread per adapter and put data in Redis
    storage. """

    #
    # Class constructor
    #
    def __init__(self, redis_server='localhost', adapters='adapters/'):
        self.redis = redis.Redis(redis_server)
        self.adapters = adapters
        self.timers = dict()
        self.module = None

        # Poll Redis info in order to verify connection
        try:
            self.redis.info()
        except:
            print "Connection to Redis server failed!"
            sys.exit(-2)

    #
    # Read configuration file
    #
    def read_config(self):
        self.module = Module(self.adapters)

        # For every configuration item, load module
        for key in config.adapters.iterkeys():
            print "Loading: %s" % key
            self.module.load(config.adapters[key]['file'])            

    #
    # Start adapter threads
    #
    def set_adapters(self):
        for key in config.adapters.iterkeys():
            obj = self.module.get_instance(key)

            # Start timer threads
            self.timers[key] = TimerEvent(config.adapters[key]['interval'], 
                                          self.__collect, key, obj.get_stats)

    #
    # Read data from adapter and put in Redis
    #
    def __collect(self, name, func):
        if self.redis.rpush(name, func()) is False:
            print "%s: Failed to store value!", name
        else:
            print "Put value: %s" % name        

    #
    # Make sure Redis flushes data to disk
    #
    def close(self):
        self.redis.save()
