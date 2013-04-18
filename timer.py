from threading import Timer

#
# Timer class
#
class TimerEvent():
    """ Really simple timer class. Create a new timer thread and tell
    it run every interval second. """

    #
    # Class constructor
    # 
    def __init__(self, interval, function, *args, **kwargs):
        self.__timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()
        
    #
    # Runner, gets trigged by thread
    #
    def __run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    #
    # Start the timer
    #
    def start(self):
        # Verify that the thread is not started
        if not self.is_running:
            self._timer = Timer(self.interval, self.__run)
            self._timer.start()
            self.is_running = True

    #
    # Stop the timer
    #
    def stop(self):
        self._timer.cancel()
        self.is_running = False
