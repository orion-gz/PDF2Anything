# Package installation
# pip install -r requirements.txt
# or 
# pip install pytesseract
# pip install Pillow

# If you use this feature you also need to install tesseract
# installation guide 
# Windows : https://github.com/UB-Mannheim/tesseract/wiki
# MacOS : brew install tesseract

import pytesseract
from PIL import Image
import os
import natsort
import sys

# You must specify the full path to the tesseract executable.
# In Linux(Also MacOS), you can get this by using the command:
# which tesseract
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

def text_to_txt_file(text, file_name):
    with open(file_name, "w") as f:
        f.write(text)
    
def img_to_text(argv):
    text = ""

    # Sort the files using natsorted function.
    for filename in natsort.natsorted(os.listdir("./img/")):
        if str(filename) not in ['.', '..']:
            nameParts = str(filename).split(".")
            print(nameParts)
        if nameParts[-1].lower() in ["gif", "png", "jpg", "jpeg", "tif", "tiff"]:
    # Calls to the API should always be bounded by a timeout, just in case.
            try:
                print ("Found filename [" + str(filename) + "]")
                ocrText = pytesseract.image_to_string("./img/" + str(filename))
                text += ocrText
            except Exception as err:
                print ("Processing of [" + str(filename) + "] failed due to error [" + str(err) + "]")
        text_to_txt_file(text, "*.txt")

if __name__ == "__main__":
    img_to_text(sys.argv[1:])