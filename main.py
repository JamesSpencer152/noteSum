import fileFunctions
from time import sleep
from transcribe import transcribe

while True:
    fileFunctions.pullFiles()
    print("Audio pulled", flush = True)

    fileFunctions.sortAudio()
    print("Audio sorted", flush = True)

    if fileFunctions.checkEmpty("audio/processing"):
        transcribe()
        print("Audio transcribed", flush = True)
    else:
        print("Nothing to transcribe", flush = True)

    sleep(5)