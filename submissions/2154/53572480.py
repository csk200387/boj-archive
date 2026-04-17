num = int(input())
print("".join([str(i) for i in range(1,num+1)]).find(str(num))+1)