# Optical character recognition using pytesseract



## OCR 
- Optical character recognition or optical character reader, often abbreviated as OCR, is the mechanical or electronic conversion of images of typed, handwritten or printed text into machine-encoded text, whether from a scanned document, a photo of a document, a scene-photo .

## Pytesseract 
- Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.

- Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Python Imaging Library, including jpeg, png, gif, bmp, tiff, and others, whereas tesseract-ocr by default only supports tiff and bmp. Additionally, if used as a script, Python-tesseract will print the recognized text instead of writing it to a file.

## How to run the programm

1. create the virtual enveiroment in the directory

```
 python3 -m venv myvenv 
```

2. to activate the virtual enviroment 

```
source myvenv /bin/activate
```

3. Required libs need to be installed 

``` 
pip install -r requirements.txt
```

4. Now, run the main program by the command 

```
python text_recognition.py --east frozen_east_text_detection.pb --image test.png --padding 0.01
```

5. boom !! the output is here 

