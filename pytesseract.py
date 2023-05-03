import pytesseract
import os
from PIL import Image, ImageFilter, ImageOps

# Define the path to tessaract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\SunShine\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Define the path to image
os.environ['TESSDATA_PREFIX'] = r'C:\Users\SunShine\AppData\Local\Programs\Tesseract-OCR\tessdata'

# Open the image using PIL
img = Image.open('tale.webp')

# Set conf of the OCR Engine Mode & Page Segmentation Mode
config: str = ('-l ara+fra+eng --oem 1 --psm 3')

# Convert to grayscale
img = img.convert('L')

# Enhance the image to improve its quality.
img = ImageOps.autocontrast(img)

# remove noise
img = img.filter(ImageFilter.MedianFilter())

# Apply a filter if the colors of the text and the background are not optimal for OCR
img = ImageOps.invert(img)  

text = pytesseract.image_to_string(img, lang='ara+fra+eng')

# Open a new file and write the extracted text to it
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text)

# Print the extracted text
print(text)
