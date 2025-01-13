import regex as re

def read_txt(filename: str):

    file = open(filename, "r")

    file_contents = file.read()

    return file_contents


if __name__ == "__main__":

    contents = read_txt("Day3/input.txt")

    #Extact all substrings mul, commas, parenthesis, and numerics O(N)
    do_commands = re.finditer(r"do\(", contents, flags=re.MULTILINE)
    dont_commands = re.finditer(r"don't\(", contents, flags=re.MULTILINE)
    mul_commands = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", contents, flags=re.MULTILINE)

    total = 0 

    do_indices = []
    for do in do_commands:
        do_indices.append(do.end(0))

    dont_indices = []
    for dont in dont_commands:
        dont_indices.append(dont.end(0))

    mul_indices = []
    for mul in mul_commands:
        mul_indices.append([mul.start(0), mul.end(0)])

    # print(do_indices)
    # print(dont_indices)
    # print(mul_indices)

    #determine mul commands that are not in do or dont commands
    #We can assume that we start out in an enabled state (do state)
    total = 0
    enabled_state = True
    while len(mul_indices) > 0:

        #We need to make a guard to check if our dos and donts are empty, if they are we break with our 
        #current state and finish up traversing our mul indices
        if len(do_indices) == 0 and len(dont_indices) == 0:
            break

        #We will use the start index for the mul index as the indicator of rather we are in do or don't territory
        #Note we could use end index too, the index is arbitrary, as long as it was captured as a mul command
        captured_dos = []
        captured_donts = []

        while len(do_indices) > 0 and mul_indices[0][0] > do_indices[0]:
            captured_dos.append(do_indices.pop(0))

        while len(dont_indices) > 0 and mul_indices[0][0] > dont_indices[0]:
            captured_donts.append(dont_indices.pop(0))
    

        #We have three different situations to check

        #If we have only captured dos
        if len(captured_dos) > 0 and len(captured_donts) == 0:
            enabled_state = True


        #If we have only captured donts
        elif len(captured_dos) == 0 and len(captured_donts) > 0:
            enabled_state = False
        
        #If we captured both dos and don'ts
        elif len(captured_dos) > 0 and len(captured_donts) > 0:
            
            if captured_dos[-1] > captured_donts[-1]:
                enabled_state = True
            else:
                enabled_state = False

        #We also have a fourth situation where we find, none. No logic is needed in this case. We simply continue
        if enabled_state:
            values = contents[mul_indices[0][0]:mul_indices[0][1]]

            values = re.findall(r"\d{1,3}", values)

            total += int(values[0]) * int(values[1])
        
        mul_indices.pop(0)

    #We need to check if we have any remaining mul commands
    if enabled_state:

        for mul in mul_indices:

            values = contents[mul[0]:mul[1]]

            values = re.findall(r"\d{1,3}", values)

            total += int(values[0]) * int(values[1])

    print(total)

    