#Ví dụ:
#Đầu vào cho trước: 
#A= 3786784723

#r = 0.12

#n = 6


#Đầu ra:
#Vay: 3,786,784,723.00 Đồng
#Lãi suất: 12.00%/tháng
#Trong: 6.00 tháng
#Mỗi tháng cần trả:  921,043,434.771 Đồng

def loan(A, r, n):
    X = A * ((1 + r) ** n) * r / ((1 + r) ** n - 1)
    print("Vay: {:,.2f} Đồng".format(A))
    print("Lãi suất: {:.2f}%/tháng".format(r * 100))
    print("Trong: {:.2f} tháng".format(n))
    print("Mỗi tháng cần trả: {:,.3f} Đồng".format(X))


loan(3786784723, 0.12, 6)
