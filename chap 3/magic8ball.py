import random

def get_answer(answer_number):
    if answer_number == 1:
        return 1
    elif answer_number == 2:
        return 2
    elif answer_number == 3:
        return 3

r = random.randint(1, 3)
number = get_answer(r)
print(number)
