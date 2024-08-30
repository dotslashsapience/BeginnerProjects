import random

#Requests name of Magic 8 ball user and sets as the variable 'name'
name = input('What is your name?: \n')

print('Hello, ', name)


def main ():
    
    #prompts the user to ask a question of the magic 8 ball

    question = input('What question do you have for the Magic 8 ball?: \n')

    #variable for script to store answer to users question

    answer = ''

    random_number = random.randint(1,9)

    if random_number == 1:
        answer = 'Yes - definitely'
    elif random_number == 2:
        answer = 'It is decidedly so'
    elif random_number == 3:
        answer = 'Without a doubt'
    elif random_number == 4:
        answer = 'Reply hazy, try again'
    elif random_number == 5:
        answer = 'Ask again later'
    elif random_number == 6:
        answer = 'Better not tell you now'
    elif random_number == 7:
        answer = 'My sources say no'
    elif random_number == 8:
        answer = 'Outlook not so good'
    elif random_number == 9:
        answer = 'Very doubtful'

    print(answer)
    
    ask_another = input('\nWould you like to ask another question? Y or N: \n')
    ask_another = ask_another.upper()

    if ask_another == 'Y':
        main ()
    elif ask_another == 'N':
        print('Goodbye!')

first_ask = input('Would you like to ask a question? Y or N: \n')
first_ask = first_ask.upper()

if first_ask == 'Y':
    main()
elif first_ask == 'N':
    print('Ok, then! Have a nice day!')
    







