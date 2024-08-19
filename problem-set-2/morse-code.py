def morse(string):
    """Encodes a string into morse code"""
    # NOTE: The keys to this dictionary are all uppercase letters.
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/', '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '×': '-..-', '%': '----- -..-. -----', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }

    # TODO: Implement a way to convert the user's input into morse code in this function.
    # NOTE: IMPORTANT!!!! YOU MUST ADD A SPACE FOR EVERY CHARACTER CONVERTED INTO MORSE CODE!!!!
    # NOTE: Hello -> ......-...-..--- is WRONG!!! Hello -> .... . .-.. .-.. --- is CORRECT!!!
    pass

        

def main():
    # TODO: Prompt the user for input and print out the morse code version. You can print out accompanying text if you'd like, like "Original Text:", "Morse Code:".
    pass





if __name__ == "__main__":
    main()
