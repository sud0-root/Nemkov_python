# Дано целое число N (>0), являющееся некоторой степенью числа 2: N = 2 K. Найти
# целое число K — показатель этой степени.

N = int(input("Введите целое число N: "))

K = 0
while N > 1:
    N = N // 2
    K += 1

print("Показатель степени K:", K)