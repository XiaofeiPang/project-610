list_a = list(range(1, 11))

print(list_a)

list_a = [x ** 2 for x in range(1, 11)]
#与列表对比，列表生成器：在内存中只存储了算法，不存储数据，节省了大量的空间，计算速度快，一般使用 yield一批一批的返回值
#一般使用for循环来遍历，很少使用next
g_a = (x ** 2 for x in range(1, 5))

print(list_a)
print(type(g_a))

print(next(g_a))
print(next(g_a))
print(next(g_a))
print(next(g_a))
# print(next(g_a))

for n in g_a:
    print(n)
