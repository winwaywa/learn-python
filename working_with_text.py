# Python 3 đã tự cập nhật bằng cách chuyển sang Unicode làm mã hóa văn bản -> hỗ trợ các ký tự quốc tế

# tách chuỗi
from ast import pattern
import re
sent4 = "A much, much longer sentence"
print(sent4.rsplit(' ', 2))  # tách được maxsplit + 1 mục
print(sent4.partition(' '))  # trả về (head, sep, tail)
print(sent4.rpartition(' '))  # head lấy từ cuối chuỗi
print(sent4.partition('-'))  # ko có sep thì trả về sep, tail chuỗi trống

# join
s0 = "example"
s1 = "text"
sep = " "
print(sep.join([s0, s1]))
print(sep.join(s0))

# changing case
s3 = "eXamPLe tEXt"
print(s3.capitalize())  # Example text
print(s3.title())  # Example Text
print(s3.upper())
print(s3.lower())
print(s3.swapcase())  # ExAMplE TexT

# formatting
print(s3.center(37, '*'))  # *************eXamPLe tEXt************
print(s3.ljust(37, '*'))  # eXamPLe tEXt*************************
print(s3.rjust(37, '*'))  # *************************eXamPLe tEXt
print("123".zfill(5))  # 00123
print("one\ttwo\tthree".expandtabs())  # one     two     three

# Advanced Formatting - string.format(*args, **kwargs)
mystring = "value {0} equals {1}: {message}"
s4 = mystring.format('x', '23', message='[ok]')
print(s4)  # value x equals 23: [ok]
# !s <=> str()
# !r <=> repr()
mystring = "value {0!s} equals {1!r}: {message!s}"
s5 = mystring.format('z', '37', message='[well, you know ...]')
print(s5)  # value z equals '37': [well, you know ...]

# Format Specification
# Alignment Format Specifiers
astring = "Value {0!s:*^3} equals {1!s:0>4}: {message!s:!<42}"
s6 = astring.format('y', 42, message="[not bad ...]")
print(s6)  # Value *y* equals 0042: [not bad ...]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Sign Format Specifiers ( + - space)
#  Integer Format Specifiers
#  Float Format Specifiers

# Editing Strings
s7 = "  Nguyen Van Hiep"
print(s7.strip())
print(s7.lstrip("p"))
print(s7.rstrip("p"))
print(s7.replace("Hiep", "Doraemon"))

# Finding Strings
print("Hiep" in s7)  # True
print(s7.find("n"))  # 7 (index đầu tiên)
print(s7.rfind("n"))  # 11 (index cuối) , ko tìm thấy trả về -1
print(s7.index("n"))  # 7 , ko tìm thấy trả lỗi ValueError: substring not found
print(s7.rindex("n"))  # 11 , ko tìm thấy trả lỗi ValueError: substring not found
print(s7.count("n"))  # 2

# Regular Expressions
# Có thể tách một chuỗi theo các lần xuất hiện của một mẫu bằng cách sử dụng
# re.split (pattern, string [, maxsplit])
string = "Nguyen 7 Van 8 Hiep"
pattern = "\d"
print(re.split(pattern, string))  # ['Nguyen ', ' Van ', ' Hiep']
print(re.sub(pattern, "-", string))  # Nguyen - Van - Hiep
# ('Nguyen - Van - Hiep', 2) 2lần thay thế
print(re.subn(pattern, "-", string))
print(re.findall(pattern, string))  # ['7', '8']

# ---------------------- File
# read và b mode (chế độ binarychứa cùng thông tin ở định dạng byte ) ->    handle image or audio data
text = open("text.txt", 'rb')
# print(text.read())
print(text.readline(10))
for line in text:
    print(line)   # line cùng kết quả readline()
# write
out_file = open("text.txt", 'a')    # a mode : append, w: writing
# file.tell() trả về vị trí hiện tại của tệp, sử dụng b mode để chính xác
print(out_file.tell())
out_file.write("Nguyen Van Hiep \n")    # ghi chuỗi
out_file.writelines(["haha", "hihi"])   # ghi từng line của arr sequence
print(out_file.tell())
out_file.flush()
# file.seek(offset[, whence]): Đặt vị trí hiện tại của tệp, (whence: 0|1|2)
print(out_file.seek(0, 2))  # 2: vị trí cuối
out_file.close()
