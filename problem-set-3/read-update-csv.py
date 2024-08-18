import csv


def printCSV():
    # TODO: Open the CSV file and print out the contents. 
    # NOTE: MAKE SURE TO PRINT A NEW LINE CHARACTER AT THE END!!! Since print() automatically adds a new line char '\n', add a print() at the end of this function
    pass


def updateCSV():
    # TODO: Update Hufflepuff's points to 420
    pass


def main():
    printCSV()
    # HINT: Since a CSV is basically just a text file, there's no dedicated way of updating a specific line. Thus, it is required to "overwrite" the entire
    # HINT: file to "update" something. Is there a way you can read everything from the CSV, change a particular thing, and then "update" (overwrite) the file?
    updateCSV()
    printCSV()

 
if __name__ == "__main__":
    main()