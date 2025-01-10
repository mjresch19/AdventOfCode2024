def read_txt(filename: str):

    file = open(filename, "r")

    file_contents = file.readlines()

    return file_contents


if __name__ == "__main__":

    contents = read_txt("input.txt")

    #strip newlines O(N)
    for i in range(len(contents)):
        contents[i] = contents[i].strip("\n")

    #add to lists O(N)
    list1 = []
    list2 = []
    for i in range(len(contents)):

        line1, line2 = contents[i].split()
        
        list1.append(int(line1))
        list2.append(int(line2))

    #sort lists (O logN)
    list1.sort()
    list2.sort()

    #calculate distance O(N)
    distance = 0
    for i in range(len(list1)):
        
        line_dist = list2[i] - list1[i]

        if line_dist < 0:

            line_dist = -(line_dist)

        distance += line_dist
    
    print(distance)



    

