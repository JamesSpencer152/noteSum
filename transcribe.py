from faster_whisper import WhisperModel
from pathlib import Path

processing = Path("audio/processing")
transcripts = Path("audio/transcripts")
files = list(processing.iterdir())
current = files[0]
currentTxt = transcripts / current.with_suffix(".txt")
model = WhisperModel("small", device = "cpu", compute_type = "int8")



segments, info = model.transcribe(current, beam_size = 5)

with open(currentTxt, "w", encoding="utf-8") as f:
    for segment in segments:
        f.write(segment.text + "\n")
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

print("transcription saved to ", currentTxt)