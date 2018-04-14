import time
import sys
from threading import Event, Thread

from crawler import Crawler
from progressbar import ProgressBar

# progress = ProgressBar(10)
# for i in range(100):
#     time.sleep(0.1)
#     progress.update(i + 1)


progress = ProgressBar()
progress.start()

crawl = Crawler("http://dl20.mihanpix.com/94/series/young.sheldon/s1/")
crawl.start()

progress.stop()

print(crawl.links)

# crawl.get_links()
