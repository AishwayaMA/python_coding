#if __name__ == '__main__':
    n = int(input())
    s=""
    while(n>=1):
        s= str(n)+s
        n=n-1
    
    print(s)