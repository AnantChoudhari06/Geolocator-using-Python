def find(n):
    # Code here
    sum=0
    for i in range(1,n+1):
        if i%3==0 or i%5==0:
            sum=sum+i
    return(sum)

print("Enter value of n")
n=int(input())
print(find(n))
