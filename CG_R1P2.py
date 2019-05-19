# In the XYZ society, the neighbours hate each other for their attitude. Various activities are organized in the society for Welcoming the New Year. The tickets were provided to each house with an integer written on it. Some got tickets with positive integers and some got tickets with negative integers. In the evening, people had to carry their tickets to the club house where the eligible ones will get the exciting gifts. The eligibility of winning the gift depends on the maximum sum which can be formed from the tickets numbers keeping in mind that neighbours hate each other. Since the neighbours hate each other, the two cannot be together in the list of maximum sum.

# The President of the society, Mr. Singh, is a wise man and know that neighbours in society don't like each other. Also, he don't wish to become bad in front of people. So, he came up with an idea to design a program which will provide the list of integers forming maximum sum and thus all the members of the list will be given the gifts. The only problem with this idea is that he don't know programming so he is asking you to provide the correct list of integers. The people may be annoying but are smart and will fight if the list provided by you doesn't form the maximum sum.


# Note: The integer written on ticket of individuals may or may not be unique. In case, when there are two list with equal maximum sum, the list with first greater element would be considered. For better understanding, look at the explanation of Test case 4 in Sample Test Case. The tickets with integer 0 are not considered for winning the gifts and there is atleast one ticket with positive integer.


# Input Format
# The first line of input consist of number of test cases, T.

# The first line of each test case consist of the number of houses(tickets distributed) in society, N.

# The second line of each test case consist of N space separated tickets with integer written on them.


# Constraints
# 1 <= T <= 10

# 1 <= N <= 10000

# -1000 <= Integer_on_Ticket <= 1000


# Output Format
# For each test case, print the ticket numbers in a single line forming the maximum sum in the format similar to Sample Test Case.

from collections import defaultdict

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        # n = int(input())
        n = 4
        # T = list(map(int,input().strip().split()))
        T = [4,5,4,3]
        max_ss(T)

def max_ss(arr):
    i,e = 0,0
    mttp = 0
    d = defaultdict(list)
    for j in arr:
        i_updated = e+j
        te = e
        e = max(i,e)
        i = i_updated
        m1 = max(i,te)
        if m1 > mttp:
            if te in d:
                d[m1].extend(d[te]+[j])
            else:
                d[m1] = [j]
            mttp = m1
    
    print("".join(list(map(str,d[mttp][::-1]))))

if __name__ == "__main__":
    main()
