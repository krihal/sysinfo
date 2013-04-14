import os
import sys
import imp

from timer import *
from module import *
    
try:
    from sqlite3 import dbapi2 as sqlite3
except ImportError:
    print "Support for Sqlite 3 needed. Quitting."
    sys.exit(-2)

def init_db():
    db = self.__get_db()
    try:
        with open('schema.sql') as fd:
            db.cursor().executescript(fd.read())
            db.commit()
    except Exception, e:
        print "Failed to open DB: %s" % e
        sys.exit(-2)
            
def get_db():
    try:
        sqlite_db = sqlite3.connect('swedbank.db')
        sqlite_db.row_factory = sqlite3.Row
    except Exception, e:
        print "Failed to connect to DB (is the database initialized?): %s" % e
        sys.exit(-2)
    return sqlite_db

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
        timers[key] = TimerEvent(config.adapters[key]['interval'], func, get_db())

if __name__ == '__main__':
    read_config("adapters/")
