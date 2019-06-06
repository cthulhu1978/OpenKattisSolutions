def main():
    test_case_list = []
    num_test_cases = int(input())
    for x in range(num_test_cases):
        total = parseLine()
        test_case_list.append(total)
    for result in test_case_list:
        print(result)



def parseLine():
    total = 0
    line_list = []
    line_list = input().split(" ")
    line_list = [int(i) for i in line_list]
    for x in range(len(line_list) - 1):
        if x == 0:
            pass # skip first
        elif line_list[x] == line_list[x-1]:
            pass # skip if no increase
        elif line_list[x] > (line_list[x-1] * 2):
            total += (line_list[x]) - (2 * (line_list[x-1]))
    return total

if __name__ == '__main__':
    main()
