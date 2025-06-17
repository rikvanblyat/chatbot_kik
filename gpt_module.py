import openai
import os
from dotenv import load_dotenv

# Load API key dari .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(question, context=None):
    """
    Hantar soalan ke GPT-4 Turbo dan terima jawapan dalam nada profesional kerajaan.
    """
    base_prompt = "Anda ialah pembantu maya profesional untuk jabatan kerajaan Malaysia. Jawab dengan nada sopan, tepat dan padat."

    messages = [{"role": "system", "content": base_prompt}]

    if context:
        messages.append({"role": "user", "content": f"Konteks: {context}"})

    messages.append({"role": "user", "content": question})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=messages,
            temperature=0.3,
            max_tokens=500
        )
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"Maaf, berlaku ralat: {str(e)}"
