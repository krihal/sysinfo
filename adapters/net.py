import os

class NetClass():
    """ Class to get network interface statistics. """

    def __init__(self):
        pass

    def __str__(self):
        return ""

    def __get_stats__(self, dev):
        stats = []
        for stat in ['rx_bytes', 'tx_bytes']:
            with open('/sys/class/net/' + dev + '/statistics/' + stat) as fd:
                dev_stat = fd.read()
                fd.close()
            stats.append(dev_stat.rstrip('\n'))
        return stats

    def get_stats(self, dev):
        return self.__get_stats__(dev)

if __name__ == '__main__':
    n = Net()
    print n
    print n.__get_stats__('wlan0')
