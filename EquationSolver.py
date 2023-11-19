# giải phương trình f(x) = 0, tìm nghiệm xấp xỉ c theo phương pháp chia đôi.
def solver(f, a, b, e=0.000001):
    while abs(f(a) - f(b)) >= e:
        c = (a + b) / 2
        if abs(f(c)) <= e:
            break 
        if f(a) * f(c) < 0:
            b = c 
        else: 
            a = c 
    return c 