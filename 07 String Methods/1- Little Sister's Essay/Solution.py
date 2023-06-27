def capitalize_title(title):
    return title.title()
    
def check_sentence_ending(sentence):
    return sentence[-1] == "."

def clean_up_spacing(sentence):
    words_list = sentence.split()
    return " ".join(words_list)
    
def replace_word_choice(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)
