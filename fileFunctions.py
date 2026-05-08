import subprocess
import os

#Pulls the files from tailscale's tail drop
def pullFiles():
    subprocess.run(["tailscale", "file", "get", "audio/incoming"])


def checkForAudio():
    folder_path = './audio/incoming'
    file_names = os.listdr(folder_path)
    print()

def moveFiles():