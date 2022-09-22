# lớp cha của exception BaseException

store = []
# Create some exceptions and handle them
try:
    {}["foo"]
except KeyError as e:
    store.append(e)
try:
    1 / 0
except ZeroDivisionError as e:
    store.append(e)
try:
    "".bar()
except AttributeError as e:
    store.append(e)

# Loop over the store of errors and print out their class hierarchy
for exception_object in store:
    ec = exception_object.__class__
    print(ec.__name__)
    indent = " +-"
    while ec.__bases__:
        # Assign ec's superclass to itself and increase
        ec = ec.__bases__[0]
        print(indent + ec.__name__)
        indent = "  " + indent

# khi dùng exception tự định nghĩa, hoặc nhảy đến exception nào đó thì có thể sử dụng từ khóa raise.
# raise KeyError
# raise KeyError('foo')
# try:
#     {}['fhahahah']
# except KeyError as e:
#     raise

# Ví dụ tạo exception và dùng raise


class InvalidAgeException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    age = int(input("Nhập tuổi của bạn?"))
    if age < 18:
        raise InvalidAgeException(age)
    else:
        print("Tuổi hợp lệ")
except InvalidAgeException as e:
    print("Bắt được lỗi: ", e)
# Truy cập thuộc tính của ngoại lệ nâng cao


def log_error(err):
    """Simple logging method: writes error's details to standard output"""
    print("LOG:: {0}: {1}".format(err.__class__.__name__, err))


# KeyError: accessing a dictionary key that does not exist
try:
    d = {"foo":  "bar"}
    d["quux"]
except KeyError as e:
    log_error(e)
# TypeError: trying to perform an operation on incompatible operands
try:
    str = "" + 5
except TypeError as ex:
    log_error(ex)

# NameError: referring to a variable that does not exist
try:
    print(ex)
except NameError as exc:
    log_error(exc)
# Ví dụ với finally


def log_data(x, y):
    """Logs some incoming data, plus their division"""
    # Try logging some data to an open file
    try:
        f = open('finally_log.txt', 'a')
        f.write("{0:g} / {1:g} = {2:g}\n".format(x, y, (x/y)))
    # If there's a problem, log it, but then re-raise the error
    # Don't handle it locally
    except ZeroDivisionError:
        f.write("Error: tried to divide by zero\n")
        # raise #in ra lỗi và dừng chương trình
    # Whatever happens, close the file
    finally:
        f.close()


log_data(12.5, 29.1)
log_data(23.0, 84.3)
log_data(66.4, 55.9)
log_data(58.2, 0)

# Ví dụ với else


def divide_by_complex(x, y):
    """Division of two numbers with complex exception handling"""
    try:
        print("TRYING : beginning division of {0} / {1}".format(x, y))
        result = x / y
    except ZeroDivisionError:
        print("HANDLED: division by zero!")
    else:
        print("SUCCESS: result is {0:g}".format(result))
    finally:
        print("FINALLY: cleaning up")
# Nếu exception trong divide_by_complex() ko bắt thì ở ngoài bắt


try:
    # Normal behaviour
    divide_by_complex(2, 1)
    print()
    # Internally handled exception
    divide_by_complex(2, 0)
    print()
    # Raised exception
    divide_by_complex(2, None)
except Exception as e:
    print("RAISING: exception {0} not handled; « rising up".format(
        e.__class__.__name__))

# Nên dùng  EAFP Programming trong python hơn là LBYL Programming
# LBYL: not Pythonic
'''
if hasattr(some_object, 'result'):
    return some_object.result()
else:
    return None
'''

# EAFP: Pythonic
'''
try:
    return some_object.result()
except AttributeError:
    return None
'''
