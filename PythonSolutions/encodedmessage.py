from math import sqrt as sq

def main():
    num_cases = int(input())
    for o in range(num_cases):

        my_line_list = []
        line = input();
        len_line = len(line)
        row_col_len = sq(len_line)

        n = int(row_col_len)
        m = int(n)
        constD = 0;
        for y in range(int(n)):
            for x in range(int(n)):
                my_line_list.append(line[(n - constD) + (m * x) - 1])
                print(line[(n - constD) + (m * x) - 1], end="")
            constD += 1
        print()


if __name__ == '__main__':
    main()
