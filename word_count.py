def word_count(sentence):
    space_count = 1
    for i in range (len(sentence)):
        if sentence[i] == " ":
            space_count+=1
    return space_count