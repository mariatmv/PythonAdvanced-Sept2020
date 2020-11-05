from _collections import  deque
import sys
jobs = deque([int(x) for x in input().split(', ')])
wanted_index = int(input())
clock_cycles = 0
while jobs:
    smallest = min(jobs)
    current_index = int(jobs.index(smallest))
    if current_index == wanted_index:
        clock_cycles += smallest
        break
    else:
        clock_cycles += smallest
        jobs[current_index] = sys.maxsize

print(clock_cycles)