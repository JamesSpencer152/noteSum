import fileFunctions
from time import sleep
from transcribe import transcribe

while True:
    fileFunctions.pullFiles()

    fileFunctions.sortAudio()

    if fileFunctions.checkEmpty("audio/processing"):
        transcribe()
    else:
        print("Nothing to transcribe", flush = True)

    sleep(5)