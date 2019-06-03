
properList = [1,1,2,2,2,8]
k,Q,R,B,K,P = map(int,input().split())
actualList = [k,Q,R,B,K,P]
newList = [j - i for j,i in zip(properList,actualList)]
for n in newList:
    print(n, end=" ")
