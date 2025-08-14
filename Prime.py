def prime(n):
    prime=0
    p=(n//2)+1
    for i in range(2,p):
        if n%i == 0:
            prime=1
            break
    if prime==0:
        print(f"{n} is prime")    
    
for i in range(1,101):
    prime(i)


