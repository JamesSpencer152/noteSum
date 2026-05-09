import fileFunctions
from time import sleep
from transcribe import transcribe
from summarizer import summarize

while True:
    fileFunctions.pullFiles()

    fileFunctions.sortAudio()

    if fileFunctions.checkEmpty("audio/processing"):
        transcribe()

    if fileFunctions.checkEmpty("audio/transcripts"):
        summarize()
        
    sleep(5)