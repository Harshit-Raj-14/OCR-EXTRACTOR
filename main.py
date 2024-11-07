# run the script using - python main.py <image_path>
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
from PIL import Image
import pytesseract

from ocr.helpers import implt, resize
from ocr import page
from ocr import words

def process_folder(folder_path):
    filename = folder_path
    save_filename = "temp_ocr_image.jpg"

    image = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB)
    implt(image)

    crop = page.detection(image)
    implt(crop)

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)
    implt(gray)

    cv2.imwrite(save_filename, gray)

    text = pytesseract.image_to_string(Image.open(save_filename))
    os.remove(save_filename)
    print(text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process_folder(folder_path)

# run the script using - python main.py <image_path>
if __name__ == "__main__":
    main()


