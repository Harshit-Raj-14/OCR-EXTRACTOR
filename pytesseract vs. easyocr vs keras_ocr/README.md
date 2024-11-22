## Requirements

    pip install -r requirements.txt
    
## Usage

    python main.py
    
 Also you can check the result by one by like:

You have to initilaze your object.  

    ocr=OCR(image_folder="test/")  

After that, for **keras ocr**:  

    ocr.keras_ocr_works()
    
for **easyocr**:

    ocr.easyocr_model_works()  
for **pytesseract**:

    ocr.pytesseract_model_works()

 ## Results

 
 ## Conclusion
1. **Pytesseract**:
   - Struggles with detecting text across the entire image and converting it to a string.
   - More effective when text detection is done first and then OCR engines are applied to the detected text regions.
   - Performs well on high-resolution images.
   - Performance can be enhanced with morphological operations such as dilation, erosion, and OTSU binarization.

2. **Keras-OCR**:
   - Offers high accuracy but is time-consuming, especially when using CPU.
   - Best suited for images with well-organized text, such as clear fonts and colors.
   - Works well with images where text is inside and clearly defined, but may struggle with disorganized fonts and colors.

3. **Easy-OCR**:
   - Lightweight and efficient, providing good performance for receipt and PDF conversion.
   - Excels with organized text, like PDFs, receipts, and bills.
   - Performs well on noisy images, offering a good balance between speed and accuracy.

4. **General OCR Performance**:
   - OCR accuracy depends on various factors such as image clarity, grayscale properties, hyperparameters, and weightings.
   - Specific image pre-processing operations can significantly improve OCR results.
   - The choice of OCR model should be influenced by the type of image (organized vs. noisy) and the specific task (receipt, PDF, etc.).
