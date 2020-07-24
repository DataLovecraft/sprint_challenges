'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    #set the target
    target = 'th'
    #if the word is <=1, it can't contain two characters
    if len(word) <= 1:
        return 0
    #if the target string is not in the word, return 0
    elif target not in word:
        return 0
    #if the target string is in the word:
    elif target in word:
        #find the index where it first appears, and add 2 (to get where the string)
        #after the target appears
        sub_word_index = word.find(target) + 2
        #use list slicing to get a new sub-word, starting after the
        #most recent useage of the target string
        new_word = word[sub_word_index:]
        #incriment the count by 1, and then recursively search the sub-word.
        return 1 + count_th(new_word)
