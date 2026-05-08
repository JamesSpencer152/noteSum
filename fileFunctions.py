import subprocess
import shutil
from pathlib import Path

#Pulls the files from tailscale's tail drop

def pullFiles():
    subprocess.run(["tailscale", "file", "get", "audio/incoming"])
    print("Audio pulled", flush = True)


def sortAudio():
    incoming = Path("audio/incoming")
    files = list(incoming.iterdir())
    if len(files) == 0:
        print("nothing to sort", flush = True)
        return
    else:
        for i in files: 
            if i.suffix == '.m4a':
                moveFile(i, "audio/processing")
                print(i.name + " moved to processing")
            else:
                moveFile(i,"audio/nonAudio")
                print(i.name + " moved to nonAudio")

def moveFile(source, destination):
    shutil.move(source, destination)

def checkEmpty(folder):
    files = list(Path(folder).iterdir())
    if len(files) == 0:
        print(folder + " folder empty")
        return False
    else:
        return True