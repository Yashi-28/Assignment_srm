n=int(input("Enter number of rows"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    m=n-(i-1)
    for j in range(1,m):
        print(" ",end=" ")
    for j in range(2,m):
        print(" ",end=" ")
    for j in range(i,0,-1):
        if(j==n):
            continue
        print(chr(64+j),end=" ")

    print()