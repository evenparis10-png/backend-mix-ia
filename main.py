from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autorise le front (Lovable) à appeler l’API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/mix")
async def mix_audio(file: UploadFile = File(...)):
    content = await file.read()
    return {
        "message": "fichier reçu",
        "size": len(content)
    }
