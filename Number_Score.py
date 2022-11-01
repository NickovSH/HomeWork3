#The program evaluates the given value using the following rules.
#if x is odd, then it's "Bad"
#if x = [2, 5] and even then it's "Not bad"
#if x = [6, 20] and even, then it's "So-so"
#if x > 20 and even then it's "Excellent"

def Number_Score():
    print('\nExercise 2 - Number Score')
    try:
        print('Enter the number')
        Number = int(input())

        Output_Mwssage = ('Вы ввели число < 0' if Number < 0 else
                        'Плохо' if Number % 2 != 0 else
                        'Неплохо' if (Number >= 2) and (Number < 6) else
                        'Так себе' if (Number >= 6) and (Number < 21) else
                        'Отлично')
        print(Output_Mwssage)
    except Exception:
        print('You didn\'t enter a number')