import os
from typing import List
import openai
import argparse
import re

MAX_INPUT_LENGTH = 32

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User Input: {user_input}")
    if validasi_panjang(user_input):
        generate_branding_snippet(user_input)
        generate_keywords(user_input)
    else:
        raise ValueError(
            f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}"
        )

def validasi_panjang(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH


def generate_keywords(prompt: str) -> List[str]:
    #Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt_apik = f"Generate related branding keywords for {prompt}:"
    print(prompt_apik)
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt_apik, max_tokens=32)
    
    #Extract output text
    teks_keyword: str = response["choices"][0]["text"]

    #Strip Whitespace,
    teks_keyword = teks_keyword.strip()
    keyword_array = re.split(",|\n|;|-", teks_keyword)
    keyword_array = [k.lower().strip() for k in keyword_array]
    keyword_array = [k for k in keyword_array if len(k) > 0]

    print(f"Hasil : {keyword_array}")

    return keyword_array


def generate_branding_snippet(prompt: str)->str:
    #Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt_apik = f"Generate upbeat branding snippet for {prompt}:"
    print(prompt_apik)
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt_apik, max_tokens=32)
    
    #Extract output text
    teks_brand: str = response["choices"][0]["text"]

    #Strip Whitespace,
    teks_brand = teks_brand.strip()

    #Add ... Truncated statement
    last_char = teks_brand[-1]
    if last_char not in {".","!","?"}:
        teks_brand += "..."

    print(f"Snippet : {teks_brand}")
    return teks_brand


if __name__ == "__main__":
    main()