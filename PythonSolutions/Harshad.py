def main():
    newString = input()
    num = int(newString)

    sum = summation(newString)
    while num % sum > 0:
        num = num + 1;

    print(num)

def summation(ns):
    sum = 0
    for char in ns:
        sum = sum + int(char)
    return sum

if __name__ == '__main__':
    main()
