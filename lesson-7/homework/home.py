# Homework
# Task
# Learn about map and filter functions, and be prepared to explain them in class. Provide examples using these functions with lambda expressions.
# Problems
# 1. is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.
def is_prime(n):
    if n < 2:
        return False
    if n in range(2, int(n ** 0.5)+1):
        return False
    return True

# 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    return sum(int(digit) for digit in str(k))

# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.
def powers_of_two(N):
    k = 1
    while 2 ** k <= N:
        print(2 ** k, end=' ')
        k += 1
