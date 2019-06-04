def main():
    numDataSets = int(input())
    finalValues = []
    # loop through and calculate each answer, store in list.
    for x in range(numDataSets):
    # zero out variables each time
        square_and_add = 0; conversion = 0;
        setNumber = 0; base = 0; numToConvert = 0;

        setNumber, base, numToConvert = map(int, input().split())
        conversion = ConvertBase(base, numToConvert)
        square_and_add = SquareAndAdd(conversion)
        finalValues.append(square_and_add)
    # print final list
    for i in range(numDataSets):
        print("{} {}".format( (i+1) , finalValues[i]))

# convert to a specified base and return a string
def ConvertBase(base, numToConvert):
    number_string = ""
    number_list = []
    while numToConvert != 0:
        rem = numToConvert % base
        quot = int(numToConvert / base)
        numToConvert = quot
        number_list.insert(0,str(rem))
    return number_list

# cycle through list, convert to int and square, add to sum
def SquareAndAdd(conversion_num):
    sum = 0
    for char in conversion_num:
        char =  ( int(char) ) ** 2
        sum += char
    return sum

# fire off main
if __name__ == '__main__':
    main()
