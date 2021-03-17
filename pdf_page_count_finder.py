import fnmatch,os
from PyPDF2 import PdfFileReader
# find the number of all pages for all pdfs

# location of PDF files
extension = input("Location of PDF files: ")
location = os.listdir(extension)
pdflist = fnmatch.filter(location,"*.pdf")

number_of_pages = 0

# where we find the sum of the pages
for i in pdflist:
    print(i)
    pdf = PdfFileReader(open(str(extension)+'\\'+ i ,'rb'))
    a = pdf.getNumPages()
    number_of_pages+=a

# the part where we show the information to the user
print("\n\nTotal Number Of Pages: ",number_of_pages)
input("\n")
