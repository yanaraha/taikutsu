#! python3

import PyPDF2
import sys
import os

if len(sys.argv) != 3:
  print('引数違う')
  exit(1)

pdf_file = open(sys.argv[1], 'rb')
pw_file = open(sys.argv[2], 'r')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

i = 0
for pw in pw_file.readlines():
  i = i + 1

  if i % 10000 == 0:
    print(i)
  
  pw = pw[:-1]
  if pdf_reader.decrypt(pw) == 1:
    result_pdf_file = open(sys.argv[1][:-4] + '_decrypted.pdf', 'wb')
    result_pdf_writer = PyPDF2.PdfFileWriter()
    for num in range(pdf_reader.numPages):
      result_pdf_writer.addPage(pdf_reader.getPage(num))
    result_pdf_writer.write(result_pdf_file)
    pdf_file.close()
    pw_file.close()
    result_pdf_file.close()
    print('パスワードは：' + pw)
    exit(0)
print('なかった')
exit(1)
  
  

