import pytesseract
import os
import cv2
from PIL import Image, ImageFilter, ImageOps


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\SunShine\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Users\SunShine\AppData\Local\Programs\Tesseract-OCR\tessdata'
# Open the image using PIL
img = Image.open('photo-inside-text.jpg')
# set configurations
config: str = ('-l eng --oem 1 --psm 3')
# Convert to grayscale
img = img.convert('L')
# Enhance the image to improve its quality
img = ImageOps.autocontrast(img)
# Apply a median filter to remove noise
img = img.filter(ImageFilter.MedianFilter())  # filter is to remove noise and smooth out any rough edges.
# Invert the colors
img = ImageOps.invert(img)  # If the colors of the text and the background are not optimal for OCR.
text = pytesseract.image_to_string(img, lang='eng')
# preserve_interword_spaces=1 preserve_interline_spaces=1
# Open a new file and write the extracted text to it
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text)
print(text)
