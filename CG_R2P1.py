'''
Rannvijay explains the task to you - "There are N boxes placed in a horizontal line infront of you with each box having a positive integer written on it. You have to tell me the maximum sum which can be formed by choosing the subset of boxes. Simple. But it is Roadies, so it can't be that simple. You have to tell me the maximum sum but the subset of boxes should not have any digit in common.

Let me give you an example, Suppose there are 5 boxes with positive integers as 14, 12, 23, 45, 39.
14 and 12 cannot be taken in the subset as 1 is common in both. Similarly {12, 23}, {23, 39}, {14, 45} cannot be included in the same subset.
So the subset which forms the maximum sum is {12, 45, 39}. The maximum sum such formed is 96.

Input Format
The first line of the input consists of the number of test cases, T.
The first line of input consists of the number of Boxes, N
The second line of each test case consists of N space separated boxes with positive integers on them.

Constraints
1 <= T <= 5
1 <= N <= 100
1 <= array elements <= 10 ^ 5

Output Format
Print the maximum sum which can be formed for each test case in a separate line.

Sample TestCase 1
Input
3
4
3 5 7 2
5
121 23 3 333 4
7
32 42 52 62 72 82 92

Output
17
458
92

Explanation
Test Case 1: {3, 5, 7, 2} = 17
Test Case 2: {121, 333, 4} = 458
Test Case 3: {92} = 92
'''
from collections import defaultdict
def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        B = input().strip().split()
        d = defaultdict(int)
        for i in B:
            k = {e for e in i}  #'122' -> {'1','2'}
            k_j = str("".join(sorted(k)))  #'12'
            for j in list(d):
                if no_common(k_j, j):
                    cmb = combine_e(k_j, j)
                    if cmb not in d:
                        d[cmb] = d[j]+int(i)
                    else:
                        d[cmb] = max(d[cmb], d[j]+int(i))
            if k_j in d:
                d[k_j] = max(d[k_j],int(i))
            else:
                d[k_j] = int(i)
        print(max(d.values()))

def no_common(n1, n2):
    return len(set([i for i in [int(j) for j in n1]]).intersection(set([i for i in [int(j) for j in n2]]))) == 0

def combine_e(fn, sn):
    l = set()
    for i in [fn, sn]:
        for j in i:
            l.add(j)
    return "".join(map(str, sorted([int(i) for i in l])))

if __name__ == "__main__":
    main()
#     T = int(input())
#    # T = 1
#     for _ in range(T):
#         # N = int(input())
#         N = 3
#         # B = list(map(int, input().strip().split()[:N]))
#         # B = [3,5,7,2] #17
#         B = [23,16,36] # 26+16=39
#         # B = [14,12,23,45,39] #96
#         # B = [33,449,985,663] #1648
#         # B = [3,1,4,14] #17
#         # B = [121, 23, 3, 333, 4] #458 [121 333 4]
#         # B = [32,42,52,62,72,82,92] #92
#         # print(B)
#         d = defaultdict(list)
#         i = 0
#         for ind,j in enumerate(B):
#             if n_common_list(d[i],j): # no common
#                 ti = i+j
#                 if ti > i:
#                     # if ti in d:
#                     d[ti].extend(d[i]+[j])
#                     # else:
#                         # d[ti].extend([j])
#                     i+=j
#             else: #common
#                 if i < j:
#                     # if n_common_list(d[i],j): #no common
#                     #     d[j].extend(d[i]+[j])
#                     # else:
#                     templ = rep(d[i].copy(),j,B,ind)
#                     i = sum(templ)
#                     d[i].extend(templ)
#                     # continue
#                     # i = j
#                 else:
#                     t9 = rep(d[i].copy(), j, B, ind)
#                     if t9 == False:
#                         pass
#                     else :
#                         templ = t9
#                         i = sum(templ)
#                         d[i].extend(templ)
#                 # i=j
#         print(i)

# def rep(l,n,B,ind):
#     # if sum(l) < n:
#     #     return [n]
#     sn = [i for i in str(n)]
#     setn = set(sn)
#     # l = list(map(str,l))
#     l_idx = []
#     for i in setn:
#         for idx,j in enumerate(l):
#             # no common
#             if not n_common_list(list(map(int, [k for k in str(j)])), i):
#                 # l[min_index] = n
#                 l_idx.append(idx)
#     # if len(l_idx)>1:
#     #     if sum([l[f] for f in l_idx])
#     min_index = min([(l[b],b) for b in l_idx])[1]

#     # if l[min_index] < n:
#     replaced_element = l[min_index]
#     # l[min_index] = n
#     # delete_indices = [c for c in l_idx if c not in [min_index]]
#     # l = [e for i, e in enumerate(l) if i not in delete_indices]
#     options = [item1 for item1 in B[:B.index(
#         replaced_element)+1] if item1 != replaced_element]  # [14,12]
#     if options:
#         s_m = [i for i in str(replaced_element)]
#         sets_m = set(s_m)  # {'2', '3'}
#         l_idx1 = []
#         for p in sets_m:
#             for idx2, j1 in enumerate(options):
#                 if not n_common_list(list(map(int, [k for k in str(j1)])), p):
#                     l_idx1.append(idx2)
#         if l_idx1:
#             delete_indices = [c for c in l_idx if c not in [min_index]]
#             l = [e for i, e in enumerate(l) if i not in delete_indices]
#             if len(l) != len(l_idx1):
#                 min_index1 = min_index
#             else:
#                 min_index1 = min([(l[b], b) for b in l_idx1])[1]
#                 l[min_index] = B[min_index1]
#             if l[min_index] < n:
#                 l[min_index] = n
#                 if not n_common(l[min_index],B[min_index1]):
#                     l.append(B[min_index1])
#         else:
#             if min_index > len(l)-1:
#                 pass
#             else:    
#                 l[min_index] = n
#     else:
#         l[min_index] = n
#     return l
#     # else:
#     #     return False

# def flatten(l):
#     tl = []
#     for sl in l:
#         if isinstance(int,sl):
#             tl.append(sl)
#         else:
#             for item in sl:
#                 tl.append(item)
#     return tl

# def n_common(int1, int2):
#     if len(set(str(int1)).intersection(str(int2))) == 0:
#         return False
#     else:
#         return True

# # if common return False
# def n_common_list(l,n):
#     l = list(map(str,l))
#     n = str(n)
#     flag = 0
#     for e in l:
#         if len(set(e).intersection(set(n))) != 0:
#             flag = 1
#             break
#         else:
#             continue
#     if flag == 1:
#         return False
#     else:
#         return True
