
from random import random


vegetables = "carrots, potatoes, onions, leeks"
vegetables = vegetables.split(", ")
print(" ".join(vegetables))
print(list(vegetables))
print(tuple(vegetables))
print(str(vegetables))

print(len(vegetables))
print(vegetables.count('carrots'))
print(max(vegetables))
print(min(vegetables))

# If you want to make a tuple that only contains one item, you must follow the item with a single comma(item,).
tuple = (1,)
t = 'blah1', 'blah2', 'blah3'

lst = [1, "hai"]
lst.append("ba")
lst.extend([4, 5])
print(lst[:])  # [1, 'hai', 'ba', 4, 5]

# từ khoá del chỉ xoá tham chiếu khi del cái item
a = b = [1, 2, 3]
# del a
print(b)  # [1, 2, 3]

del (a[1:])
print(b)  # [2, 3]

vegetables.index("onions")  # [1]

vegetables.insert(2, "hiep")
print(vegetables)  # ['carrots', 'potatoes', 'hiep', 'onions', 'leeks']
vegetables.remove("hiep")
print(vegetables)  # ['carrots', 'potatoes', 'onions', 'leeks']

# xoá và trả về giá trị đã xoá
print(vegetables.pop(-1))

# stack
vegetables.append("stack")
vegetables.pop()

# queues
vegetables.append("queues")
vegetables.pop(0)

# sort
vegetables.sort()  # sắp xếp trực tiếp list, ko return giá trị
new_list = sorted(vegetables)  # trả về giá trị

vegetables.reverse()
reversed(vegetables)  # return iterator , có thể duyệt qua

# duyệt có thể lấy index, value
for index, value in enumerate(vegetables):
    print(index, "\t", value)

# duyệt qua 2 list cùng lúc
lst1 = [1, 2, 3, 4]
lst2 = ["một", "hai", "ba", "bốn"]
for value1, value2 in zip(lst1, lst2):
    print(value1, value2)

# list comprehension
upper_vegetables = [value.upper() for value in vegetables]
print(upper_vegetables)

int_list = [0, 1]
char_list = ['a', 'b', 'c']
l = [(an_int, a_char) for an_int in int_list for a_char in char_list]
print(l)

matrix = [['one', 'data', 'data'], [
    'data', 'two', 'data'], ['data', 'data', 'three']]
data_filter = [value for row in matrix for value in row if value is not 'data']
print(data_filter)

# set
a = set(['apples', 'oranges', 'bananas'])
b = set(['avocados', 'apples', 'grapes', 'mangos'])
print(a-b)
print(b-a)
print(a | b)
print(a & b)
# print(a[1])  # you can’t reference them with an index.

# dictionaries
# các giá trị lưu key là giá trị có thể băm, nếu bạn thay đổi nội dung của một giá trị có thể băm
# hàm băm kết quả cũng sẽ thay đổi và máy tính sẽ không thể định vị giá trị mà nó chứa nữa.
# => khóa phải thuộc loại dữ liệu immutable.
profile = {'Name': "Hiệp", 'Gender': "", 'Brainz': 0, 'Speed': 0}
for key in profile:
    print(key)
print(profile['Name'])
print(profile.get('haha', 'default value'))  # Nếu ko biết key đó có ko
print(profile.keys())
print(profile.values())
print(profile.items())
print(profile.fromkeys(profile, "default value"))  # copy dict trống
print(max(profile))  # Speed
print(min(profile))
print(len(profile))
del profile['Name']
print(profile.popitem())  # xoá và trả về cặp đã xoá
profile.clear()  # xoá hết
print(sorted(profile.items()))

sentence = "nguyen van hiep"
characters = {}
for c in sentence:
    characters[c] = characters.get(c, 0) + 1
print(characters)
