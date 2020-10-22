import random



answers=['Strongly Disagree', 'Disagree', 'Agree', 'Strongly Agree']

for x in range(1, 64):
    print(x, " : ", answers[random.randint(0,3)])
