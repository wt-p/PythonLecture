def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


# 自作のgenertorもnext()で値を返し，iter()でiteratorを返している．
# generatorはiteratorの一種
even10 = even(10)
print(next(even10))
print(iter(even10))

print("=" * 30)
for i in even(10):
    print(i)

print("=" * 30)
even_gen = even(10)
print(next(even_gen))
print(next(even_gen))
print(id(iter(even_gen)))





