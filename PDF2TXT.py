# Package installation
# pip install -r requirements.txt
# or 
# pip install pdfplumber

import pdfplumber

# pdf file must be in your project path.
PDF_FILE_PATH = "*.pdf"

# you can specify a starting page.
INDEX_OF_PAGE = 202

def text_to_txt_file(text, file_name):
    with open(file_name, "w") as f:
        f.write(text)


def pdf_to_text():
    text = ""
    with pdfplumber.open(PDF_FILE_PATH) as pdf:
        pages = pdf.pages
        for index in range(INDEX_OF_PAGE, len(pages)):
            page = pdf.pages[index]
            sub = page.extract_text()
            text += sub
        text_to_txt_file(text, "*.txt")

if __name__ == '__main__':
    pdf_to_text()