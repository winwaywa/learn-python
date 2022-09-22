from package_example import *


from bs4 import BeautifulSoup  # format html

import urllib.request  # lấy data từ link gg


import datetime

import csv


from module_example import *


print(piratify("Hello, world."))

print(yarr("This is a test."))

print(me_hearties("It uses the strings module!"))


# Khi tạo module thì Trong pycache có file .pyc


# Hàm dir() được sử dụng để hiển thị các ký hiệu đã xác định(defined symbols)

print(dir(piratify))

# Hàm help() được sử dụng để hiển thị chuỗi tài liệu và cũng tạo điều kiện cho bạn thấy trợ giúp liên quan đến các mô-đun, từ khóa, thuộc tính, v.v.

print(help(piratify))


# module có chứa tham chiếu đến biến __name__


# package

# packages là không gian tên chứa nhiều gói và mô-đun.

# Mỗi gói trong Python là một thư mục PHẢI chứa một tệp đặc biệt được gọi là __init__.py

# =>  file này sẽ được tự động chạy khi bạn package được import.

# => file __init__.py này nhằm mục đích khởi tạo những thứ cần thiết cho package trong trường hợp bạn import package này

test.print_text()
