import os
import sys
import imp
import redis
import signal
import collector

def sighandler(signal, frame):
    print "Exiting..."
    c.close()
    sys.exit(0)

if __name__ == '__main__':
    global c
    c = collector.Collector()
    signal.signal(signal.SIGINT, sighandler)
    c.read_config()
    c.set_adapters()    
