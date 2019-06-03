def main():
    first_num, second_num = map(str, input().split())
    num_first = ""
    num_second = ""
    for x in range(len(first_num)):
        num_first +=(first_num[len(first_num) - (x+1)])
        num_second +=(second_num[len(second_num) - (x+1)])
    num_first = int(num_first)
    num_second = int(num_second)
    if num_first > num_second:
        print(num_first)
    else:
        print(num_second)


if __name__ == '__main__':
    main()
