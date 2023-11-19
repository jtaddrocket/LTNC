# Viết chương trình cho phép nhập một số nguyên n từ bàn phím
# tính và in ra kết quả của biểu thức n + nn + nnn + nnnn
# Ví dụ n = 5, kết quả là 5 + 55 + 5555 + 5555 = 6170
# Chú ý: n có thể là số tự nhiên bất kỳ

n = int(input())

nn = int(f"{n}{n}")
nnn = int(f"{n}{n}{n}")
nnnn = int(f"{n}{n}{n}{n}")

print(n + nn + nnn + nnnn)