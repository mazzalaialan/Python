import PyPDF2
import os
os.chdir('c:\\users\\alan\\documents')
pdfFile = open('meetingminutes1.pdf','rb')
reader = PyPDF2.PdfFileReader(pdfFile)
page = reader.getPage(0)
page.extractText()
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())