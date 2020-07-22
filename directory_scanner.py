import os
import os.path
import time

from pathed import File, Directory

from loguru import logger
from repeated import Repeated
from pprint import pprint
from blake3 import blake3

scan_interval_ms = 5000


class DirectoryScanner:
    def __init__(self, dirname: str, call_on_change = None):
        self.__dirname = dirname
        self.__directory = None
        self.__call_on_change = call_on_change

    @Repeated(scan_interval_ms)
    def scan(self) -> None:

        logger.info('Scanning {}...', self.__directory.name)

    def _dir_has_contents(self) -> bool:
        return len(os.listdir(self.__directory)) != 0

    @property
    def directory(self) -> Directory:
        return self.__directory


if __name__ == '__main__':
    a = DirectoryScanner('M:/workspace/java/test')
    b = a.directory
    a.scan()
    time.sleep(10)
