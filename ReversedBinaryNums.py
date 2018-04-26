number = int(input())

number = bin(number)

num = number[2:]


reverse = ''
num = str(num)

for ch in range(len(num),0,-1):
    reverse += (num[ch -1])

reverse = int(reverse,2)
print(reverse)
