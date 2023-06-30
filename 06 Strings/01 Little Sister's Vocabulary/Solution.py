def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    for i in range(len(vocab_words)):
        if i != 0:
            vocab_words[i] = vocab_words[0] + vocab_words[i]
            
    return " :: ".join(vocab_words)

def remove_suffix_ness(word):
    if word[-5] == "i":
        word = word.removesuffix("iness") + "y"  
    else:
        word = word.removesuffix("ness")

    return word
    
def adjective_to_verb(sentence, index):
    sentence_list = sentence.split()
    word = sentence_list[index].removesuffix(".") + "en"
    
    return word
    
