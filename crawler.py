import requests
import re
import grequests
from progressbar import ProgressBar
from threading import Thread, Event


class Crawler:
    PATTERN = "href=['|\"].*['|\"]"

    def __init__(self, url):
        self.url = url

    def run(self):
        hyperlinks = []
        response = requests.get(self.url)
        if response.status_code is requests.codes.ok:
            content = response.text
            links = re.findall(self.PATTERN, content)
            for link in links:
                link = str.replace(link, "href=", "")
                link = str.replace(link, "\"", "")
                hyperlinks.append(f"{self.url}{link}")
        self.links = hyperlinks
        self.ready.set()

    def start(self):
        self.ready = Event()
        thread = Thread(target=self.run())
        thread.start()
        self.ready.wait()
        return self.links

    def on_response(self, response, *args, **kwargs):
        print(response)

    def get_links(self):
        request = grequests.get(self.url)
        self.progress.run()
        print(grequests.map([request]))
        self.progress.stop()
