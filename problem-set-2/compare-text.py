import string


def cleanUpOutput(file):
    """ Remove any punctuations from words that may have been read in """
    # Read the text content of the file, strip the whitespace and seperate the words (since .read() reads the entire text file into one giant continuous list)
    contents = file.read().strip().split() 
    # Initialize an empty list to be used to append things into later
    filtered = []
    for word in contents:
        # For every word, use the translation map to replace the punctuation in a word (if any) with nothing (deleting it) and append it to "filtered"
        filtered.append(word.translate(str.maketrans("", "", string.punctuation)))
    
    # Return the filtered list of words, should be free of any punctuation (i.e "Hello!" -> "Hello")
    return filtered




#User-defined function of the intersection method of a set
def intersection(set1, set2):
    # TODO: Implement a way to perform the intersection method of a set
    pass


#User-defined function of the union method of a set
def union(set1, set2):
    # TODO: Implement a way to perform the union method of a set
    pass


#User-defined function of the difference method of a set
def difference(set1, set2):
    # TODO: Implement a way to perform the difference method of a set
    pass


#User-defined function of the symdif method of a set
def symdif(set1, set2):
    # TODO: Implement a way to perform the symmetric difference method of a set
        pass


def main():
    # Open up both text files in "read-only" mode
    try:
        with open("harry-potter.txt", 'r') as infile_1, open("lotr.txt", 'r') as infile_2:
            # Clean up the text output of both files
            text_1 = cleanUpOutput(infile_1)
            text_2 = cleanUpOutput(infile_2)
    except:
        print("Unable to open files")
        exit()


    # Initialize two empty sets 
    set_1 = set()
    set_2 = set()


    # TODO: Populate Set 1 and Set 2 with the words from text_1 and text_2
    # NOTE: text_1 and text_2 are both lists.


    # Print out stuff
    print("Unique words in Harry Potter: ", set_1)
    print("\n") # Output formatting
    print("Unique words in Lord of the Rings: ", set_2)
    print("\n") # Output formatting
    print("Unique words contained in both Harry Potter and LotR: ", union(set_1, set_2))
    print("\n") # Output formatting
    print("Words that appear in both Harry Potter and LotR: ", intersection(set_1, set_2))
    print("\n") # Output formatting
    print("Words that appear in Harry Potter but not LotR: ", difference(set_1, set_2))
    print("\n") # Output formatting
    print("Words that appear in LotR but not in Harry Potter: ", difference(set_2, set_1))
    print("\n") # Output formatting
    print("Words that appear in either Harry Potter or LotR, but not both: ", symdif(set_1, set_2))


if __name__ == "__main__":
    main()