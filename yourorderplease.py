def order(sentence):
    if len(sentence)==0:
        return ""
    words = {}
    for word in sentence.split():
        for letter in word:
            if letter.isdigit():
                words[int(letter)]=word
    ret_list = [words[key] for key in sorted(words.keys())]
    return ' '.join(ret_list)
