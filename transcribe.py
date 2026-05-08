from faster_whisper import WhisperModel
from pathlib import Path
from fileFunctions import moveFile
import time

start_time = time.perf_counter()

PROCESSING = Path("audio/processing")
TRANSCRIPTS = Path("audio/transcripts")
PROCESSED = Path("audio/processed")

files = [f for f in PROCESSING.iterdir() if f.suffix == ".m4a"]
current = files[0]

currentTxt = TRANSCRIPTS / current.with_suffix(".txt").name

model = WhisperModel("base", device = "cpu", compute_type = "int8")

start_time = time.perf_counter()

segments, info = model.transcribe(current, beam_size = 5)

with open(currentTxt, "w", encoding="utf-8") as f:
    for segment in segments:
        f.write(segment.text + "\n")
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

print("transcription saved to ", currentTxt)

moveFile(current, PROCESSED)

end_time = time.perf_counter()

print(f"Elapsed time: {end_time - start_time:.4f} seconds")