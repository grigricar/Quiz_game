# Quiz_game_bigger_than.py

"""
This flashcard game program asks the reader to choose between the bigger of two options.
The user is prompted to enter 's' to see a new entry or 'q' to quit.In response, the
 program randomly picks an entry from all glossaryentries. It asks the user to select
an option, 'A.' or 'B.'. The program tells the user whether they were correct or not.
The user can repeatedly ask for an entry and also has the option to quit the program.
If quit ('q') is selected the program shows the user the number of correct answers. 
"""

from random import *

# Set up the question bank
question_bank = {
            'The area of Texas':'The area of France',
            'A Zettabyte':'An Exabyte',
            'Mars':'Mercury',
            'Population of Austria':'Population of Switzerland',
            'Common seal':'Labrador dog',
            'GDP of India':'GDP of the UK',
            'Number of kinds of bee':'Number of kinds of bat',
            'Jupiter':'All the other planets put together',
            'Words in the works of Shakespeare':'Words in the Bible',
            'Number of bees on Earth':'Number of stars in our galaxy'    
            }

# Show a random flash card

def show_flashcard():
    """ Presents the user with a randomised choice between a pair from question_bank.
        The user is then asked to choose which is greater. The user input is recorded
        and tested for whether it is correct or not. The value of 'True' is returned
        if the correct answer is gvien. 
    """
   
    # DO NOT ALTER THE NEXT LINE
    global score_count

    # MAKE YOUR CHANGES BETWEEN HERE AND THE END OF THE show_flashcard() FUNCTION
    #Randomise the order of pairs from the glossary
    big_item = choice(list(question_bank))
    small_item = question_bank[big_item]

    #Randomises the order of the pair selected and asks the question
    random_number = choice([0,1])
    if random_number == 0:
        first_random = big_item
        second_random = small_item
    elif random_number == 1:
        first_random = small_item
        second_random = big_item
    print ('Which is bigger?\nA.', first_random,'\nB.', second_random)

    #Determines whether the input is correct or not.
    user_input2 = input("Enter your guess, A. or B. : ")
    if user_input2 == 'A.':
        user_input2 = first_random
    elif user_input2 == 'B.':
        user_input2 = second_random
    if user_input2 == big_item:
        return True
    else:
        return False
   


# The interactive loop which allows the user to repeatedly see a new entry or quit and see thier score.
score_count = 0
total_attempts = 0
exit = False
while not exit:
    user_input = input("Enter 's' to show a new pair and 'q' to quit: ")
    if user_input == 'q':
        exit = True
        print('Number of correct answers:', score_count, 'out of', total_attempts)
    elif user_input == 's':
        result = show_flashcard()
        total_attempts = total_attempts + 1
        if result == True:
            score_count = score_count +1
            print ('Correct')
        else:
            print('Incorrect')
    
                       
