def main():

    listA = [1,2,3,4]

    squareCubeList = [[a**2, a**3] for a in listA]
    print(squareCubeList)


if __name__ == '__main__':
    main()
