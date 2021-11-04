def spin_words(sentence):
    str = sentence.split(" ")
    for i in range(len(str)):
        if(len(str[i]) >= 5):
            str[i] = str[i][::-1]
    str = " ".join(str)
    return str