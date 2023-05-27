import PyPDF2

new_pdf = open('Intro1.pdf', 'rb') #file object creation
reading_pdf = PyPDF2.PdfFileReader(new_pdf) #pdf reader object
print(reading_pdf.numPages) #number of pages in pdf

pdf_page = reading_pdf.getPage(0) #page object creation
print(pdf_page.extractText())

# Close PDF File
new_pdf.close()