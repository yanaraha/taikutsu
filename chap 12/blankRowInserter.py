#! python3

import openpyxl, sys

wb = openpyxl.open(sys.argv[3])
sheet = wb.active
sheet.insert_rows(idx=int(sys.argv[1]), amount=int(sys.argv[2]))
wb.save(sys.argv[3])