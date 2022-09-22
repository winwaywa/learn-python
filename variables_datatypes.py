# không đặt tên biến trùng với từ khóa trong python
# -> hiển thị đỏ  (class, def...)
# -> lỗi khi chay (type, print)

# Variable names must begin with either a letter or an underscore.

# Every variable has a value; there's no such thing as an empty variable in Python.

# print(type(None))  <class 'NoneType'>

# python needs to keep track of the type of a variable for 2 main reasons:
# 1. to set aside enough memory to store the data
# 2. it will flag up a TypeError if you try to perform an inappropriate operation on that data. Ex: TypeError: 'int' object is not callable

# muốn biến trống , gán biến = None -> có kiểu là TypeNone

# Using Quotes

'a'

"a"

'''

a

b

'''

# Nesting Quotes

" ' "

' " '

""" " ' """

# Escaping Sequences (Trình tự thoát) :  \ (backslash)

# Using Special Whitespace Characters

# \n LineFeed (LF)

# \r Carriage return (CR)

# strings is immutable

# Operator Precedence (Quyền ưu tiên) theo operators bind tightest.

# ()

# **

# +x, -x, ~x

# *, /, //, %

# +, -

# <<, >>

# &

# ^

# |

# ==, !=, >, >=, <, <=, is, is not, in, not in

# not

# and

# or

# diving number

print(13/5)  # 2.6

print(13//5)  # 2

print(13 % 5)  # 3

# avoid using this operator with negative numbers

print(-13 // 5)  # -3

print(-13 % 5)   # 2

# -13 = -3 * 5 + 2

# Khi ép kiểu float -> int : mặc định làm tròn theo floor ( int(2.7) = 2 )

# Base 8 (Octal) -> sử dụng để chỉ định quyền đối với tệp

# 0o3765 = 3*512 + 7*64 + 6*8 + 5*1 = 2037

# oct()

# Base 16 (Hexadecimal) -> sử dụng để chỉ định màu

# A - F (10 - 15)

# 0x7F5 = 7*256 + 15*16 + 5*1 = 2037

# hex()

print(hex(2037), oct(2037))

# -------- more -----------

# each variable to which we assign a value/container is treated as an object. When we are assigning a value to a variable, we are actually binding a name to an object.
# Khi khai báo 1 biến mới, và gán giá trị cho nó là immutable thì địa chỉ của những biến này bằng nhau.
# Khi khai báo 1 biến mới, và gán giá trị cho nó là mutable thì địa chỉ của những biến này # nhau.
# khi gán một giá trị cũ cho giá trị mới thì cả cũ và mới đề cùng địa chỉ (immutable, mutable)

# Tất cả parameter (argument) trong Python được truyền bởi tham chiếu đối tượng (Pass by Object Reference).
# Nếu truyền vào immutable:  numbers, strings or tuples -> ko thể thay đổi biến ngoài
# Nếu truyền vào mutable : Lists, Dicts, Sets, User-Defined Classes, Dictionaries -> thay đổi được biến nằm ngoài function

# trinh thong dich
# sync
