def count_chars(word):
    letters = {}
    for c in word:
        if c in letters.keys():
            letters[c] = letters[c] + 1
        else:
            letters[c] = 1
    return letters


def are_chars_equal(dict1, dict2):

    for key, value in dict2.items():
        if key not in dict1:
            return False

        if dict1[key] != value:
            return False

    return True


def anagrams(word, words):

    word_chars = count_chars(word)

    valid_words = []

    for w in words:
        temp_chars = count_chars(w)
        if(are_chars_equal(word_chars, temp_chars)):
            valid_words.append(w)

    return valid_words
