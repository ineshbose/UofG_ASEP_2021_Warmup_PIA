def anagrams(word, words):
    word = sorted(word)
    l = []
    
    for i in words:
        if word == sorted(i):
            l.append(i)
    return l
    
    