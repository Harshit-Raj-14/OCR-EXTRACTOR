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
