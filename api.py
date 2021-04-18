import uvicorn
from fastapi import FastAPI
import TTS as tts
from playsound import playsound

app = FastAPI()


@app.get("/play/{sentence}/{freq}")
def get_speech(sentence: str, freq: int):
    tts.output_file(sentence, freq)
    playsound("output.wav")


@app.get("/{sentence}/{freq}")
def get_speech(sentence: str, freq: int):
    tts.output_file(sentence, freq)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
