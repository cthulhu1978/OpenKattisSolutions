def main():
    radius = int(input())
    PI = 3.14159265358979
    TAXICONST = 2.0000

    R2 = radius ** 2;

    print("%.6f" %(PI * R2))
    print("%.6f"% (TAXICONST * R2))



if __name__ == '__main__':
    main()
