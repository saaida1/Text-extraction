# Text Extraction from Image

## Overview

This Python script utilizes the Tesseract OCR (Optical Character Recognition) engine along with the Pillow (PIL) library to extract text from images. The script processes the image by converting it to grayscale, enhancing its quality, removing noise, and applying filters to improve OCR accuracy.

## Prerequisites

- Ensure you have Tesseract OCR installed on your system. You can download it from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
- Install the required Python libraries using the following:
  ```bash
  pip install pytesseract
  pip install Pillow

## Setup
1. Define the path to the Tesseract executable (`tesseract_cmd`) and the Tesseract data folder (`TESSDATA_PREFIX`) in the script.
 ```python
 pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
 os.environ['TESSDATA_PREFIX'] = 'C:/Program Files/Tesseract-OCR/tessdata'
```
## Usage

1. Call the `extract_text_from_image` function with the path to the image you want to process.
   ```python
   image_path = 'path/to/your/image.png'
   result_text = extract_text_from_image(image_path)
   print(result_text)
   ```

## Image Processing Steps

1-Open the image using PIL.
2-Convert the image to grayscale.
3-Enhance the image quality using autocontrast.
4-Remove noise using a median filter.
5-Invert the image colors if needed for optimal OCR.

## Note
Ensure the correct path to Tesseract OCR and its data is provided.
Adjust language parameters in the OCR configuration for your specific use case.
Experiment with additional image processing techniques based on the characteristics of your images for improved OCR results.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or bug fixes.

