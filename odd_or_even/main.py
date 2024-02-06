bob = input('Choose a whole number: ')

def odd_or_even(num):
    if num % 2 == 0:
        print('Number is even')
    elif num % 2 != 0:
        print('Number is odd')
    else:
        print('Not a number')

odd_or_even(int(bob))