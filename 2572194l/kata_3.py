def anagrams(word, words):
    result = words.copy()
    for w in words:
        if(len(word) != len(w)):
            result.remove(w)
        else:
            for i in range(len(word)):
                if(word[i] not in w or w[i] not in word):
                    result.remove(w)
                    break
    return result