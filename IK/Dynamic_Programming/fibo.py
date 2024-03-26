"""
Author: Soumil Ramesh Kulkarni
Date: 03.25.2024
"""
import time
def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num -1) + fibo(num - 2)

storage = {}
def fibo_dynamic_memoization(num):
    if num in storage:
        return storage[num]
    elif num <= 1:
        storage[num] = num
        return num
    else:
        storage[num] = fibo_dynamic_memoization(num - 1) + fibo_dynamic_memoization(num - 2)
        return storage[num]

def fibo_dynamic_bottom_up(num):
    table = [0]*(num + 1)
    # Base Cases
    table[0] = 0
    table[1] = 1
    # Iterative Instead of Recursive
    for i in range(2, num+1):
        #print(table)
        table[i] = table[i-1] + table[i-2]
    #print(table)
    return table[num]

start = time.process_time()
print(fibo(35))
print(time.process_time() - start)

start = time.process_time()
print(fibo_dynamic_memoization(35))
print(time.process_time() - start)

start = time.process_time()
print(fibo_dynamic_bottom_up(35))
print(time.process_time() - start)