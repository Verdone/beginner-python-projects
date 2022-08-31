def replaceWord(): # Method is case sensitive (for replacing, StRiNg ≠ string)
    
    str = input("> Enter a string: \n> ")
    print("> Your string is ",str)
    word_to_replace = input(
        "Enter the character(s) to replace (case sensitive!): \n> ")

    if str.find(word_to_replace) != -1:
        pass
    else:
        print("> Input not accepted, restart application to try again.")
        print("> Character(s) not part of original string input.")
        quit()
    word = input("> Enter the word replacement: \n> ")

    print(str.replace(word_to_replace, word))

replaceWord()