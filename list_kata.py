# The variety of ways the print(), range() and f-string can be used

# 1. print('Integers from 1 to 20:')
num = list(range(1, 21))
print(f"num = {num}")

# 2. print('Evens from 1 to 20:')
for n in num:
    if n%2 == 0:
        print(f"The even numbers are {n}")

# 3. print('Odds from 1 to 20:')
for n in num:
    if n%2 != 0:
        print(f"The odd numbers are {n}")

# 4. print('Multiples of 5, from 5 to 100:')
for n in num:
    n *= 5
    print(n)

# 5. print('Squares of integers from 1 to 10:')
num2 = range(1, 11)
for n in num2:
    square_num = pow(n, 2)
    print(square_num)

# 6. print('Integers from 20 to 1:')
num3 = list(reversed(num))
print(f"num3 = {num3}")

# 7. print('Evens from 20 to 2:')
for n in num3:
    if n%2 == 0:
        print(f"num3_even = {n}")

# 8. print('Odds from 20 to 1:')
for n in num3:
    if n%2 == 0:
        print(f"The odd_num3  = {n}")

# 9. print('Multiples of 5 descending from 100 to 5:')
for n in num3:
    n*=5
    print(n)
# 10. print("Squares of integers descending from 10 to 1:")
num4 = list(range(10, 0, -1))
print(num4)

for n in num4:
    square_num = pow(n, 2)
    print(square_num)

# 11. print("Sum of integers from 1 to 20:")
print(sum(num4))

