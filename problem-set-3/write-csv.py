import csv


def getHeaders():
    # TODO: Prompt the user for input with these variables

    return header_1, header_2


def getData(header_1, header_2):
    # Initialize the first row of what we're going to use with .writerows() with the fieldnames (file headers)
    data = []
    temp_dict = {header_1: header_1, header_2: header_2}
    data.append(temp_dict)

    # TODO: Prompt the user thrice for the data in each row and append it to the list data.
    # NOTE: The CSV library expects a list of dictionaries with .writerows().
    

    return data


def writeCSV(rows, header_1, header_2):
    # TODO: Write to a CSV
    pass


def main():
    header_1, header_2 = getHeaders()
    rows = getData(header_1, header_2)
    writeCSV(rows, header_1, header_2)


if __name__ == "__main__":
    main()