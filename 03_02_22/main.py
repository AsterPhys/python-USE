def f_dividers_except_1n(n):
    dividers = []
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            dividers.append(i)
            dividers.append(n // i)
    if int(n**0.5)**2 == n:
        dividers.append(int(n**0.5))
    return dividers


def f_dividers(n):
    dividers2 = f_dividers_except_1n(n)
    dividers2.append(1)
    dividers2.append(n)
    return dividers2


# task 1
print("Результат выполнения первой программы:")
with open("file1.txt") as f:
    data = f.readlines()
    k = 0
    for line in data:
        if line.count("AOA") > line.count("OAO"):
            k += 1
    print(k)
print("-"*41)

# task 2
print("Результат выполнения второй программы:")
with open("file2.txt") as f:
    data = f.readline()
    data = data.replace("A", " ")
    data = data.replace("B", " ")
    data = data.replace("C", " ")
    data = data.split()
    lens = []
    for i in data:
        lens.append(len(i))
    print(max(lens))
print("-"*41)

# task 3
print("Результат выполнения третьей программы:")
with open("file3.txt") as f:
    data = f.readline()
    s = ""
    while s in data:
        for i in "DBAC":
            s += i
    print(len(s) - 1)
print("-"*41)

# task 4
print("Результат выполнения четвертой программы:")
i_result = []
for i in range(326496, 649633):
    i_dividers = f_dividers_except_1n(i)
    k_odd = 0
    k_even = 0
    for j in i_dividers:
        if j % 2 == 0:
            k_even += 1
        else:
            k_odd += 1
    if k_even == k_odd and k_even >= 70:
        i_result.append(i)
i_max = max(i_result)
dividers_i_max = f_dividers_except_1n(i_max)
dividers_i_max.sort()
print(i_max, end=" ")
for i in dividers_i_max:
    if i > 1000:
        print(i)
        break
print("-"*41)

# task 5
print("Результат выполнения пятой программы:")
i = 350301
k = 0
result = {}
while k < 6:
    dividers_i = f_dividers(i)
    sum_dividers_i = sum(dividers_i)
    if sum_dividers_i % 13 == 0:
        k += 1
        result[i] = sum_dividers_i
    i += 1
for key in result:
    print(key, result[key] // 13)
print("-"*41)
