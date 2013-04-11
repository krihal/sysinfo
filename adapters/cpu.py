import os

class CPU():
    """ CPU adapter, return the average CPU load for the 15, 10 and 5
    last minutes. """

    def __init__(self):
        pass

    def __cpu_percent__(self):
        PROC_LOADAVG = '/proc/loadavg'
        with open(PROC_LOADAVG) as fd:
            loadavg = fd.read()
            fd.close()
        load15, load10, load5 = loadavg.split()[:3]
        return float(load15), float(load10), float(load5)

    def __str__(self):
        return "%s %s %s" % self.__cpu_percent__()

    def get_load_average(self):
        return self.__cpu_percent__()

if __name__ == '__main__':
    c = CPU()
    print c
