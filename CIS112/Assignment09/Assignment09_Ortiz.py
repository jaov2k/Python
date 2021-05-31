# Jose Ortiz
# 05-14-2021
# CIS112 - Spring 2021
# Assignment 9
#
# PURPOSE:  A program which merges an existing PDF file
#           into another existing PDF file, creating a
#           new output merged pdf file.

# Import necessary modules
from pathlib import Path
from PyPDF2 import PdfFileMerger

# New PDF Merger object
pdf_merger = PdfFileMerger()

# This is the main PDF which will have pages merged into
pdf_merger.append(str('pythonlearn_ch8MissingPages.pdf'))

# These is the file which will be inserted and its location
pdf_merger.merge(4,str('From_pythonlearn_ch8.pdf'))

# Output file gets created
with Path("full_report.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file) 