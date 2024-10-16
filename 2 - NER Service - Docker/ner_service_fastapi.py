from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import torch
import numpy as np


# Input model
class TextRequest(BaseModel):
    text: str


# Initializing
app = FastAPI()

# Loading the pre-trained model and tokenizer from Hugging Face
MODEL_NAME = "CyberPeace-Institute/SecureBERT-NER"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForTokenClassification.from_pretrained(MODEL_NAME)

device = 0 if torch.cuda.is_available() else -1  # -1 == CPU

ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="first", device=device)


@app.post("/ner")
async def extract_entities(text_request: TextRequest):
    """Extract named entities from text."""

    text = text_request.text
    if not text:
        raise HTTPException(status_code=400, detail="Text must be provided.")

    try:

        entities = ner_pipeline(text)

        # Converting numpy types to native types - for JSON
        for entity in entities:
            if isinstance(entity.get('score'), np.float32):
                entity['score'] = float(entity['score'])

        return {"entities": entities}

    except Exception as e:
        # Error handling
        print(f"Error during NER processing: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error during NER processing.")

