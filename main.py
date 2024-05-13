from PyPDF2 import PdfWriter, PdfReader
import getpass

pdfwriter = PdfWriter()

pdf = PdfReader("./3.pdf")
print(pdf)
for page_num in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page_num])

passw = getpass.getpass(prompt='Enter password: ')
pdfwriter.encrypt(passw)

with open('ho.pdf', 'wb') as f:
    pdfwriter.write(f)
