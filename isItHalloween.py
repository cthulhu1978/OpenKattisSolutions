def main():
    month,day = map(str,input().split())
    if (month == "DEC") and (day == "25"):
        print("yup")
    elif (month == "OCT") and (day == "31"):
        print("yup")
    else:
        print("nope")

if __name__ == '__main__':
    main()
