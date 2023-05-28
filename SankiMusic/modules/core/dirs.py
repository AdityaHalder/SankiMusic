import os
import sys
from os import listdir, mkdir

from ...console import LOGGER


def dirr():
    if "SankiMusic" not in listdir():
        LOGGER(__name__).warning(
            f"Assets Folder not Found. Please clone repository again."
        )
        sys.exit()
    if "resource" not in listdir("SankiMusic"):
        LOGGER(__name__).warning(
            f"Resource Folder not Found. Please clone repository again."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
