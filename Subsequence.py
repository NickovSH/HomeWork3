#The program outputs a sequence of numbers up to a given number

def Subsequence():
    print('\nExercise 3 - Sequence of numbers')
    print('Enter the number')

    try:
        Number = int(input())
        Sequence_list = []
    except Exception:
        print('You didn\'t enter a number')
        exit()

    if Number > 0:
        for i in range(Number):
            Sequence_list.append(i+1)
        print(Sequence_list)

    elif Number < 0:
        Number = abs(Number)
        for i in range(Number):
            Sequence_list.append(-1*i-1)
        print(Sequence_list)

    elif Number == 0:
        print('0')