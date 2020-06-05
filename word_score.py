def word_sc():
    word = input("Type a word").upper()
    wordscore=0
    if word.isalpha() == True:
        for i in word:
            wordscore = wordscore + (ord(i)-64)
        print(wordscore)
    else:
        print("Please enter only alphabet")
        word_sc()
word_sc()
