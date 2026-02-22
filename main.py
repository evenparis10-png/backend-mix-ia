from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydub import AudioSegment
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/mix")
async def mix_audio(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    # Lire les fichiers
    audio1 = AudioSegment.from_file(io.BytesIO(await file1.read()))
    audio2 = AudioSegment.from_file(io.BytesIO(await file2.read()))

    # Mix basique (superposition)
    mixed = audio1.overlay(audio2)

    # Export en MP3
    buffer = io.BytesIO()
    mixed.export(buffer, format="mp3")
    buffer.seek(0)

    return Response(content=buffer.read(), media_type="audio/mpeg")
