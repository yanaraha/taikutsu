list = []

def comma(list):
    str = ''
    for i in range(len(list)):
        if len(list) == 1:
            str = list[i]
        elif i == len(list) - 1:
            str = str + 'and ' + list[i]
        else:
            str = str + list[i] + ', '
    return str

while True:
    print('値を入力してください、終わりの場合はEnter押下')
    value = str(input())
    if value == '':
        break
    list.append(value)

print(comma(list))
