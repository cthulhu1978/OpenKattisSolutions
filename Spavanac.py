def main():
    hour,minute = map(int,input().split())
    newMinute = 0
    newHour = 0

    if minute < 45:
        newMinute = ((minute - 45) + 60)
        if hour == 0:
            newHour = 23
        else:
            newHour = hour - 1
    else:
        newMinute = (minute - 45)
        newHour = hour

    print( "{} {}".format(newHour,newMinute) )

if __name__ == "__main__":
    main()
