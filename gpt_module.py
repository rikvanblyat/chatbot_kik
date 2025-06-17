from openai import OpenAI
import os

# Terus baca API key dari environment (Streamlit Secrets)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(question, context=None):
    """
    Hantar soalan ke GPT-3.5 Turbo dan terima jawapan dalam nada profesional kerajaan.
    """
    base_prompt = "Anda ialah pembantu maya profesional untuk jabatan kerajaan Malaysia. Jawab dengan nada sopan, tepat dan padat."

    messages = [{"role": "system", "content": base_prompt}]

    if context:
        messages.append({"role": "user", "content": f"Konteks: {context}"})

    messages.append({"role": "user", "content": question})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Maaf, berlaku ralat: {str(e)}"
