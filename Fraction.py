#Hoàn thiện các phương thức trong file Fraction.py theo các mô tả sau:

#Hàm is_minimalist_fraction(numerator, denominator) kiểm tra phân số gồm tử số là numerator, và mẫu số là denominator có phải phân số tối giản hay không nếu đúng trả lại giá trị là True, ngược lại trả lại giá trị là False?
import math 
def is_minimalist_fraction(numerator, denominator):
    if denominator == 0:
        return False 
    return math.gcd(numerator, denominator) == 1



#Hàm get_minimalist_fraction(numerator, denominator) thực hiện tính và trả lại phân số tối giản của phân số đầu vào (phân số được trả lại là 2 giá trị tương ứng là tử số và mẫu số)
def get_minimalist_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd 
    simplified_denominator = denominator // gcd 
    return simplified_numerator, simplified_denominator
