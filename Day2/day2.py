def read_txt(filename: str):

    file = open(filename, "r")

    file_contents = file.readlines()

    return file_contents


if __name__ == "__main__":

    contents = read_txt("input.txt")
    
    #Clean contents and separate into nested lists O(N^2)
    reports = []
    for i in range(len(contents)):
        contents[i] = contents[i].strip("\n")
        report = contents[i].split()

        for j in range(len(report)):
            report[j] = int(report[j])

        reports.append(report)
    
    safe_count = 0

    #Determine if report is safe O(N^2) optimized
    for report in reports:

        safe = True

        try:
            increasing = False
            decreasing = False
            if report[1] > report[0]:
                increasing = True
            if report[1] < report[0]:
                decreasing = True
        except:
            print("Length of Report is invalid. Not possible to check if safe.")

        for i in range(1, len(report)):

            #if there is no change
            if report[i] == report[i-1]:
                safe = False
                break

            #if increasing and it shouldn't or the increase is greater than 3
            if (report[i] > report[i-1] and not(increasing)) or (report[i] - report[i-1] > 3):
                safe = False
                break

            #if decreasing and it shouldn't be or if decrease is greater than 3
            if (report[i] < report[i-1] and not(decreasing)) or (report[i-1] - report[i] > 3):
                safe = False
                break

        if safe:
            safe_count += 1

    print(safe_count)

            
            

