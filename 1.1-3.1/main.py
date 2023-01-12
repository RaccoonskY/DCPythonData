import random


count = 0
before = []
biggest_ans = 10
smallest_ans = 0

while 1:
    answer = random.randint(smallest_ans, biggest_ans)
    while answer in before:
        answer = random.randint(smallest_ans, biggest_ans)
    before.append(answer)
    print(f"My version:{answer}\nIs number bigger, less or equal?")
    count += 1
    rightous = input()
    rightous = rightous.lower()
    while rightous not in ['bigger', 'less', 'equal']:
        print('What?')
        rightous = input()
    if rightous == 'bigger':
        smallest_ans = answer
    elif rightous == 'less':
        biggest_ans = answer
    elif rightous == 'equal':
        print(f'FUCK YEAH!\nnumber of tries: {count}')
        break
