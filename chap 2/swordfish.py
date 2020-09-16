while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hey Joe. Input your pass')
    password = input()
    if password == 'pass':
        break
print('OK')
