def main():
    limit, events = map(int, input().split())
    sumOnTerrace = 0;
    groupsTurnedAway = 0;
    for n in range(events):
        direction, number = map(str, input().split())
        number = int(number)
        if direction == "enter":
            if number + sumOnTerrace > limit:
                groupsTurnedAway = groupsTurnedAway + 1
            else:
                sumOnTerrace = sumOnTerrace + number
        if direction == "leave":
            sumOnTerrace = sumOnTerrace - number
    print(groupsTurnedAway)



if __name__ == '__main__':
    main()
