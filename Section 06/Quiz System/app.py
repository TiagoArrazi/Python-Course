questions = list()

with open('questions.txt', 'r') as questions_file:
    for line in questions_file:
        questions.append(line.rstrip('\n'))

questions_file.close()


score = 0
for question in questions:
    try:
        user_answer = int(input(f'{question} '))
    except ValueError:
        print('Invalid answer, must be integer, WRONG!')
    else:
        right_answer = eval(question[:-1])
        if user_answer == right_answer:
            score += 1
        else:
            print('Wrong answer!')

print(f'Total questions = {len(questions)}')
print(f'Right answers = {score}')
print(f'Score = {score / len(questions):.2f}')
