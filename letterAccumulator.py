
givenString = "You can have data without information, but you cannot have information without data"
listedGivenString = list(givenString.lower())
alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
for letter in range(0, len(alphabet)):
  letterCount = 0
  for target in range(0, len(listedGivenString)):
    if alphabet[letter] == listedGivenString[target]:
      letterCount += 1
  if letterCount > 0:
    print(alphabet[letter], ":", letterCount)