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
        

def unique(list_of_words):
    # TODO: Iterate through this list of words and count how many times it appears. Return value should be a dictionary.
    pass


def main():
    # Open up the file in "read only" mode
    infile = open("harry-potter.txt", 'r')
    # Clean up the text output of the file
    text = cleanUpOutput(infile)
    
    #Identify what words appear in the text and how many times
    unique_words = unique(text)

    # NOTE: Unique words should be a dictionary with the value of each word being how many times that word appeared
    print(unique_words)

    # Close the file
    infile.close()


if __name__ == "__main__":
    main()