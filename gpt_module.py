from openai import OpenAI
import os

# Terus baca API key dari environment (Streamlit Secrets)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(question, context=None):
    """
    Hantar soalan ke GPT-3.5 Turbo dan terima jawapan dalam nada profesional JANM.
    """
    base_prompt = (
        "Anda ialah Chatbot rasmi JANM Pulau Pinang. "
        "Tugas anda ialah memberi jawapan kepada soalan berkaitan prosedur kewangan dan perakaunan sektor awam, "
        "berdasarkan pekeliling seperti SPANM Bil.5/2023 dan peraturan kewangan semasa. "
        "Jawapan mestilah dalam nada formal, padat, sopan, dan membantu pelanggan membuat keputusan dengan tepat. "
        "Jika maklumat tidak dapat dijumpai secara terus dalam pekeliling, anda dibenarkan menjawab berdasarkan prinsip am kewangan awam, pendigitalan sektor kerajaan, serta kefahaman umum anda tentang sistem perkhidmatan awam. "
        "Jika soalan langsung tiada asas untuk dijawab, barulah berikan arahan berikut: "
        "'Sila hubungi Pegawai kami di JANM Pulau Pinang untuk maklumat lanjut.'"
    )

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
        return "Sila hubungi Pegawai kami di JANM Pulau Pinang untuk maklumat lanjut."
