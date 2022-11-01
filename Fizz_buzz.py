#The program takes a positive integer and returns the sl. values.
#"Fizz Buzz" if the number is divisible by 3 and 5;
#"Fizz" if the number is divisible by 3;
#"Buzz" if the number is divisible by 5;

def Multiplicity_of_a_number ():
    print('\nExercise 2 - Fizz Buzz')

    try:
        print('Enter the number = ')
        Number = int(input())

        if (Number % 3 == 0) and (Number % 5 == 0):
            print('Fizz Buzz')

        elif (Number % 3 == 0) and (Number % 5 != 0):
            print('Fizz')

        elif (Number % 5 == 0) and (Number % 3 != 0):
            print('Buzz')

        else:
            print('Number')

    except Exception:
        print('You didn\'t enter a number')