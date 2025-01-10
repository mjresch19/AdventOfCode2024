def read_txt(filename: str):

    file = open(filename, "r")

    file_contents = file.readlines()

    return file_contents

if __name__ == "__main__":

    contents = read_txt("input.txt")

    #add to lists O(N)
    list1 = []
    list2 = []
    for i in range(len(contents)):

        line1, line2 = contents[i].split()
        
        list1.append(int(line1))
        list2.append(int(line2))

    #Make Dictionary of list1 contents with the key being the value in list1
    # and the value being the number of occurences that the value in list1 occurs O(N)
    loc_dict = {}

    for loc in list1:

        if loc not in loc_dict:
            loc_dict[loc] = 1
        else:
            loc_dict[loc] += 1

    #Make Dictionary of list2 contents with the key being the value in list1
    # and the value being the number of occurences that the value in list1 occurs O(N)
    loc2_dict = {}
    for loc in list2:

        if loc not in loc2_dict:
            loc2_dict[loc] = 1
        else:
            loc2_dict[loc] += 1

    #Iterate over Dictionary1, index into Dictionary2 with that value, if it exists, then we can 
    #perform some arithmetic optimized O(N)
    similarity_score = 0
    for key in loc_dict.keys():

        if key in loc2_dict:
            similarity_score += (key * loc_dict[key]) * loc2_dict[key]

    print(similarity_score)