def find_anagrams(word, candidates):
    word = word.lower()
    word_letters = {}
    anagram_list = []
    
    for char in word:
        if char in word_letters:
            word_letters[char] += 1
        else:
            word_letters[char] = 1
    
    counter = 0
    for candidate in candidates:
        print(anagram_list) 
        if len(candidate) == len(word):
            test = candidate.lower()
            if test != word:
                for char in test:
                    if char in word_letters:
                        if test.count(char) == word_letters[char]:
                            counter += 1
            if counter == len(word):
                anagram_list.append(candidate)
            counter = 0
    
    return anagram_list
