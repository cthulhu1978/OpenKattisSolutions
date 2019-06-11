def main():
    line_list = input()
    final_list = []
    vowel_list = ['a','e','i','o','u']

    i = 0
    while i < len(line_list) :
        char = line_list[i]
        if char in vowel_list:
            final_list.append(char)
            i+=3
        else:
            final_list.append(char)
            i+=1

    new_string = ''.join(final_list)
    print(new_string)


if __name__ == '__main__':
    main()
