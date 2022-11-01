#The program finds matches with the words right and changes them to left

def Change_words():
    print('\nExercise 6 - Lefties have taken over the world')
    print('Enter text')
    Text = input()

    if 'right' in Text:
        Text = Text.replace('right', 'left')

    print(Text)

Change_words()