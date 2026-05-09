import ollama
import time
from prompt import PROMPT_TEMPLATE
from pathlib import Path




def summarize():
    TRANSCRIPTS = Path("audio/transcripts")
    SUMMARIES = Path("audio/summaries")

    files = [f for f in TRANSCRIPTS.iterdir() if f.suffix == ".txt"]
    transcriptPath = files[0]

    sumText = SUMMARIES / f"{transcriptPath.stem} SUM.txt"

    start_time = time.perf_counter()

    with open(transcriptPath, "r") as file:
        transcriptText = file.read()

    summary = ollama.generate(
        model = "llama3.2:3b",
        prompt = PROMPT_TEMPLATE.format(transcript = transcriptText)
    )

    with open(sumText, "w", encoding="utf-8") as f:
        f.write(summary["response"])

    end_time = time.perf_counter()

    print("Summary saved to: " + sumText)

    print(f"Elapsed time: {end_time - start_time:.4f} seconds")

