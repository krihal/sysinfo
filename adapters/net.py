import os

class NetClass():
    """ Class to get network interface statistics. """

    #
    # Class constructor
    #
    def __init__(self):
        pass

    #
    # String representation
    #
    def __str__(self):
        return ""

    #
    # Get interface statistics
    #
    def __get_stats(self, dev):
        stats = []

        # Open the two files in /sys/
        for stat in ['rx_bytes', 'tx_bytes']:
            with open('/sys/class/net/' + dev + '/statistics/' + stat) as fd:
                dev_stat = fd.read()
                fd.close()

            # Get the statistics
            stats.append(dev_stat.rstrip('\n'))

        return stats

    #
    # Collector trigger
    #
    def get_stats(self):
        return self.__get_stats('wlan0')
