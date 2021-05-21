# Jose Ortiz
# 05-20-2021
# CIS112 - Spring 2021
# Assignment 8
#
# PURPOSE:  A Python program which concatenates three PDF files 
#           together and name merged file as "MergedFile.pdf"

# Import necessary modules
from pathlib import Path
from PyPDF2 import PdfFileMerger
import glob

# Create a list of all the PDF files in the directory and sort them
PLearn = list(glob.glob("*.pdf")) # relative pathing
PLearn.sort()

# Creates a merge object for appending PDF files to, and appends the list
pdf_M = PdfFileMerger()
for path in PLearn:
	pdf_M.append(str(path))

# Creates the output file with the concatenated PDF files
with Path("MergedFile.pdf").open(mode='wb') as outpf:
	pdf_M.write(outpf)