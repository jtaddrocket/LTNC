#Tính căn bậc hai theo phương pháp Newton:
#Để tính căn bậc hai của một số dương t, hãy bắt đầu với ước tính t = c. Nếu t = c/t thì t bằng căn bậc hai của c. Nếu không, hãy tinh chỉnh ước tính bằng cách thay thế t bằng giá trị trung bình của t và c/t và lặp lại cho tới khi nhận được kết quả có độ chính xác tới 15 chữ số sau dấu phẩy.
#Chú ý: Điều kiện dừng là abs(t - c/t) < (EPSILON * t). Với EPSILON = 10E-15.
def sqrt_newton(c):
    EPSILON = 1e-15
    t = c 
    while abs(t - c/t) >= (EPSILON * t):
        t = (t + c/t) / 2
    return t