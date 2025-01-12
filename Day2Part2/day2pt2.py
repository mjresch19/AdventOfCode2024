def read_txt(filename: str):

    file = open(filename, "r")

    file_contents = file.readlines()

    return file_contents


if __name__ == "__main__":

    #TOOD - finish this problem by checking if the report is safe
    contents = read_txt("Day2Part2/input.txt")
    
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

        if report == [27, 24, 26, 29, 30, 33, 36]:
            print("FOUND")

        safe_shield = True
        index_bump = 0
        safe = True
        at_index_bump = 0

        try:
            increasing = False
            decreasing = False
            if report[1] > report[0]:
                increasing = True
            if report[1] < report[0]:
                decreasing = True
        except:
            print("Length of Report is invalid. Not possible to check if safe.")
            safe = False

        for i in range(1, len(report)):

            #if there is no change
            if report[i] == report[i-1-index_bump]:

                if not(safe_shield):
                    safe = False
                    print(report)
                    break
                safe_shield = False
                index_bump += 1
                at_index_bump = i
        
            #if increasing and it shouldn't or the increase is greater than 3
            if (report[i] > report[i-1-index_bump] and not(increasing)) or (report[i] - report[i-1-index_bump] > 3):
                if not(safe_shield):
                    safe = False
                    print(report)
                    break
                safe_shield = False
                index_bump += 1
                at_index_bump = i

            #if decreasing and it shouldn't be or if decrease is greater than 3
            if (report[i] < report[i-1-index_bump] and not(decreasing)) or (report[i-1-index_bump] - report[i] > 3):
                if not(safe_shield):
                    safe = False
                    print(report)
                    break
                safe_shield = False
                index_bump += 1
                at_index_bump = i

            #We check last if first index was removed, if it was, then we have to calcualte whether our report should be increasing or decreasing
            if not(safe_shield) and i == 1:
                try:
                    increasing = False
                    decreasing = False
                    if report[2] > report[1]:
                        increasing = True
                    if report[2] < report[1]:
                        decreasing = True
                except:
                    print("Length of Report is invalid. Not possible to check if safe.")
                    safe = False
                    print(report)

                    break

            #We only want to bump the index once, so once that happens we should eliminate the index bump
            if at_index_bump < i:
                index_bump = 0



        if safe:

            if index_bump == 1:
            #Final check to see if last index is valid if a replacement was made (we need to check both the last and second to last index to see if either would work)
                if report[-1] == report[-3]:
                    
                    if report[-2] == report[-3]:
                        print(report)
                        continue
                    if (report[-2] > report[-3] and not(increasing)) or (report[-2] - report[-3] > 3):
                        print(report)                        
                        continue
                    if (report[-2] < report[-3] and not(decreasing)) or (report[-3] - report[-2] > 3):
                        print(report)                        
                        continue


                if (report[-1] > report[-3] and not(increasing)) or (report[-1] - report[-3] > 3):
                    
                    if report[-2] == report[-3]:
                        print(report)
                        continue
                    if (report[-2] > report[-3] and not(increasing)) or (report[-2] - report[-3] > 3):
                        print(report)
                        continue
                    if (report[-2] < report[-3] and not(decreasing)) or (report[-3] - report[-2] > 3):
                        print(report)
                        continue

                if (report[-1] < report[-3] and not(decreasing)) or (report[-3] - report[-1] > 3):

                    if report[-2] == report[-3]:
                        print(report)
                        continue
                    if (report[-2] > report[-3] and not(increasing)) or (report[-2] - report[-3] > 3):
                        print(report)
                        continue
                    if (report[-2] < report[-3] and not(decreasing)) or (report[-3] - report[-2] > 3):
                        print(report)
                        continue


            safe_count += 1

    print(safe_count)