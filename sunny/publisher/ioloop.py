
import asyncio
class IOLoop(object):

    self.event_loop = asyncio.get_event_loop()

    def __init__(self):
        pass

    def start(self):

        if self._running:
            raise RuntimeError("IOLoop is already running")
        if self._stopped:
            self._stopped = False
            return







