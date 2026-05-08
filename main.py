import fileFunctions
from transcribe import transcribe

print("Audio pulled", flush = True)
fileFunctions.pullFiles()

print("Audio sorted", flush = True)
fileFunctions.sortAudio()

print("Audio transcribed", flush = True)
transcribe()