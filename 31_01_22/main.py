# task 1
print("Результат выполнения первой программы:")
with open("file1.txt") as f:
    data = f.readlines()
    max_odd = 0
    for i in range(len(data)):
        data[i] = int(data[i])
        if data[i] % 2 != 0 and data[i] > max_odd:
            max_odd = data[i]
    result = []
    for i in range(len(data) - 1):
        if (data[i] + data[i + 1]) * 2 > max_odd:
            result.append(data[i] + data[i + 1])
    print(len(result), min(result))

print("-----------------------------------------")

# task 2
print("Результат выполнения второй программы:")
with open("file2.txt") as f:
    data = f.readlines()
    max_odd = 0
    min_odd = 100000
    for i in range(len(data)):
        data[i] = int(data[i])
        if data[i] % 2 != 0 and data[i] > max_odd:
            max_odd = data[i]
        if data[i] % 2 != 0 and data[i] < min_odd:
            min_odd = data[i]
    result = []
    for i in range(len(data) - 1):
        if (data[i] + data[i + 1]) % 2 == 0 and\
           (data[i] + data[i + 1]) > (max_odd + min_odd):
            result.append(data[i] + data[i + 1])
    print(len(result), min(result))

print("-----------------------------------------")

# task 3
print("Результат выполнения третей программы:")
for i in range(248015, 251576, 2):
    if int(i**0.5)**2 == i:
        print(i, int(i**0.5))

print("-----------------------------------------")

# task 4
print("Результат выполнения четвертой программы:")
i = 250001
k = 0
while k < 5:
    S = 0
    temp = i
    for j in range(2, int(i**0.5) + 1):
        while temp % j == 0:
            S += j
            temp //= j
    if S != 0 and S % 17 == 0:
        print(i, S)
        k += 1
    i += 1
