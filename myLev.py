# a straightforward approach may be Levenshtein distance, 
# importing this and running as lev("wordA", "wordB"), 
# instead I have attempted a (very probably inelegant and inefficient
# ... at something like O(n-squared) cost...) approach where
# any current coexisting letters are kept, and additions are only made
# if not already in the word. These additions are counted as 'changes made'.
































 
wordA = list("learn")
wordB = list("dream")
count = 0
finalWord = []

for i in range(len(wordA)):
    if len(wordA) != len(wordB):
        wordB.append(" ")

for i in range(len(wordB)):
    if len(wordA) != len(wordB):
        wordA.append(" ")


for i in range(len(wordA)):
    for j in range(len(wordB)):
        if wordA[i] == wordB[j]:
            finalWord.append(wordB[j])
            wordB[j] = " "
            wordA[i] = " "
            break
   

print("These letters we don't have to change: ", finalWord)
wordB = list("dream")      


for i in range(len(wordB)):
    if len(finalWord) != len(wordB):
        finalWord.append(" ")
    if finalWord[i] != wordB[i]:
        finalWord.insert(i, wordB[i])
        count = count + 1

print("With the letters we have to add: ", [x for x in finalWord if x.strip(" ")])
print("We had to add this many letters: ", count)


