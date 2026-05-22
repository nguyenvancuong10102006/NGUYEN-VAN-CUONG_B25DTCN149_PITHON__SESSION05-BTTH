while True:
    stass = int(input("Nhập số lượng nhân viên: "))
    for nhap in range(stass):
        name = input("Nhập tên: ")
        work = int(input("Số ngày làm việc: "))
        if work < 0 or work > 22:
            print("Dữ liệu không hợp lệ....! ")
            continue
        if work == 0:
            print("Nhân viên nghĩ toàn bộ tháng")
        elif work >= 18:
            print("làm việc chăm chỉ")
        elif work < 10:
            print("Làm việc ít")
        else:
            print("Làm việc bình thường")
        #
        print(name, ": ", end="")
        for i in range(work):
            print("*", end="")
        print()
