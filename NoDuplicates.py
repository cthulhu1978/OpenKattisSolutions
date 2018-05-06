

List = input().split(' ')

dupes = False

dupes = len(List) == len(set(List))

if(dupes):
    print("yes")
else:
    print("no")
