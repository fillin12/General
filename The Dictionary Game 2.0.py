__author__ = 'Robert'

######################
## The Dictionary Game
######################

######################
## Fixes:

## Add incorrect question words to a list for problem words then repeat them at the end
## Fix the scoring system
## Screen answers so that their part of speech matches the hint ( v., adj., noun )
## Get rid of repeats in the hints
## Add in-game options: changes to question number, quitting, number of answers
## Allow the entry of one of the words in the list as an answer not just A, B, etc.



import random

import time

debug = False


def make_random_list( count ):

    random_list = []

    n = 0
    
    while n < count:
        
        random_int = random.randint( 0, count )

        if random_int in random_list:

            continue

        else:
            
            random_list.append( random_int )

        n += 1

    return random_list


def make_answer_list( ans_num, count, enumerated_dict ):

    answer_list = []
    
    n = 0
    
    while n < ans_num:

        alt_random_int = random.randint( 0, count )

        if question_type == "d2w":
            dummy_answer = enumerated_dict[ alt_random_int ][ 0 ]
        else:
            dummy_answer = enumerated_dict[ alt_random_int ][ 1 ]

        answer_list.append( dummy_answer )
        
        n += 1
        
    return answer_list


def question( ans_list, key, enumerated_dict, correct_answer ):

    num_of_ans = len( ans_list )
    base_str = ""
    answer_index_list = []
    count = 0
    
    for i in range( 65, 65 + num_of_ans ): 

        if ( count // 26 ) > 0:
            base_str = "A" * ( count // 26 )

        unicode_char_val = i - ( 26 * ( count // 26 ) )

        answer_index_list.append( base_str + str( chr( unicode_char_val ) ) )
        
        count += 1

    ans_list.pop()
    ans_list.append( correct_answer )
    random.shuffle( ans_list )
    
    print( "\n\t\tHint:", key )
    print()
    
    for i in range(0, num_of_ans):
        print( "\t\t\t", answer_index_list[ i ] + ":", ans_list[ i ] )

    while True:
        
        ans_input_str = input( "\n>>> " )
        print()

        if ans_input_str.upper() not in answer_index_list:
            print( "\t######## That is not an acceptable answer. Try again. ########" )

        else:
            
            answer_index = answer_index_list.index( ans_input_str.upper() )
            answer = ans_list[ answer_index ]
            
            if answer == correct_answer:
                print( "Correct!\n\n\n" )
                break

            else:
                print( "Incorrect! Try again!" )
                


enumerated_dict = {}

seconds_flt = time.time()

while True:
    
    try:
        print()

        if debug == True:
            file_name = "NewDict.txt"
        else:
            file_name = input( "Enter the name of a dictionary to be used: ")

        word_file = open( file_name, "r")

        break

    except FileNotFoundError:

        print()
        print( "That file was not found. Try again" )

count = 0

numbers = "0123456789"
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for line in word_file:

    #Checks for blank line in the file
    for char in line:
        
        if (char in characters) or (char in numbers):
            break
        
        else:
            count -= 1
            continue

    main_string_length = len( line )

    i = 0

    while ( i + 1 ) <= main_string_length:

        main_string_split = line [ i : i + 1 ]

        if " " in main_string_split: #if space is found in the line

            word = line[ : i ]

            definition = line[ i + 1 : ].strip()

            enumerated_dict[ count ] = [ word, definition ] #assembles the dictionary

            break # stops at the first space

        i += 1

    count += 1



if debug == True:
    question_count = 5
    
else:
    while True:
        
        try:
            question_count = int( input( "Enter the number of questions you would like to answer: " ))
            
            if question_count <= 0:
                print( "Question count must be an integer greater than zero. Try again." )
                continue

            else:
                break
            
        except TypeError:
            print( "Unrecognizable input. Try again." )


if debug == True:
    question_type = "d2w"
    
else:
    while True:
        
        question_type = input( "Enter your preffered question type (d2w or w2d): ")
        
        if question_type == "d2w" or question_type == "w2d":
            break
        
        
        else:
            print( "That is an unrecognizable response. Try again." )
            continue
        

if debug == True:
    number_of_answers = 15
    
else:
    while True:
        
        try:
            number_of_answers = int( input( "Enter the number of answers you'd like in each question: " ) ) 

            if number_of_answers <= 0:
                print( "Number of answers must be an integer greater than zero. Try again." )
                continue

            else:
                break
            
        except TypeError:
            print( "Unrecognizable input. Try again." )
            
random_list = make_random_list( count - 1 )

answered_questions = 0
question_number = 1
attempts = 1

while answered_questions < question_count:
    
    if random_list == []:
        break

    random_int = random_list.pop()
            
    word = enumerated_dict[ random_int ][ 0 ]
    definition = enumerated_dict[ random_int ][ 1 ]

    answer_list = make_answer_list( number_of_answers, count - 1, enumerated_dict )

    print( "Question", str( question_number ) + ":" )
    
    if question_type == "d2w":
        question( answer_list, definition, enumerated_dict, word )

    else:
        question( answer_list, word, enumerated_dict, definition )
    
    answered_questions += 1
    question_number += 1
    
print( "\n\nScore:", ( answered_questions / attempts ) * 100 )




















    
