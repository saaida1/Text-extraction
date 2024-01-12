import pytesseract
import os
from PIL import Image, ImageFilter, ImageOps


def extract_text_from_image(image_path):
    # Define the path to tessaract.exe
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

    # Define the path to image
    os.environ['TESSDATA_PREFIX'] = 'C:/Program Files/Tesseract-OCR/tessdata'

    # Open the image using PIL
    img = Image.open(image_path)

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

    return text
