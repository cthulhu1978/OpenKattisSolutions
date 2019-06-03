num1, num2, num_range = map(int,input().split())
num_range +=1

for x in range(1,num_range):
    if(x % num1 == 0 and x % num2 == 0):
        print("FizzBuzz")
    elif(x % num1 == 0):
        print("Fizz")
    elif(x % num2 == 0):
        print("Buzz")
    else:
        print(x)
