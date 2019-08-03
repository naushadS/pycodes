from sys import maxsize
import timeit


def maxSubArraySum1(a, size):

    max_so_far = -maxsize - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def maxSubArraySum2(a, size):

    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


a = [-2, -3, -4, -1, -2, -1, -5, -3]
print("1",timeit.timeit(stmt='maxSubArraySum1(a, len(a))',
                    setup="from __main__ import maxSubArraySum1; a = [-2, -3, -4, -1, -2, -1, -5, -3]",
                    number=100000))
print("2",timeit.timeit(stmt='maxSubArraySum2(a, len(a))',
                    setup="from __main__ import maxSubArraySum2; a = [-2, -3, -4, -1, -2, -1, -5, -3]",
                    number=100000))
