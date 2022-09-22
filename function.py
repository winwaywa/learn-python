
from threading import local


def collect_args(*number):
    print(number)  # (1, 2, 3, 4, 5)


collect_args(1, 2, 3, 4, 5)  # positional arguments


def collect_kwargs(**kwargs):
    print(kwargs)  # {'one': 1, 'two': 2, 'three': 3}


collect_kwargs(one=1, two=2, three=3)  # keyword arguments


def collect_args(b, e, a=432, c=512, *args, **kwargs):  # giống rest
    print(a, b, c, e)  # 432 486 512 648
    print(args)  # (576, 682, 768)
    print(kwargs)  # {'first': 729, 'second': 546, 'third': 819}


collect_args(486, 648, 432, 512, 576, 682, 768,
             first=729, second=546, third=819)

args = (486, 648, 432, 512, 576, 682, 768)
kwargs = {'first': 729, 'second': 546, 'third': 819}
collect_args(*args, **kwargs)  # giống spread


##### vars() , locals(), globals()
fred = 1
pete = 2


def cardboard_box():
    a = 3
    dave = fred + pete
    return vars()  # {'a': 3, 'dave': 3}
    return locals()  # {'a': 3, 'dave': 3}
    return globals()  # tất cả các biến global ngoài func


print(cardboard_box())


# Trog hàm có thể dùng biến ở ngoài
# Nhưng không thể gán lại dữ liệu biến ngoài, chỉ có thể thay đổi dữ liệu bên trong đv mutable object
out = 0


def change_value():
    out = 10
    print(out)  # 10


change_value()
print(out)  # 0


# Đưa biến bên trong hàm ra ngoài thì dùng global
fred = 1
pete = 2


def cardboard_box():
    global dave
    dave = fred + pete
    return vars()


print("Inside the box")
print(cardboard_box())  # {}
fred = dave
print("Outside the box:")
print(vars())  # có dave ở ngoài global


# Ví dụ scope and namespace(lưu dưới dạng từ điển(dictionary))

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)  # test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)  # nonlocal spam
    do_global()
    print("After global assignment:", spam)  # nonlocal spam


scope_test()
print("In global scope:", spam)  # global spam


# Generators function sẽ trả về yield thay vì return
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

# Generator Expressions sử dụng cú pháp giống list comprehensions nhưng dùng dấu ngoặc đơn thay vì vuông
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))  # ['f', 'l', 'o', 'g']
