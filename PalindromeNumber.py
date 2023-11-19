#Hoàn thiện hàm is_palindrome(p), hàm này thực hiện kiểm tra số nguyên p có phải là số đối xứng hay không, nếu có thì trả lại giá trị True, và ngược lại thì trả lại giá trị False.

def is_palindrome(p):
    check = p
    reversed_number = 0 
    while (p > 0):
        reversed_number = reversed_number * 10 + p % 10 
        p //= 10 

    if (reversed_number != check):
        return False 
    return True
