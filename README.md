# OCR-EXTRACTOR
## Team : FullMetal Algorithmist

**Pitch Desk** - https://www.canva.com/design/DAGVzi19Y2s/FnQFxSlvWKFh8cNZe03oBQ/edit?utm_content=DAGVzi19Y2s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Table of Contents 
1. [Introduction](#1-introduction)
2. [System Design](#2-system-design) 
3. [Workflow](#3-workflow) 
4. [Technologies Used](#4-technologies-used)
5. [Key Features](#5-key-features)
6. [Image Processing](#6-image-processing) 
7. [After Preprocessing: Image Data Extraction](#7-after-preprocessing-the-image-data-extraction) 
8. [Notebook](#8-notebook) 

## 1. Introduction :
- This project is to implement OCR data extraction, and this project will auto classify and extract useful information from documents.
- Implemented this project by using libraries - Pytesseract(Runs On Google Optical Character Recognition-OCR), Computer Vision, Regex, PDF2Image, LLM, AI.
- Applied use of LLM as word dictionary to easily recognise words and automatically fix them.
- At first we use PDF2Image library to convert PDF into image, clean the image with Computer Vision by Adaptive Thresholding Techinique and extract useful data by using Pytesseract(OCR) and regex.
- This project works well on legal document analysis, medical records processing, or invoice reading (like extracting name, patient details, medicine, diagonosis, legal rules, price tags, amount) and this saves time as it reduces human work and saves time from 10 min to less than a second.

## 2. System Design
![system design](https://github.com/user-attachments/assets/bef32bb2-a86a-4df9-981c-24e2155403d0)

## 3. Workflow
![data flow](https://github.com/user-attachments/assets/b3771cd0-de0a-4660-b7db-1668dfad7fb3)

## 4. Technologies used
- Python
- Pdf2image module
- Opencv
- pytesseract
- Regular expression
- RAG Model
- LLM
- Postman
- FastApi


# 5. Key Features
### **High Accuracy with OCR Extraction**
* Leverages advanced Computer Vision techniques like OCR and pytesseract extraction.
* Focuses on relevant sections of handwritten documents as well.
* Ensures precise data capture.

### **Regex for Comprehensive Data Extraction**
* Uses advanced Regex patterns.
* Extracts detailed information based on asked paramters from the documents and it type.
* Enhances the depth of insights from documents.

### **Error Correction for Improved Reliability**
* Integrates an error correction mechanism.
* Uses a medical vocabulary model to predict and correct handwritten text errors.
* Ensures higher accuracy in critical data fields like medicine names.
* Uses RAG model and LLM to get the right output from the extracted text.


## 6. Image processing
![1](https://github.com/user-attachments/assets/6aabfb1b-4df2-4293-8728-50780478b725)

We initially chose to preprocess the images using OpenCV, starting with normal thresholding. However, this method can cause areas with shadows or noise to fade out, leading to data loss.

To improve our approach, we decided to switch to adaptive thresholding. This technique divides the image into smaller regions, applying different threshold values to each. As a result, adaptive thresholding produces significantly better outcomes compared to normal thresholding.

![image](https://github.com/user-attachments/assets/d32ff5e8-2c93-4d6a-be40-a7dc1d2768f0)



## 7. After preprocessing the image data extraction

C. Nature of Illness / Disease with presenting complaint: CHRONIC IVER DISEASE; PEDAL EDEMA ORAMPS f
D. Relevant Critical Findings: JAUNDICE, PEDAL EDEME
E. Duration of the present ailment: 1 year Days
i. Date of First consultation: 8/1/24.
(DD/MM/YYYY)
H. Past history of present allment, if any Detected as CAD & yeast ago elsewhere.
Provisional diagnosis: DECOMPENSATED CHRONIC IVER DIRGALE.
1. ICD 10 code
F.
G. Proposed line of treatment:
1. Medical Management
ii. Surgical Management
ii. Intensive care
iv. Investigation
()
V. Non-allopathic treatment ()
H. If Investigation and/or Medical Managernent, provide details
1. Route of Drug Administration:
If surgical, narne of surgery TRANSPLANTATION.
i. ICD 10 PCS code
J. If other treatment, provide details
K. How did injury occur
      
## 8. Notebook
For all these above trials, used jupyter books and developed the small bits of the functionalities., which can be used later while designing the class.

[Notebooks](https://github.com/Harshit-Raj-14/OCR-EXTRACTOR/blob/main/Notebooks/OCR%20Notebook.ipynb)
