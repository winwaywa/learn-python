# mixin là kỹ thuật để thêm vào nhiều class một tập các thuộc tính/method sẵn có giúp tái sử dụng code, khiến code ngắn gọn cô đọng hơn.

# Python hiểu khai báo đa kế thừa từ phải qua trái
class Mixin1(object):
    def test(self):
        print("Mixin1")


class Mixin2(object):
    def test(self):
        print("Mixin2")


class MyClass(Mixin1, Mixin2):
    pass


obj = MyClass()
obj.test()  # Mixin1
