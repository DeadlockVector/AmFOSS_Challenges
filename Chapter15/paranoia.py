import os
import PyPDF2 as pdf
#import sys

#password = sys.argv[-1]
password = 'password'

list_pdfs = []
for foldername, subfolders, filenames in os.walk('home/isocyanate/test_PdfParanoia'):
    for filename in filenames:
        if filename.endswith('pdf'):
            list_pdfs.append(os.path.join(foldername, filename))

for i in list_pdfs:
    path = open(i, 'rb')
    reader = pdf.PdfFileReader(path)
    writer = pdf.PdfFileWriter(path)

    name = os.path.basename(i)
    print(name)

    if reader.isEncrypted == False:
        writer.encrypt(password)

#TODO: check encryption
#open file again with password
#let user know if file can't open
