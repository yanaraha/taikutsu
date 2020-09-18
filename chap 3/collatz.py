def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('数字を入力してください')
while True:
    try:
        number = int(input())
        break
    except ValueError:
        print('数字を入力してください')

ans = 0
i = 1
while ans != 1:
    ans = collatz(number)
    print(str(i) + '回目:' + str(ans))
    number = ans
    i = i + 1
    
