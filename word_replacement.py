def replaceWord():

    str = "This is a string"
    word_to_replace = input("Enter the word to replace: ")
    word = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word))

replaceWord()