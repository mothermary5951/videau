def break_words(stuff):    #separates each word
    """This function will break up words for us."""
    words = stuff.split(' ')    # makes each word a string in single quotes
    return words               # comma-separated and remembered individually.

def sort_words(words):         # alphabetizes the words in the sentence using
    """Sorts the words."""    # again the words as strings in single quotes.
    return sorted(words)       #  remembered as alphabetized words

def print_first_word(words):    #prints the sentence's first word
    """Prints the first word after popping it off."""  
    word = words.pop(0)     #searches for the first byte in the sentence
    print word                # prints the first word in the sentence "0"

def print_last_word(words):    
    """Prints the last word after popping it off."""
    word = words.pop(-1)    #searches for the last word in the sentence
    print word                # prints the last word "-1"

def sort_sentence(sentence):  # alphabetizes all the words in a sentence
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)  # makes the words strings in single quotes
    return sort_words(words)    #remembers each word in alphabetical order

def print_first_and_last(sentence):  #prints 1st and last words of original
    """Prints the first and last words of the sentence."""    #sentence.
    words = break_words(sentence)  #same as above
    print_first_word(words)     # print first word as a string      
    print_last_word(words)     # same for last word

def print_first_and_last_sorted(sentence): # prints alphabetized 1st & last
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)   
    print_first_word(words)
    print_last_word(words)
