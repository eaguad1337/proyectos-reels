import re
import os
from imapclient import IMAPClient
from cerebras.cloud.sdk import Cerebras

EMAIL = os.environ.get("GMAIL_ADDRESS")
APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

def explicar_correo(body):
    CEREBRAS_API_KEY = os.environ.get("CEREBRAS_API_KEY")
    client = Cerebras(api_key=CEREBRAS_API_KEY)

    result = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente que se dedica a resumir correos. Indica si el correo es una promoción o si es un correo de trabajo según el correo que envíe el usuario.",
            },
            {
                "role": "user",
                "content": body[:8000],
            }
        ],
        model="llama-4-scout-17b-16e-instruct",
        stream=False,
        max_completion_tokens=2048,
        temperature=0.2,
        top_p=1,
    )
    return result.choices[0].message.content

with IMAPClient("imap.gmail.com", ssl=True) as server:
    print("Conectando a Gmail...")
    server.login(EMAIL, APP_PASSWORD)
    server.select_folder("INBOX")
    messages = server.search(["UNSEEN"])
    print(f"Se encontraron {len(messages)} emails no leídos")

    if not messages:
        print("No hay emails no leídos.")
        exit

    mensajes_limitados = messages[:5]

    # Iterar sobre los emails no leídos
    for uid, datos in server.fetch(
        mensajes_limitados, ["ENVELOPE", "BODY[TEXT]"]
    ).items():
        envelope = datos[b"ENVELOPE"]
        asunto = envelope.subject.decode()
        desde = envelope.from_[0]
        emisor = f"{desde.mailbox.decode()}@XXXXXXXX"
        print(f"De: {emisor}")
        print(f"Asunto: {asunto}")
        print("====================")
        body = datos[b"BODY[TEXT]"].decode("utf-8")
        body = re.sub(r"<[^>]*>", "", body)
        body = "\n".join(line.strip() for line in body.splitlines() if line.strip())
        print(body)
        print("====================")
        print(explicar_correo(body))