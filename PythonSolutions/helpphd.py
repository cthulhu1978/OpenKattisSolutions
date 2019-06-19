def main():

    digits = '0123456789'
    sum = 0

    answer_list = []
    num_cases = int(input())
    for x in range(num_cases):
        new_string = input()
        if(len(new_string)) == 1:
            pass
        elif new_string[0] in digits:
           first, second = new_string.split("+")
           sum = int(first) + int(second)
           answer_list.append(sum)
        else:
            if(new_string == "P=NP"):
                answer_list.append("skipped")
            else:
                pass
    for char in answer_list:
        print(char)





if __name__ == '__main__':
    main()