# 引数と戻り値の型のヒントをつけることができる．(Type annotation)
def add_nums(num1: int, num2: int) -> int:
    return num1 + num2

# pythonは動的型付け言語
print(add_nums(1, 2))
