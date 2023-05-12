from random import choice

print('-' * 40)
print(f'{"Draw Lottery Numbers":^38}')
print('-' * 40)


def int_number(value=''):
    if value.isdigit() == False:
        while value.isdigit() == False:
            print("There isn't a valid choice, please try again!")
            value = input("Insert here => ")
            value.isdigit()

    return int(value)


lottery_numbers = []
num = None

total_numbers = input(
    "What's the largest number your lottery allows you to pick? ")
total_numbers = int_number(total_numbers)

numbers_to_choose = input("How many numbers to choose? ")
numbers_to_choose = int_number(numbers_to_choose)

while len(lottery_numbers) != numbers_to_choose:
    num = choice(range(total_numbers + 1))

    if num not in lottery_numbers:
        lottery_numbers.append(num)

print("Your lottery numbers are:")
for number in lottery_numbers:
    print(f'\033[34m— {number}\033[m', sep=' - ')
