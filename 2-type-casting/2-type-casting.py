# 2-type-casting
# Python learning exercise

#converting strings
print(int("42"))            # 42
print(float("3.14"))        # 3.14
print(complex("2+3j"))      # (2+3j)
print(list("hello"))        # ['h', 'e', 'l', 'l', 'o']
print(tuple("hi"))          # ('h', 'i')
print(set("hello"))         # {'h', 'e', 'l', 'o'}
print(bool("text"))         # True

#converting integers
print(float(5))             # 5.0
print(complex(5))           # (5+0j)
print(str(5))               # "5"
print(bool(5))              # True
print(list(range(5)))       # [0, 1, 2, 3, 4]

#converting floats
print(int(3.99))            # 3
print(complex(3.5))         # (3.5+0j)
print(str(3.14))            # "3.14"
print(bool(0.0))            # False

#converting complex numbers
print(str(2+3j))            # "2+3j"
print(bool(2+3j))           # True

#converting lists
print(tuple([1, 2, 3]))     # (1, 2, 3)
print(set([1, 2, 3]))       # {1, 2, 3}
print(str([1, 2, 3]))       # "[1, 2, 3]"
print(bool([1, 2, 3]))      # True

#casting tuples
print(list((1, 2, 3)))      # [1, 2, 3]
print(set((1, 2, 3)))       # {1, 2, 3}
print(str((1, 2, 3)))       # "(1, 2, 3)"
print(bool((1,)))           # True

#casting sets
print(list({1, 2, 3}))      # [1, 2, 3]
print(tuple({1, 2, 3}))     # (1, 2, 3)
print(str({1, 2, 3}))       # "{1, 2, 3}"
print(bool({1}))            # True

#casting dictionaries
print(list({"a": 1, "b": 2}))     # ['a', 'b']
print(tuple({"a": 1, "b": 2}))    # ('a', 'b')
print(set({"a": 1, "b": 2}))      # {'a', 'b'}
print(str({"a": 1}))              # "{'a': 1}"
print(bool({"a": 1}))             # True

#casting booleans
print(int(True))           # 1
print(float(False))        # 0.0
print(str(True))           # "True"
print(complex(True))       # (1+0j)

#casting strings
b = b"ABC"
print(list(b))             # [65, 66, 67]
print(set(b))              # {65, 66, 67}
print(str(b))              # "b'ABC'"
print(bool(b))             # True

#casting byte array
ba = bytearray(b"ABC")
print(bytes(ba))           # b'ABC'
print(list(ba))            # [65, 66, 67]
print(str(ba))             # "bytearray(b'ABC')"
print(bool(ba))            # True

#casting None
print(str(None))           # "None"
print(bool(None))          # False
