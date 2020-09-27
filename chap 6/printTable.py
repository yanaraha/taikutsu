#! python3

def print_table(table):
  col = len(table)
  row = len(table[0])
  max_col_width = [0] * col

  for i in range(col):
    for row_list in table[i]:
      max_col_width[i] = max(max_col_width[i], len(row_list))

  for i in range(row):
    for j in range(col):
      print(table[j][i].rjust(max_col_width[j] + 1), end='')
    print()

table_data = [['apples', 'oranges', 'cherries', 'banana'], 
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
print_table(table_data)
