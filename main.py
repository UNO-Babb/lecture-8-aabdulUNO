def main():
    # Open the files we will be using
    inFile = open("names.dat", 'r')
    outFile = open("StudentList.csv", 'w')

    # Process each line of the input file and output to the CSV file
    for line in inFile:
        data = line.split()
        first = data[0]
        last = data[1]
        idNum = data[3]
        year = data[5]
        major = data[6]

        student_id = makeID(first, last, idNum)
        major_year = makeMajorYear(major, year)

        output = f"{last},{first},{student_id},{major_year}\n"
        outFile.write(output)

    # Close files in the end to save and ensure they are not damaged
    inFile.close()
    outFile.close()

def makeID(first, last, idNum):
    idLen = len(idNum)

    while len(last) < 5:
        last += "x"

    student_id = first[0] + last + idNum[idLen - 3:]
    return student_id

def makeMajorYear(major, year):
    # Abbreviate the major to the first three letters
    major_abbr = major[:3].upper()

    # Convert the year to its abbreviation
    if year == "Freshman":
        year_abbr = "FR"
    elif year == "Sophomore":
        year_abbr = "SO"
    elif year == "Junior":
        year_abbr = "JR"
    elif year == "Senior":
        year_abbr = "SR"
    else:
        year_abbr = "UNK"  # Handle unexpected year values

    # Combine major and year with a hyphen
    return f"{major_abbr}-{year_abbr}"

# Call the main function to execute the script
if __name__ == "__main__":
    main()
