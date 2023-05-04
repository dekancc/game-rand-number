import random
random_number = random.randint(1,3)
answer_number = int(input('Try to guess the number I guessed ='))
while answer_number != random_number:
    print('You failed to guess my number!')
    random_number = random.randint(1,3)
    answer_number = int(input('Try to guess the number I guessed'))
if answer_number == random_number:
    print('Well done!')