import math as m

def main():
    roundUp = False

    inputedMile = float(input())

    romanMile = 1000
    EnglishMileInPaces = romanMile * (5280/4854)

    totalPaces = inputedMile * EnglishMileInPaces

    remainder = (totalPaces % 1)
    if remainder >= 0.5:
        roundUp = True
        totalPaces = m.ceil(totalPaces)
    else:
        roundUp = False
        totalPaces = m.floor(totalPaces)

    print(totalPaces)


main()
