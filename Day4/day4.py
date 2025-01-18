from pprint import pprint

def read_txt(filename: str):

    file = open(filename, "r")

    file_contents = file.readlines()

    return file_contents


if __name__ == "__main__":

    #TOOD - finish this problem by checking if the report is safe
    contents = read_txt("Day4/input.txt")

    content_list = []
    for i in range(len(contents)):
        contents[i] = contents[i].strip("\n")
        content_list.append(list(contents[i]))

    pprint(content_list)

    for row in content_list:

        for cell in row:

            print(cell, "cell")