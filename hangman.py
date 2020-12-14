import random

def hangman():
    word = random.choice(['notebook','classroom','system','network','python','javascript','banana','jackfruit','friends','wineglass','yellow','green','square','cube','save','safe'])
    guess_word_list = ''
    missed = 10

    while len(word) > 0:
        main = ''
        for letter in word:
            if letter in guess_word_list:
                main = main + letter
            else:
                main = main + '_'+ ' '
        
        if main == word:
            print(f'you win !{user_name} you save life.')
            print('correct word is :', word)

            break

        print(f'Try to find in {missed} attemps : {main}')
        guess_word = input()
        
        if guess_word in word:
            guess_word_list = guess_word_list + guess_word
        else:
            missed = missed - 1
            if missed == 9:
                print("-------")
            if missed == 8:
                print("-------")
                print('   0   ')
            if missed == 7:
                print("-------")
                print('   0   ')
                print('   |   ')
            if missed == 6:
                print("-------")
                print('   0   ')
                print('   |   ')
                print('  /    ')
            if missed == 5:
                print("-------")
                print("   0   ")
                print("   |   ")
                print("  / \  ")
            if missed == 4:
                print("-------")
                print("  \0   ")
                print('   |   ')
                print('  / \  ')
            if missed == 3:
                print("-------")
                print(" \ 0_  ")
                print('   |   ')
                print('  / \  ')
            if missed == 2:
                print("-------")
                print(' \ 0_| ')
                print('   |   ')
                print('  / \  ')
            if missed == 1:
                print("-------")
                print(" \ 0_|/")
                print('   |   ')
                print('  / \  ')
            if missed == 0:
                print("-------")
                print("   0__|")
                print("  /|\  ")
                print("  / \  ")
                print(f"OOPS ! {user_name} you killed a kind man ! ")
                break

user_name = input('Enter your name :')
print('Welcome ! To hangman Game ',user_name)
print('------------------------------------------------')
print('In the game you will get 10 attempts to guess the word, in each turn guess one alphabet(a to z)' )
print()
key = input('Press y to start game :')
if key == 'y':
    hangman()
else:
    print('thankyou !',user_name)