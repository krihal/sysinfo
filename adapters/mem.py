import os

class MemClass():
    """ Class to get the total memory usage, free memory, buffered and
    cached memory. """

    def __init__(self):
        pass

    def __str__(self):
        return ' '.join(self.__mem_current__())

    def __mem_current__(self):
        PROC_MEMINFO = '/proc/meminfo'
        with open(PROC_MEMINFO) as fd:
            meminfo = fd.read().split()
            fd.close()
        del meminfo[3 - 1::3]
        mem = []
        for key in range(len(meminfo)):
            if "MemTotal" in meminfo[key]:
                mem.append(meminfo[key + 1])
            if "MemFree" in meminfo[key]:
                mem.append(meminfo[key + 1])
        return mem

    def get_stats(self):
        return self.__mem_current__()

if __name__ == '__main__':
    m = Mem()
    print m
    
