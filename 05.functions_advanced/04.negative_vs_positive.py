def get_negatives(*args):
    l = []
    for i in args[0]:
        if i < 0:
            l.append(i)
    return l


def get_positives(*args):
    l = []
    for i in args[0]:
        if i >= 0:
            l.append(i)
    return l


nums = list(map(int, input().split()))
negatives_sum = sum(get_negatives(nums))
positives_sum = sum(get_positives(nums))
print(negatives_sum)
print(positives_sum)
if positives_sum > abs(negatives_sum):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')