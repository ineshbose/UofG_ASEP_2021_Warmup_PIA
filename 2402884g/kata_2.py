def spin_words(sentence):
    words = sentence.split(" ")

    new_sentence = []

    for w in words:
        temp = w
        if(len(w) >= 5):
            temp = w[::-1]

        new_sentence.append(temp)

    return(' '.join(new_sentence))
