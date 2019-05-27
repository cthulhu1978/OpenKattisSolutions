def main():
    # variables
    limitingFactor = 500
    tablet = 0
    compass = 0
    gear = 0
    pointTotal = 0
    # get input and check for chars
    inputString = input()
    for char in inputString:
        if char.upper() == 'T':
            tablet = tablet + 1
        elif char.upper() == 'C':
            compass = compass + 1
        elif char.upper() == 'G':
            gear = gear + 1
        else:
            print("enter valid chars")

    # create list of the variables with respective number of cards
    gearList = [tablet,compass,gear]
    # check for the bonus points
    for gear in gearList:
        if gear < limitingFactor:
            limitingFactor = gear
    limitingFactor = (limitingFactor * 7)

    # add up points
    for item in gearList:
        pointTotal = pointTotal + item ** 2
    print(pointTotal + limitingFactor)

if __name__ == "__main__":
    main()
