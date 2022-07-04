from fastapi import FastAPI, HTTPException
from mangum import Mangum
from sembarang import generate_branding_copywrite, generate_keywords
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app)
MAX_INPUT_LENGTH = 32

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_copywrite")
async def generate_branding_copywrite_api(prompt: str):
    validasi_panjang_input(prompt)
    copywrite = generate_branding_copywrite(prompt)
    return {"copywrite": copywrite, "keyword": []}

@app.get("/generate_keyword")
async def generate_keywords_api(prompt: str):
    validasi_panjang_input(prompt)
    keyword = generate_keywords(prompt)
    return {"copywrite": None, "keyword": keyword}

@app.get("/generate_copywrite_and_keywords")
async def generate_keywords_api(prompt: str):
    validasi_panjang_input(prompt)
    copywrite = generate_branding_copywrite(prompt)
    keywords = generate_keywords(prompt)
    return {"copywrite": copywrite, "keywords": keywords}

def validasi_panjang_input(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400, 
            detail=f"Input is too long. Enter max {MAX_INPUT_LENGTH} character")
#uvicorn sembarang_api:app --reload