from fastapi import FastAPI, HTTPException
from mangum import Mangum


app = FastAPI()
handler = Mangum(app)

from sembarang import generate_branding_snippet, generate_keywords

app = FastAPI()
MAX_INPUT_LENGTH = 32

@app.get("/generate_snippet_api")
async def generate_branding_snippet_api(prompt: str):
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keyword": []}

@app.get("/generate_keyword_api")
async def generate_keywords_api(prompt: str):
    keyword = generate_keywords(prompt)
    return {"snippet": None, "keyword": keyword}

@app.get("/generate_snippet_keyword_api")
async def generate_keywords_api(prompt: str):
    validasi_panjang_input(prompt)
    snippet = generate_branding_snippet(prompt)
    keyword = generate_keywords(prompt)
    return {"snippet": snippet, "keyword": keyword}

def validasi_panjang_input(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400, 
            detail=f"Input length is too long. Can only support {MAX_INPUT_LENGTH} Characters")
#uvicorn sembarang_api:app --reload