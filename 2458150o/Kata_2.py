def spin_words(sentence):
    # Your code goes here

    sentence = sentence.split(" ")
    newSentence = ""
    for i in sentence:
        print(i)
        if len(i) >= 5:
            word = i[::-1]
            newSentence += word + " "
        else:
            newSentence += i + " "
    return newSentence[:-1]