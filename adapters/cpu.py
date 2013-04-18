import os

class CPUClass():
    """ CPU adapter, return the average CPU load for the 15, 10 and 5
    last minutes. """

    #
    # Class consctructor
    #
    def __init__(self):
        pass

    #
    # Get CPU usage
    #
    def __cpu_percent(self):
        # Open the proc file
        with open('/proc/loadavg') as fd:
            loadavg = fd.read()
            fd.close()

        # Get the different loads
        load15, load10, load5 = loadavg.split()[:3]

        # Convert to float and return
        return float(load15), float(load10), float(load5)

    #
    # String representation
    #
    def __str__(self):
        return "%s %s %s" % self.__cpu_percent()

    #
    # Collector tigger
    #
    def get_stats(self):
        return self.__cpu_percent()
