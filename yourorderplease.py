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

# Recommended Best Practice Solutions are:
# • No.1 :
# def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

# • No.2 :
# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

# • No.3 :
# def order(sentence):
#     if not sentence:
#         return ""
#     result = []    #the list that will eventually become our setence
      
#     split_up = sentence.split() #the original sentence turned into a list
  
#     for i in range(1,10):
#         for item in split_up:
#             if str(i) in item:
#                  result.append(item)    #adds them in numerical order since it cycles through i first
  
#     return " ".join(result)

# • No.4 :
# def order(sentence):
#     def sort_key(s):
#         return next(c for c in s if c.isdigit())
#     return ' '.join(sorted(sentence.split(), key=sort_key))

# • No.5 :
# order = lambda xs: ' '.join(sorted(xs.split(), key=min))
