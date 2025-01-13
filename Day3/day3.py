import regex as re

def read_txt(filename: str):

    file = open(filename, "r")

    file_contents = file.read()

    return file_contents


if __name__ == "__main__":

    contents = read_txt("Day3/input.txt")

    #Extact all substrings mul, commas, parenthesis, and numerics O(N)
    mul_commands = re.findall(r"mul\(\d{1,3},\d{1,3}\)", contents, flags=re.MULTILINE)

    total = 0

    #extract values from the command
    for command in mul_commands:

        values = re.findall(r"\d{1,3}", command)

        total += int(values[0]) * int(values[1])

    print(total)