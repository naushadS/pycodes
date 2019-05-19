# A new fighting game has become popular. There are N number of villains with each having some strength. There are N players in the game with each having some energy. The energy is used to kill the villains. The villain can be killed only if the energy of the player is greater than the strength of the villain.

# Maxi is playing the game and at a particular time wants to know if it is possible for him to win the game or not with the given set of energies and strengths of players and villains. Maxi wins the game if his players can kill all the villains with the allotted energy.


# Input Format
# The first line of input consist of number of test cases, T.

# The first line of each test case consist of number of villains and player, N.

# The second line of each test case consist of the N space separated strengths of Villains.

# The third line of each test case consist of N space separated energy of players.


# Constraints
# 1 <= T <= 10

# 1 <= N <= 1000

# 1 <= strength, energy <= 100000


# Output Format
# For each test case, Print WIN if all villains can be killed else print LOSE in separate lines.

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        p = input().strip().split(" ")
        v = input().strip().split(" ")
        p = list(map(int, p))
        p.sort()
        v = list(map(int, v))
        v.sort()
        win = True
        for i in range(len(p)):
            if v[i]-p[i] < 0:
                win = False
                break
        if win == True:
            print("WIN", end='\n')
        else:
            print('LOSE', end='\n')


if __name__ == "__main__":
    main()
