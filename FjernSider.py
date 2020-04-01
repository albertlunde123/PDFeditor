# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:11:14 2020

@author: Administrator

fjern sider fra pdf.
"""
from PyPDF2 import PdfFileWriter, PdfFileReader

pages_to_keep = list(range(0,24)) # page numbering starts from 0
infile = PdfFileReader('Clark-2013.pdf', 'rb')
output = PdfFileWriter()

for i in pages_to_keep:
    p = infile.getPage(i)
    output.addPage(p)

with open('Clark-2013_edit.pdf', 'wb') as f:
    output.write(f)