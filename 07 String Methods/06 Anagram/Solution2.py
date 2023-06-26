from collections import defaultdict

def find_anagrams(word, candidates):
    word = word.lower()
    word_letters = defaultdict(int)
    
    for char in word:
        word_letters[char] += 1
    
    anagram_list = [candidate for candidate in candidates
                    if len(candidate) == len(word) and candidate.lower() != word 
                    and all(candidate.lower().count(char) == word_letters[char]
                            for char in candidate.lower())]

    return anagram_list
    
