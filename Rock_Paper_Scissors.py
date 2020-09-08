import random
options = ['Stone', 'Scissors', 'Paper']
rounds = int(input('Enter number of rounds:'))
user_counter = 0
computer_counter = 0
for i in range(rounds):
    print(f'Round {i+1}')
    user = input('Enter your choice(from Stone,Paper and Scissors):')
    computer = random.choice(options)
    print(computer)
    if computer == 'Stone' and user == 'Paper':
        print('User wins')
        user_counter = user_counter + 1
    elif computer == 'Paper' and user == 'Scissors':
        print('User wins')
        user_counter = user_counter + 1
    elif computer == 'Scissors' and user == 'Stone':
        print('User wins')
        user_counter = user_counter + 1
    elif computer == user:
        print("It's a Tie")
    else:
        print('Computer wins')
        computer_counter = computer_counter + 1
print(user_counter)
print(computer_counter)
if user_counter < computer_counter:
    print('Computer is the winner')
elif user_counter > computer_counter:
    print('User is the winner')
else:
    print("It's a Tie")
