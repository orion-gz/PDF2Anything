# Package installation
# pip install -r requirements.txt
# or 
# pip install pdf2image

from pdf2image import convert_from_path

# pdf file must be in your project path.
PDF_FILE_PATH = "*.pdf"

def pdf_to_jpg():
    pages = convert_from_path(PDF_FILE_PATH)
    for i, page in enumerate(pages):
        # you can change the image type.
        page.save(f"./img/{str(i)}.jpg", "JPEG")
        
if __name__ == '__main__':
    pdf_to_jpg()