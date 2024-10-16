# Python base image
FROM python:3.10-slim

# Setting envs so python don't buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copying requirements.txt to dir
COPY requirements.txt /app/

# Dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Downloading the Hugging Face model and tokenizer
RUN python -c "from transformers import AutoTokenizer, AutoModelForTokenClassification; \
                AutoTokenizer.from_pretrained('CyberPeace-Institute/SecureBERT-NER'); \
                AutoModelForTokenClassification.from_pretrained('CyberPeace-Institute/SecureBERT-NER');"

# Copying FastAPI app to dir
COPY ner_service_fastapi.py /app/

# FastApi port
EXPOSE 8000

# Run
CMD ["uvicorn", "ner_service_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
