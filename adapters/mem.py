import os

class MemClass():
    """ Class to get the total memory usage, free memory, buffered and
    cached memory. """

    #
    # Class constructor
    #
    def __init__(self):
        pass

    #
    # String representation
    #
    def __str__(self):
        return ' '.join(self.__mem_current())

    #
    # Get memory usage
    #
    def __mem_current(self):
        # Open proc file
        with open('/proc/meminfo') as fd:
            meminfo = fd.read().split()
            fd.close()

        # Remove uninteresting items from list
        del meminfo[3 - 1::3]
        mem = []

        # Return the two things we're interested in
        for key in range(len(meminfo)):
            if "MemTotal" in meminfo[key]:
                mem.append(meminfo[key + 1])
            if "MemFree" in meminfo[key]:
                mem.append(meminfo[key + 1])

        return mem

    #
    # Collector trigger
    #
    def get_stats(self):
        return self.__mem_current()
    
