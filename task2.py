def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
    
    return True 

def isFloatingPrime(num):
    # 1.43318 --> 143318
    onedigit = int(str(num[0])+str(num[1])) # 14
    twodigit = int(str(num[0])+str(num[1])+str(num[2])) #143
    threedigit = int(str(num[0])+str(num[1])+str(num[2])+str(num[3])) #1433
    if isPrime(onedigit) == True:
        return "TRUE"
    elif isPrime(twodigit) == True:
        return "TRUE"
    elif isPrime(threedigit) == True:
        return "TRUE"
    else:
        return "FALSE"

if __name__ == '__main__':
    floatinp = 1.0
    while floatinp >= 1.0:
        inp = str(input())
        if inp == "0.0":
            break
        floatinp = float(inp)
        inp_split = inp.split('.')
        num = ""
        for n in inp_split:
            num += n
        print(isFloatingPrime(num))
    
    