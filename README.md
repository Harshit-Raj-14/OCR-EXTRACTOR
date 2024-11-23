# OCR-EXTRACTOR
## Team : FullMetal Algorithmist

**Pitch Desk** - https://www.canva.com/design/DAGXOGByQoE/R9E2iof2VTXyCPCfyC4hqA/edit?utm_content=DAGXOGByQoE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

# OCR and LLM Integration with RAG

## Introduction
In the modern digital age, data is stored and represented in various formats such as PDFs, JPGs, and PNGs. While humans can easily understand this data, machines often struggle to interpret it. Optical Character Recognition (OCR) bridges this gap by recognizing patterns in images and converting them into machine-readable formats. However, OCR alone has limitations, such as inaccuracies in differentiating between similar characters (e.g., 'O' and '0') or dealing with unstructured data.

To overcome these challenges, we integrated OCR with Large Language Models (LLMs) enhanced by a **Retrieval-Augmented Generation (RAG)** system. This combination ensures improved accuracy and relevance in text extraction and processing, especially in complex or domain-specific scenarios.

## Features
### OCR Integration
- Converts images into text using advanced preprocessing techniques:
  - **Bitmap conversion**
  - **Grayscale transformation**
  - **Noise removal**
  - **Thresholding**

### LLM Augmentation
- Improves OCR output by:
  - Differentiating between visually similar characters
  - Structuring unstructured data into meaningful formats
- Provides context-aware insights by understanding extracted text.

### RAG Implementation
- Introduces a **contextual data store** to improve LLM accuracy.
- Ensures the LLM provides outputs only from the relevant information.
- Reduces computational costs by eliminating the need for frequent retraining.
- Mitigates hallucination issues by grounding LLM outputs in the provided context.


## Demo
https://github.com/Harshit-Raj-14/OCR-EXTRACTOR/blob/main/demo1.mkv

https://github.com/Harshit-Raj-14/OCR-EXTRACTOR/blob/main/demo2.mkv

## System Design
![System Design - Medical Diagnosis Extraction](https://github.com/user-attachments/assets/c2c1072c-be58-40de-a6c8-5b7d3ba43917)


## Installation
- Enter the main project
> cd MAIN PROJECT - medical-data-extractor

- Install all dependancies from `requirements.txt`
> pip install -r requirements.txt

- For `pdf2image` you need to [download `poppler`](https://github.com/oschwartz10612/poppler-windows/releases/)
  
- Install Tesseract OCR Engine in your PC
    - [Tesseract installation instrution : Github](https://github.com/tesseract-ocr/tesseract#installing-tesseract)

- Set required PATHs for poppler and teserract in your environment variables

- Running Backend
> cd backend/src

> python main.py

- Running Frontend
> Open new terminal

> streamlit run frontend/app.py


## Project Images
![vlcsnap-2024-11-24-03h36m07s620](https://github.com/user-attachments/assets/79e6f992-d78f-47d5-9070-080dcb39c396)

<hr>

![vlcsnap-2024-11-24-03h36m14s491](https://github.com/user-attachments/assets/0fc142f6-c680-4a1e-959d-ec7eb3723e40)

<hr>

![vlcsnap-2024-11-24-03h36m28s185](https://github.com/user-attachments/assets/f4ce15d3-5725-4c9f-9978-26c66c1f644e)





















