def word_frequency(phrase):
    word = phrase.split()
    result = {}
    for el in word:
        if el not in result:
            result[el] = 1
        else:
            result[el] += 1
    return result

text = "i love to be in this i i i  situation a lot"
print(word_frequency(text))
