import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from cerebras.cloud.sdk import Cerebras

app = FastAPI()

client = Cerebras(
    # This is the default and can be omitted
    api_key=os.environ.get("CEREBRAS_API_KEY")
)

@app.get("/")
async def generate_html():
    def generate():
        stream = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You're a text to html converter. Read the user input and create an HTML based on the user description. Be creative and use your own style, css, structure, etc. Reprase the content to make it more interesting and engaging. Do not import or use external libraries, all the CSS and Javascript should be written in the base HTML. Please deliver the response in plain text without any Markdown or formatting. Provide the output as raw text."
                },
                {
                    "role": "user",
                    "content": "Crea un HTML con distintos colores y estilos según tu criterio, manten algo básico y funcional. El contenido del sitio se detallará a continuación, aunque no debe estar escrito exactamente igual. Expande cada frase para que sea más interesante y atractiva. \nTitulo: Este sitio no existe.\nHola, soy Eduardo Aguad (eduaguad en redes sociales) y me dedico a mostrar conceptos de programación de forma básica. Este sitio web no existe y cada vez que ingreses será generado automáticamente. Aunque parezca mentira, ninguna versión es igual a la anterior. Este sitio está siendo generado por un modelo de IA de forma brutalmente rápida. "
                },
            ],
            model="llama-4-scout-17b-16e-instruct",
            stream=True,
            max_completion_tokens=2048,
            temperature=1.5,
            top_p=0.8
        )

        for chunk in stream:
            content = chunk.choices[0].delta.content or ""
            if content:
                yield content

    return StreamingResponse(generate(), media_type="text/html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)