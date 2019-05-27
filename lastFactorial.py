def main():
    testCases = int(input())
    factorial = 1
    newList = []
    for x in range(testCases):
        num = int(input())
        for i in range(num):
            factorial = factorial * (i+1)
        newList.append(factorial)
        factorial = 1
    for num in newList:
        print(num % 10)

if __name__ == "__main__":
    main()
