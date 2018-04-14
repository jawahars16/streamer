import time
from threading import Thread, Event


class ProgressBar:
    PROGRESS_CHARS = ["\\", "|", "/", "--", ]

    def __init__(self, length=1):
        self.length = length

    def run(self):
        index = 0
        self.ready = Event()
        while not self.ready.wait(0.3):
            print("\r{0}".format(self.PROGRESS_CHARS[index]), end="", flush=True)
            index += 1
            if (index >= len(self.PROGRESS_CHARS)):
                index = 0

    def start(self):
        thread = Thread(target=self.run)
        thread.start()

    def stop(self):
        print("\r\r", end="", flush=True)
        self.ready.set()

    def update(self, progress):
        bar = progress / 10
        print("\r[{0}{1}] {2}%".format("#" * int(bar * self.length), "-" * int(((10 - bar) * self.length)), progress,
                                       progress / 10), end="", flush=True)
