import pdfplumber
with pdfplumber.open(r'/home/ctw01911/Code/devops/python/pdf/af02.pdf') as pdf:
    first_page = pdf.pages[14]
    print(first_page.extract_text())