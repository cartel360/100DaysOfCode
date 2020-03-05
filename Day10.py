sentence = input("Enter your Sentence: ")

vowels = ('a', 'e', 'i', 'o', 'u')

#words = sentence.split()
# print(words)

# for word in words:
#     if(len(words) > 4):
#         for vowel in words.lower():
#             if vowel in vowels:
#                 new_sentence = words.replace(vowel, "")

#         print(new_sentence)for word in words:
#     if(len(words) > 4):
#         for vowel in words.lower():
#             if vowel in vowels:
#                 new_sentence = words.replace(vowel, "")

#         print(new_sentence)


if (len(sentence) > 4):
    for vowel in sentence.lower():
        if vowel in vowels:
            new_sentence = sentence.replace(vowel, "")

    print(new_sentence)

else:
    print(sentence)
