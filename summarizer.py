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
    print("Begin Summary", flush = True)

    with open(transcriptPath, "r") as file:
        transcriptText = file.read()

    summary = ollama.generate(
        model = "llama3.2:3b",
        prompt = PROMPT_TEMPLATE.format(transcript = transcriptText),
        stream = True
    )

    with open(sumText, "w", encoding="utf-8") as f:
        for chunk in summary:
            text = chunk["response"]

            print(text, end="", flush=True)
            f.write(text)

    end_time = time.perf_counter()

    print("Summary saved to: " + sumText, flush = True)

    print(f"Elapsed time: {end_time - start_time:.4f} seconds")

