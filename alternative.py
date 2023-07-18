'''
based on learning from Hyperion.dev
first compulsory task set in T11
A program to output a string of alternating
upper and lower case letters, followed by
outputting a string of alternating lower case and
upper case words.
'''



inputString = list("hello world I am learning to code")
for i in range(len(inputString)):
    if i%2 == 0:
        inputString[i] =inputString[i].upper()
    else:
        inputString[i] = inputString[i].lower()
inputStringJoined = "".join(inputString)
print(inputStringJoined)


sentence = "hello world I am learning to code"
split_sentence = sentence.split(" ")
for i in range(len(split_sentence)):
    if i%2 == 0:
        split_sentence[i] = split_sentence[i].lower()
    else:
        split_sentence[i] = split_sentence[i].upper()
list_joined = " ".join(split_sentence)
print(list_joined)