# The variety of ways the print(), range() and f-string can be used

print('1. Integers from 1 to 20:')
num = list(range(1, 21))
print(f"num = {num}")

print('2. Evens from 1 to 20:')
for n in num:
    if n%2 == 0:
        print(f"The even numbers are {n}")

print('3. Odds from 1 to 20:')
for n in num:
    if n%2 != 0:
        print(f"The odd numbers are {n}")

print('4. Multiples of 5, from 5 to 100:')
for n in num:
    n *= 5
    print(n)

print('5. Squares of integers from 1 to 10:')
num2 = range(1, 11)
for n in num2:
    square_num = pow(n, 2)
    print(square_num)

print('6. Integers from 20 to 1:')
num3 = list(reversed(num))
print(f"num3 = {num3}")

print('7. Evens from 20 to 2:')
for n in num3:
    if n%2 == 0:
        print(f"num3_even = {n}")

print('8. Odds from 20 to 1:')
for n in num3:
    if n%2 == 0:
        print(f"The odd_num3  = {n}")

print('9. Multiples of 5 descending from 100 to 5:')
for n in num3:
    n*=5
    print(n)

print("10. Squares of integers descending from 10 to 1:")
num4 = list(range(10, 0, -1))
print(num4)

for n in num4:
    square_num = pow(n, 2)
    print(square_num)

print("11. Sum of integers from 1 to 20:")
print(sum(num))

