
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from pydantic import BaseModel

from chatbotapi import stream_ai_response
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import FileResponse

# ---------------- APP ----------------

app = FastAPI()

# first i added pip install python multipart
# now 

import uvicorn
import os

port = int(os.environ.get("PORT", 8000))

uvicorn.run(app, host="0.0.0.0", port=port)

@app.get("/")

async def root():
    return FileResponse("index.html")


app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)



# ---------------- REQUEST MODEL ----------------

class ChatRequest(BaseModel):
    message: str

# ---------------- CHAT ROUTE ----------------

@app.post("/chat")

async def chat(request: ChatRequest):

    generator = stream_ai_response(
        request.message
    )

    return StreamingResponse(
        generator,
        media_type="text/plain"
    )
