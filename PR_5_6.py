for i in range(2, 10001):
    divisors_sum = 1
    for j in range(2,i):
        if i % j == 0:
           divisors_sum += j
    if i == divisors_sum:
        print(i)