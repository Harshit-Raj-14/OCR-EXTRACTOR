import cv2
import pytesseract

img = cv2.imread('img.png')

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# remove noise -> some pixels are extra and makee the image sharp
def remove_noise(image):
    return cv2.medianBlur(image, 5)     # 5 is gradient

# thresholding -> pixel black and white based on above or below threshold -> to get concrete black and white image
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = get_grayscale(img)
img = remove_noise(img)
img = thresholding(img)

print(ocr_core(img))