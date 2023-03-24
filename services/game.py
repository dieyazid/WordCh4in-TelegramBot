import random

with open("words.txt") as f:
    words = f.read().splitlines()

def Valid_Check(word,current_word,duplicated):
    if word in words: 
        if word not in duplicated:
            if current_word !='':
                if word[0] == current_word[-1]:
                    return True
                else:
                    return False
            else: 
                return True
        else:
            return False
    else: 
        return False

def Generate_Bot_Answer(word,current_word,duplicated):
    Valid = False
    if word !='':
        matching_words = [word for word in words if word[0] == current_word[-1]]
    else:
        matching_words = words
    while Valid ==False:
        selected_word= random.choice(matching_words)
        Valid = Valid_Check(selected_word,current_word,duplicated)
        if Valid == False:
            matching_words.remove(selected_word)
        if len(matching_words) == 0:
            return 'I Lost'
    return selected_word