import fileFunctions
from time import sleep
from transcribe import transcribe

while True:
    fileFunctions.pullFiles()

    fileFunctions.sortAudio()

    if fileFunctions.checkEmpty("audio/processing"):
        transcribe()

    sleep(5)