numLines = int(input())

qaly = 0.0

for x in range(numLines):
    x,y = map(float, input().split())
    qaly = (qaly + (x*y))
print(qaly)
