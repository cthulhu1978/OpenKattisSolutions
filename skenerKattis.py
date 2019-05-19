def main():
    R, C, Zr, Zc = map(int,input().split())
    matrix = []

    for i in range(R):
        newLine = input()
        newList =""
        for j in range(Zr):
            newList = [i * Zc for i in newLine ]
            print(''.join(newList))

main()

