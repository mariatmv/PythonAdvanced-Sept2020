n = int(input())
longest_len = 0
longest = []
for i in range(n):
    args = input().split('-')
    first = list(map(int, args[0].split(',')))
    second = list(map(int, args[1].split(',')))
    first_set = set()
    second_set = set()
    for i in range(first[0], first[1] + 1):
        first_set.add(i)
    for i in range(second[0], second[1] + 1):
        second_set.add(i)
    intersection = first_set & second_set
    if len(intersection) > longest_len:
        longest = intersection
        longest_len = len(intersection)
longest2 = list(map(str, longest))
print('Longest intersection is [' +
      ", ".join(longest2) +
      f'] with length {longest_len}')
