import PyPDF2
pdfFile1 = open('c:\\users\\alan\\documents\\meetingminutes1.pdf','rb')
pdfFile2 = open('c:\\users\\alan\\documents\\meetingminutes2.pdf','rb')
reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)
writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    Page = reader1.getPage(pageNum).extractText()
    writer.addPage(Page)
for pageNum in range(reader2.numPages):
    Page = reader2.getPage(pageNum).extractText()
    writer.addPage(Page)

outputFile = open('c:\\users\\alan\\documents\\combinated.pdf','wb')
writer.write(outputFile)
outputFile.close()
pdfFile1.close()
pdfFile2.close()