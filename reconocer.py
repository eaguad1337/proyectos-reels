

import streamlit as st
from PIL import Image

from transformers import CLIPProcessor, CLIPModel

st.title("Reconocimiento de frutas")

def zero_shot_classification(image):
    model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")

    # Convert UploadedFile to PIL Image
    pil_image = Image.open(image)
    categories = ["avocado", "banana", "orange"]

    inputs = processor(
        text=categories,
        images=pil_image,
        return_tensors="pt",
        padding=True,
    )

    outputs = model(**inputs)
    logits_per_image = (
        outputs.logits_per_image
    )  # this is the image-text similarity score
    probs = logits_per_image.softmax(
        dim=1
    )  # we can take the softmax to get the label probabilities

    st.write(
        {
            categories[i]: float(probs[0][i]) for i in range(len(categories))
        }
    )




image = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

if image is not None:
    st.image(image, width=300)


if image is not None:
    if st.button("Detectar"):
        zero_shot_classification(image)
