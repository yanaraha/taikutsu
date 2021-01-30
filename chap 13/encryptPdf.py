#! python3

import PyPDF2
import os
import sys

if len(sys.argv) != 2:
  print('引数違う')
  exit(1)

pdf_files = []

for foldername, subfolders, filenames in os.walk('.'):
  pdf_files.clear()
  # カレントディレクトリのpdfファイル名取得
  for filename in filenames:
    if filename.endswith('.pdf'):
      pdf_files.append(os.path.join(foldername, filename))

  # 取得したpdfファイルを読み込む
  for filename in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(open(filename, 'rb'))
    pdf_writer = PyPDF2.PdfFileWriter()
    # 前ページ読み込み
    for num in range(pdf_reader.numPages):
      pdf_writer.addPage(pdf_reader.getPage(num))
    # pdfファイル暗号化
    pdf_writer.encrypt(sys.argv[1])
    result_pdf = open(filename[:-4] + '_encrypted.pdf', 'wb')
    pdf_writer.write(result_pdf)
    print(filename + '暗号化完了')
    result_pdf.close()