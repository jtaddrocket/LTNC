# Chương trình kiểm tra một số có phải là số Siêu nguyên tố hay không
# Số siêu nguyên tố là số nguyên tố mà khi bỏ 1 số tùy ý các chữ số bên phải của nó thì phần còn lại vẫn là số nguyên tố

import math 

def isPrime(n):
    if n < 2:
        return False 
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False 
    return True 

def isSuperPrime(n):
    if n == 0:
        return False 
    while(n):
        if (isPrime(n) == False):
            return False 
        n //= 10
    return True 

if(isSuperPrime(int(input()))):
    print("True")
else:
    print("False")