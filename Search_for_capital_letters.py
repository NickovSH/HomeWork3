#The program finds all the capital letters of a string

def Capital_letters():
    print('\nExercise 4 - Capital letters')
    print('Enter text')
    Text = input()
    Capital_text = []
    Sep_text = []

    Sep_text = Text.split()
    print(Sep_text)

    for i in Sep_text:
        if i.istitle() == True:
            Capital_text.append(i[0])
        else:
            continue

    print(Capital_text)