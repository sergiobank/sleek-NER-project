# NER Benchmarking and Deployment Project

This project benchmarks a Named Entity Recognition (NER) model, namely the SecureBERT-NER HuggingFace pretrained model,
using the DNRTI dataset.
The goal is to evaluate the model against the dataset (1), build and run a FastApi based NER Service Docker Container (2)
and provide a user-friendly interface for entity extraction from text files (3).

## Table of Contents
- [Overview](#overview)
- [Structure](#structure)
- [Benchmarking](#benchmarking)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Docker Container](#running-the-docker-container)
  - [Using the Streamlit Web Interface](#using-the-streamlit-web-interface)

## Overview
The project focuses on:
1. **Benchmarking Analysis**: Evaluating the SecureBERT-NER model on the DNRTI dataset using precision and recall metrics.
2. **NER Service Deployment**: Creating a Docker container to deploy the selected NER model, ensuring it runs on-prem with offline capabilities.
3. **Web Interface**: Developing a Streamlit web application that allows users to upload text files and receive a report on the identified named entities.

DISCLAIMER: The project is divided into 3 directories, each one comprising of one part of
the project. All 3 parts of the project contain a Jupyter Notebook with step-by-step
explanation, so all the details will be explained in the respective notebooks.

## Structure

```bash
├── 1 - Benchmarking Analysis
│   ├── data
│   │   └── DNRTI                          # DNRTI dataset
│   │       ├── test.txt                   
│   │       ├── train.txt                  
│   │       └── valid.txt                  
│   └── NER_benchmark_analysis.ipynb       # Jupyter notebook for evaluating model
├── 2 - NER Service - Docker
│   ├── Dockerfile                         # Dockerfile to build the container for the NER service
│   ├── NER_docker_service.ipynb           # Jupyter notebook for explaining the NER Docker service code
│   ├── ner_service_fastapi.py             # FastAPI-based service for the NER model
│   ├── ner_service_image.tar              # Prebuilt Docker image for the NER service
│   └── requirements.txt                   # Python dependencies for the Docker service
├── 3 - Web Development - Streamlit
│   ├── NER_streamlit.ipynb                # Jupyter notebook for explaining the Streamlit web app code
│   ├── example_sentences.txt              # Sample sentences for testing the Streamlit application
│   ├── ner_streamlit_app.py               # Streamlit web app
│   ├── result_screenshot_1.png            # Streamlit Screenshot
│   ├── result_screenshot_2.png            # Streamlit Screenshot
│   └── sleek_logo.png                     
├── README.md                              # Docs
└── requirements.txt                       
```

## Benchmarking
The benchmarking analysis compares the performance of SecureBERT-NER based on:
- **Latency**: Time taken to process a batch of text.
- **Precision**: The percentage of correctly identified entities out of all predicted entities.
- **Recall**: The percentage of correctly identified entities out of all true entities.

## Installation

### Prerequisites
- Python 3.10+
- Docker
- Streamlit

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/sergiobank/sleek-NER-project.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Build the Docker container:
    ```bash
    docker build -t ner_service_fastapi .
    ```

## Usage

### Running the Docker Container
1. Start the container:
    ```bash
    docker run -p 8000:8000 ner_service_fastapi
    ```
2. Send a POST request to the API to extract entities:
    ```bash
   curl -X POST http://localhost:8000/ner
   -H "Content-Type: application/json"
   -d '{"text": "Kaspersky believes both Shamoon and StoneDrill groups are aligned in their interests."}'
    ```

### Using the Streamlit Web Interface
1. Run the Streamlit app:
    ```bash
    streamlit run ner_streamlit_app.py --theme.base dark
    ```
2. Upload a text file through the interface to see extracted named entities. An example
is provided in the directory 3 - Web Development - Streamlit under the name example_sentences.txt.

![result_screenshot_1.png](3%20-%20Web%20Development%20-%20Streamlit%2Fresult_screenshot_1.png)

![result_screenshot_2.png](3%20-%20Web%20Development%20-%20Streamlit%2Fresult_screenshot_2.png)
