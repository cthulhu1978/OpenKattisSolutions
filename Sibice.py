numMatches, width, height = map(int,input().split())

hypot = (width**2 + height**2)**0.5

for x in range(numMatches):
    match = int(input())
    if match <= hypot:
        print("DA")
    else:
        print("NE")
