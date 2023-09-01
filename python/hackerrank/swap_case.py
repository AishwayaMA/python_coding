def swap_case(s):
    x=''
    for i in s:
        if(i.islower()):
            i= i.upper()
        elif(i.isupper()):
            i= i.lower()
        x= x+i
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)