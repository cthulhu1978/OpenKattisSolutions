def main():
    totalPoints = 0
    numGuest = 0
    for x in range(5):
        a,s,d,f = map(int, input().split())
        newList = [a,s,d,f]
        sum = 0
        for num in newList:
            sum = (sum + num)
            if sum > totalPoints:
                totalPoints = sum
                numGuest = (x+1)

    print("{} {}".format(numGuest,totalPoints))
if __name__ == "__main__":
    main()
