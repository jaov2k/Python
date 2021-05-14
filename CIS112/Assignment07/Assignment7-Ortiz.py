# Jose Ortiz
# 05-14-2021
# CIS112 - Spring 2021
# Assignment 7
#
# PURPOSE:  A program which receives a filename from the user,
#           a range of pages to be extracted, and a filename
#           to extract the range of pages to. Program provides
#           validation of pages range.

# Import necessary modules
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

# Get input/output filenames from user, and validate range of pages to be extracted
input_pdf_path = input('Please enter a file name: ')
input_pdf = PdfFileReader(str(input_pdf_path))
while True:
    startPage = int(input('Please enter the beginning page number to extract: '))
    endPage = int(input('Please enter the ending page number to extract: '))
    if startPage > endPage:
        print ('Your beginning and ending page numbers are not correct.')
        continue
    elif endPage > input_pdf.getNumPages():
        print ('Your ending index is out of range, please enter correct ending page.')
        continue
    elif startPage == 0 or endPage == 0:
        print ('"0" page numbers are not correct.')
        continue
    break
output_pdf_path = input('Please enter output file name: ')

# Add the range of pages to the output object
pdf_writer = PdfFileWriter()
for page in input_pdf.pages[startPage:endPage]:
	pdf_writer.addPage(page)

# Write output file to directory
with Path(output_pdf_path).open(mode="wb") as output_file:
	pdf_writer.write(output_file)