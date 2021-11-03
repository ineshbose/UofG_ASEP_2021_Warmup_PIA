def anagrams(word, words):
    anagrams = []

    word_map = {}
    for let in word:
        if let in word_map:
            word_map[let] += 1
        else:
            word_map[let] = 1


    for w in words:
        is_anagram = True

        if len(word) != len(w):
            is_anagram = False
        
        else:
            for let in w:
                if w.count(let) != word_map.get(let):
                    is_anagram = False

        if is_anagram:
            anagrams.append(w)

    return anagrams
        

