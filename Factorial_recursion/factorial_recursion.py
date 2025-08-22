n=int(input("Enter a number"))
def func(n):
    if(n==1):
        return 1
    
    return n*func(n-1)
p=func(n)
print(p)    
