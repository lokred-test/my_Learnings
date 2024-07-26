def solution(S):
    N = len(S)
    total_A = S.count('A')
    total_B = N - total_A  # Since the string only contains 'A' and 'B'
    
    min_deletions = float('inf')
    # Initialize counts of 'A's and 'B's seen so far
    count_A = 0
    count_B = 0
    
    for i in range(N):
        if S[i] == 'A':
            count_A += 1
        else:
            count_B += 1
        # Deletions needed to make all 'A's on the left and all 'B's on the right:
        # 1. Delete all 'B's before the current position i
        # 2. Delete all 'A's after the current position i

        # For each position i, we calculate the number of deletions required to achieve the desired order by:
        deletions = count_B + (total_A - count_A)
        # print(deletions)
        min_deletions = min(min_deletions, deletions)
    return min_deletions


# Example usage:
print(solution("BAAABAB"))  # Output: 2
print(solution("BBABAA"))   # Output: 3
print(solution("AABBBB"))   # Output: 0
