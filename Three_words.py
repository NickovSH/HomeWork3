#The sequence contains words and numbers, if the string contains three words
# in a row, the result is True, otherwise False

def Three_Words():
    print('\nExercise 5 - Three words')
    print('Enter text')
    Text = input()
    Text = Text.split()
    k = 0
    Result = 'False'

    for i in Text:
        if i.isdigit() == False:
            k += 1
        else:
            k = 0
        if k >= 3:
            Result = 'True'

    print('Результат = ', Result)