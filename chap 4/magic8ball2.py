import random

messages = ['確かにそうだ', '間違いなくそうだ',
            'はい', 'なんとも。もういちどやってみて',
            '後でもう一度聞いてみて', '集中してもう一度聞いてみて']
print(messages[random.randint(0, len(messages) - 1)])
