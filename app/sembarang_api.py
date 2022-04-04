from fastapi import FastAPI, HTTPException
from mangum import Mangum
from sembarang import generate_branding_snippet, generate_keywords

app = FastAPI()
handler = Mangum(app)
MAX_INPUT_LENGTH = 32

@app.get("/generate_snippet")
async def generate_branding_snippet_api(prompt: str):
    validasi_panjang_input(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keyword": []}

@app.get("/generate_keyword")
async def generate_keywords_api(prompt: str):
    validasi_panjang_input(prompt)
    keyword = generate_keywords(prompt)
    return {"snippet": None, "keyword": keyword}

@app.get("/generate_snippet_keyword")
async def generate_keywords_api(prompt: str):
    validasi_panjang_input(prompt)
    snippet = generate_branding_snippet(prompt)
    keyword = generate_keywords(prompt)
    return {"snippet": snippet, "keyword": keyword}

def validasi_panjang_input(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400, 
            detail=f"Input terlalu panjang. Maksimal {MAX_INPUT_LENGTH}")
#uvicorn sembarang_api:app --reload