import subprocess
import shutil
from pathlib import Path

#Pulls the files from tailscale's tail drop

def pullFiles():
    subprocess.run(["tailscale", "file", "get", "audio/incoming"])


def sortAudio():
    incoming = Path("audio/incoming")
    files = list(incoming.iterdir())
    for i in files: 
        print(i.name)
        print(i.suffix)
        if i.suffix == '.m4a':
            moveFile(i, "audio/processing")
            print("moved to processing")
        else:
            moveFile(i,"audio/nonAudio")
            print("moved to nonAudio")

def moveFile(source, destination):
    shutil.move(source, destination)

def checkEmpty(folder):
    files = list(Path(folder).iterdir())
    if len(files) == 0:
        return False
    else:
        return True