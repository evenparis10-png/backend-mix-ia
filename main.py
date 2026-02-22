from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/mix")
async def mix_audio(file: UploadFile = File(...)):
    content = await file.read()

    return Response(
        content=content,
        media_type="audio/mpeg"
    )
