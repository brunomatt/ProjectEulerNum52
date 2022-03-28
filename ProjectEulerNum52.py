# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
import time
start = time.time()

def deconstruct(num): #turns number into a list of its digits
    digits = [int(k) for k in str(num)]
    return digits

answer = []

for x in range(100,1000000):
    a = deconstruct(x)
    b = deconstruct(2 * x)
    c = deconstruct(3 * x)
    d = deconstruct(4 * x)
    e = deconstruct(5 * x)
    f = deconstruct(6 * x)
    if sorted(a) == sorted(b) == sorted(c) == sorted(d) == sorted(e) == sorted(f):
        answer.append(x)
        break
print(answer[0])

stop = time.time()
print(stop-start, "seconds")