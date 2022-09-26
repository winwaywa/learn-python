from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name()

    def getName(self):
        return self.name


class Player(Person):
    def __init__(self, name, desc):
        # Person.__init__(self, name)  # tham chiếu đến một phương thức không liên kết
        super().__init__(name)  # super() thông minh hơn khi gọi một phương thức không liên kết
        self.desc = desc

    def __str__(self):
        return """
            Name: {name!s}
            Desc: {desc!s}
            """.format(**vars(self))
    # hàm này được gọi khi dùng với rep()-> trả về đại diện của đối tượng

    def __repr__(self) -> str:
        return """
            ---------Repr-------
            Name: {name!s}
            Desc: {desc!s}
            """.format(**vars(self))
    # len()

    def __len__(self):
        return len(vars(self))
    # dùng player1['name']

    def __getitem__(self, key):
        names = vars(self)
        try:
            item = names[key]
        except:
            item = 0
        return item

    # có thuộc tính chỉ đọc bí mật được gọi là __dict__ trả về dictionary được sử dụng để triển khai namespace của mô-đun
    # set
    def __setitem__(self, key, value):
        self.__dict__[key] = value
        return

   # del
    def __delitem__(self, key):
        del self.__dict__[key]
        return


# Các phương thức này thường được sử dụng để overloading toán tử trong python (Magic Methods or Dunder Methods)
# __iter__(self)
# __reversed__(self)
# __contains__(self, item)
player1 = Player("Hiep", "okkkkk")
print(repr(player1))
print(len(player1))  # 2
print(player1['name'])  # Hiep
# mutable type
player1['desc'] = "Ngu vc"
print(player1['desc'])  # Ngu vc
del player1['desc']
print(player1['desc'])  # 0
# dir() trả về những phương thức và thuộc tính của instance
# print(dir(player1))
# print(id(player1))  # identity

# ------------- Ví dụ Magic Methods or Dunder Methods


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial({!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x+y for x, y in zip(self.coeffs, other.coeffs)))


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 5)
print(p1+p2)  # Polynomial((4, 6, 8))

# abstract class


class Animal(ABC):
    @abstractmethod  # pthuc truu tượng
    def setName(self):
        pass

    def getName(self):
        print("get name")


class Dog(Animal):
    def setName(self):
        print("set name")


d1 = Dog()
d1.setName()
d1.getName()
# - Không thể khởi tạo đối tượng từ abstract class.
# - Cần ghi đè phương thức trừu tượng ở lớp con
print(isinstance(d1, Dog))  # True


# polymorphism
# Sử dụng tính đa hình thông qua các hàm như len(), nghĩa là sử dụng tương thích cho nhiều kiểu dữ liệu khác nhau.
print(len("Laptrinhtudau.com"))  # 17
print(len(["Python", "Java", "C++"]))  # 3
print(len({"name": "Chu Minh Nam", "age": 20, "sex": "nam"}))  # 3

# có thể tự khởi tạo một số hàm có tính đa hình


def tong(x, y, z=0):
    return x + y + z


print(tong(1, 2))
print(tong(1, 2, 3))
# Đa hình phương thức trong các lớp Python( Các phương thức cùng tên nhưng đối với đối tượng khác nhau cho ra kết quả #)
# Đa hình phương thức trong các lớp kế thừa Python ( phương thức trong lớp con override phương thức cha)


# Ví dụ chia sẻ thuộc tính giữa các instance ( giống static)
class Dog:
    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

# python hỗ trợ đa kế thừa và nó hiểu khai báo đa kế thừa từ phải qua trái.

# private variable
# Để tránh xung đột tên của tên với tên được xác định bởi lớp con
# nên có giới hạn hỗ trợ cho cơ chế như vậy, được gọi là name mangling
# Name mangling rất hữu ích để cho phép các lớp con ghi đè các phương thức mà không phá vỡ các lệnh gọi phương thức nội lớp


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


# _ : protected (truy cập _name : bình thường)
# __: private ( truy cập __name : lỗi AttributeError, nó sẽ thay biến đó thành _Student__name)
class Student:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newname):
        self.__name = newname


std = Student("Hiep")
print(std.__name)  # AttributeError
print(std._Student__name)  # Hiep

# Để có thể Iterators thì sử dụng các phương thức __iter __ () và __next __ ()
# Để ngăn việc lặp đi lặp lại mãi mãi, chúng ta sử dụng câu lệnh StopIteration

######################################################################


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')
print(iter(rev))
for char in rev:
    print(char)

# iterable :
# - một đối tượng mà bất kỳ người dùng nào cũng có thể lặp lại
# - dùng iter() để tạo ra iterator
# - Mọi iterator về cơ bản đều iterable

# iterator (trình lặp)
# - cũng là một đối tượng giúp người dùng lặp lại trên một đối tượng khác
# - sử dụng phương thức __next __ () để lặp lại
# - Không phải mọi iterable để là iterator
