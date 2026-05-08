from faster_whisper import WhisperModel
from pathlib import Path

folder = Path("audio/processing")
files = list(folder.iterdir())
current = files[0]
currentTxt = current.with_stem(current.stem + ".txt")
model = WhisperModel("small", device = "cpu", compute_type = "int8")



segments, info = model.transcribe(current, beam_size = 5)

with open(currentTxt, "w", encoding="utf-8") as f:
    for segment in segments:
        f.write(segment.text + "\n")
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

print("transcription saved to ", currentTxt)