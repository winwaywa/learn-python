
def chuyen(n, cot_1, cot_2):
    print("Chuyen dia thu %s từ %s sang %s" % (n, cot_1, cot_2))


def thapHaNoi(n, cot_1, cot_2, cot_3):
    if n == 1:
        chuyen(1, cot_1, cot_3)  # chuyển 1 từ 1 -> 3
    else:
        thapHaNoi(n-1, cot_1, cot_3, cot_2)  # chuyển n-1 cái trên sang cột 2
        chuyen(n, cot_1, cot_3)  # chuyển n từ 1 -> 3
        thapHaNoi(n-1, cot_2, cot_1, cot_3)  # cột 2 lúc này sẽ là 1, 1 là 2


thapHaNoi(3, "Cọc 1", "Cọc 2", "Cọc 3")
