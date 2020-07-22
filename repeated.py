import time, threading

from loguru import logger


class Repeated:
    def __init__(self, interval_ms: int, times: int = -1):
        logger.info('Creating new repeated callback, {}ms {} times', interval_ms, times)
        self._interval_ms = interval_ms
        self._times = times

    def __call__(self, callback):
        logger.info('in __call__, {}', callback)

        def wrap(*args, **kwargs):
            print('in wrap')
            stop_event = threading.Event()

            def threaded():
                print('in threded')
                i = 0
                while i != self._times and not stop_event.is_set():
                    callback(*args, **kwargs)
                    time.sleep(self._interval_ms / 1000)
                    i += 1

            timer = threading.Timer(0, threaded)
            timer.daemon = True
            timer.start()

            return stop_event

        print(wrap)

        return wrap
